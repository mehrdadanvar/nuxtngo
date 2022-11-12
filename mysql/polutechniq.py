import requests as r
from bs4 import BeautifulSoup as bs
from mysql.connector import connect, Error

main_url = "https://www.kpu.ca/arts/ngo/nonprofit-database"


def get_sites():
    response = r.get(main_url)
    print(response.status_code)
    page = bs(response.text, "lxml")
    cont = page.select("div.Table-Container")
    return cont


tables = get_sites()
table = tables[1]
rows = table.select("tr")
rows = rows[1:97]

images = [x.img for x in rows]


def get_image_links(x):
    result = []
    for i in range(len(x)):
        if x[i] == None:
            result.append("null")
        else:
            result.append(x[i]["src"])
    return result


image_links = get_image_links(images)

names = [x.select("td a")[0] for x in rows]
names = [x.get_text() for x in names]


def const_values_for_sql(names, image_links):
    inter = []
    for i in range(len(names)):
        inter.append((i + 1, names[i], image_links[i]))
    return inter


values = const_values_for_sql(names, image_links)

try:
    with connect(
            host="localhost",
            user="developer",
            password="developer",
    ) as connection:
        print("successfully connected to local host")
        use_ngo = "use ngo"
        print("selected")
        create_poly_table = "CREATE TABLE poly (ID int NOT NULL,org_name varchar(255),image_link varchar(255), PRIMARY KEY (ID))"
        insert_to_poly = "insert into poly values (%s,%s,%s)"
        with connection.cursor() as cursor:
            cursor.execute(use_ngo)
            cursor.execute(create_poly_table)
            cursor.executemany(insert_to_poly, values)
            connection.commit()
            print("success")

except Error as e:
    print(e)
