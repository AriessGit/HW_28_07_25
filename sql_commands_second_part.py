import streamlit as st
import psycopg2
import psycopg2.extras

def get_connection():
    return psycopg2.connect(dbname='postgres', user='postgres', password='admin',
                            host='localhost', port='5432', cursor_factory=psycopg2.extras.RealDictCursor)

def fetch_query(query: str) -> list:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def shop_list():
    rows = fetch_query("SELECT * FROM products")
    if rows:
        for row in rows:
            st.write(f"Product id: {row['product_id']}  /  Item: {row['name']}  /  Price: {row['price']}  /  Available: {row['in_stock']}")

def shop_list_available():
    rows = fetch_query("SELECT * FROM products WHERE in_stock = TRUE")
    if rows:
        for row in rows:
            st.write(f"Product id: {row['product_id']}  /  Item: {row['name']}  /  Price: {row['price']} ")

def price_calculation():
    st.subheader("Calculate the price by yourself!")
    st.write("Calculate the price for few items:")
    item_price = st.number_input("Item price:")
    item_amount = int(st.number_input("Amount:",min_value=1, step=1))

    if st.button("View total price"):
        price = item_price *  item_amount
        st.success(f"Total price is: {price}")

def session_sec():
    # The next 3 "if" conditions is for a session_state command.
    # I used this command to store and remember values or user actions (like button clicks) across reruns of Streamlit website.

    if "calculation_price" not in st.session_state:
        st.session_state.calculation_price = False

    if st.button("Show Available Products"):
        st.session_state.calculation_price = True

    if st.session_state.calculation_price:
        shop_list_available()
        price_calculation()

    if st.button("Hide Products"):
        st.session_state.calculation_price = False

def math_operations():
    first_num = st.number_input("First number:")
    second_num = st.number_input("Second number:")

    st.subheader("Select one of the options:")

    if st.button("ADD"):
        add_sum = first_num + second_num
        st.success(f"The number is: {add_sum}")

    if st.button("SUBTRACT "):
        sub_sum = first_num - second_num
        st.success(f"The number is: {sub_sum}")

    if st.button("MULTIPLY "):
        mul_sum = first_num * second_num
        st.success(f"The number is: {mul_sum}")

    if st.button("DIVIDE "):
        try:
            div_sum = first_num / second_num
            st.success(f"The number is: {div_sum}")
        except ZeroDivisionError as e:
            st.error("Cannot divide by 0. Please try another number")


