from mysql.connector import connect, Error

# import csv
#
# with open("organizations.csv", "r") as file:
#     data = []
#     csvreader = csv.reader(file)
#     for row in csvreader:
#         data.append(row)
#         print(row)
#     print(csvreader)
#
# print("imported")
# # SQl does not like . (dots in variable names) replacing them with underscores!
# names = data[0]
# names = [x.replace(".", "_") for x in names]
# data = [x[1:12] for x in data[1:708]]
#
#
# def converter(accept):
#     print(len(accept))
#     changed = tuple(accept)
#     return changed
#
#
# def final_list(accept):
#     print(type(accept))
#     out = []
#     for i in range(len(accept)):
#         print(i)
#         converted = converter(accept[i])
#         print(type(converted))
#         out.append(converted)
#         pass
#     return out


# values = final_list(data)

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
        select_data = "SELECT * FROM organization"


        def get_data():
            with connection.cursor() as cursor:
                # cursor.execute(create_ngo)
                cursor.execute(use_ngo)
                # cursor.execute(create_organization_table)
                # cursor.executemany(insert_to_organization, values)
                cursor.execute(select_data)
                data = []
                for item in cursor:
                    data.append(item)
                connection.commit()
                print(len(data))
            return data
        result = get_data()
        print(result)


except Error as e:
    print(e)
