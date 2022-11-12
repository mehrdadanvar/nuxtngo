from flask import Flask
from flask_cors import CORS
from mysql.connector import connect, Error

app = Flask(__name__)
CORS(app)


def get_data():
    try:
        with connect(
                host="localhost",
                user="developer",
                password="developer",
        ) as connection:
            print("successfully connected to local host ")
            # create_ngo = "create database ngo"
            use_ngo = "use ngo"
            print("selected")
            # create_organization_table = "CREATE TABLE organization (_id VARCHAR(255), address VARCHAR(255), category VARCHAR(255), description VARCHAR(4000), identity VARCHAR(255), link VARCHAR(255), name VARCHAR(255), person VARCHAR(255),phone VARCHAR(255),social_brans VARCHAR(255), social_links VARCHAR(4000))"
            # insert_to_organization = "insert into organization values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            select_data = "SELECT JSON_ARRAYAGG(JSON_OBJECT('link',link)) from organization"
            with connection.cursor() as cursor:
                # cursor.execute(create_ngo)
                cursor.execute(use_ngo)
                # cursor.execute(create_organization_table)
                # cursor.executemany(insert_to_organization, values)
                cursor.execute(select_data)
                data = []
                for item in cursor:
                    print(len(item))
                    data.append(item)
                    print(type(data))
                connection.commit()
                return data

    except Error as e:
        print(e)


@app.route("/", methods=["GET"])
def hello_world():
    print("run hello")
    result = get_data()
    print(type(result))
    print(len(result))
    # x = result[1]
    # corrected = {"mongo_id": x[0], "address": x[1], "category": x[2], "description": ast.literal_eval(x[3]),
    #              "link": x[5]}
    # print(corrected)
    return result
