
#HOMEWORK 28/07/25 PART 1 OF 2:

import psycopg2
import psycopg2.extras


## connect to postgres server
try:
    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='admin',
        host='localhost',
        port='5432',
        cursor_factory=psycopg2.extras.RealDictCursor
    )
    print("Connected successfully.")
except psycopg2.Error as e:
    print("Connection error:", e)

## Creating new table
try:
    cur = conn.cursor()
    cur.execute(
    ''' CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    price NUMERIC(6, 2) NOT NULL,
    in_stock BOOLEAN DEFAULT TRUE);
    ''')
    conn.commit()
    print("Table was created")
except psycopg2.Error as e:
    print("Error creating table")
finally:
    cur.close()


#creating data to insert in a table:
data_products = [('Laptop', 3200.50, True),
                ('Mouse', 99.99, True),
                ('Keyboard', 250.00, False),
                ('Monitor', 1190.95, True)]

## Inserting new data to create a table and deleting other data if it exists
try:
    cur = conn.cursor()
    cur.execute("DELETE FROM products;")
    cur.executemany('''INSERT INTO products (name, price, in_stock)
     VALUES (%s, %s, %s);''', data_products)
    conn.commit()
    print("Data inserted to the table")
except psycopg2.Error as e:
    print("Error with inserting data")
finally:
    cur.close()

#Search for relevant data and print it (Products that are in stock - True)
try:
    cur = conn.cursor()
    cur.execute('''SELECT * FROM products WHERE in_stock = TRUE;''')
    print("Products in stock:\n")
    products = cur.fetchall()
    for row in products:
            print(row["name"])
except psycopg2.Error as e:
    print("Something went wrong with your products")
finally:
    cur.close()





