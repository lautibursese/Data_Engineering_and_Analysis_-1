import mysql.connector


if __name__ == "__main__":
    mydb = mysql.connector.connect(
        # host="35.232.179.155",
        host='localhost',
        user="root",
        password="root"
    )

    # creamos la base de datos "olist_db"

    # abrimos el archivo
    path_schema = "./schema.sql"
    with open(path_schema, "r") as file:
        schema = file.read()

    # ejecutamos el archivo
    cursor = mydb.cursor()
    cursor.execute(schema)
    cursor.close()
    mydb.close()




