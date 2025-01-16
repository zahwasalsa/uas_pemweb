import pymysql

def connect():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="dbuas",
        cursorclass=pymysql.cursors.DictCursor
    )

def fetch_all_items():
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM list")
            rows = cursor.fetchall()
            return rows
    finally:
        connection.close()

def insert_item(name, harga, qty):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO list (name, harga, qty) VALUES (%s, %s, %s)",
                (name, harga, qty)
            )
            connection.commit()
            return 1
    finally:
        connection.close()

def update_item(item_id, name, harga, qty):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE list SET name = %s, harga = %s, qty = %s WHERE id = %s",
                (name, harga, qty, item_id)
            )
            connection.commit()
            return 1
    finally:
        connection.close()

def fetch_item_by_id(item_id):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM list WHERE id = %s", (item_id,))
            rows = cursor.fetchone()
            return rows
    finally:
        connection.close()

def delete_item(item_id):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM list WHERE id = %s", (item_id,))
            connection.commit()
            return 1
    finally:
        connection.close()