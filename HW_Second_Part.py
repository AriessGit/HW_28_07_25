#HOMEWORK 28/07/25 PART 2 OF 2:

import streamlit as st
from sql_commands_second_part import *

st.title("Arie's Web Calculator & Shop")
st.subheader("Here, you can easily perform simple math operations, explore available products, and calculate prices on your own - All in my awesome store! Enjoy!")

menu = st.selectbox("Choose action:", [" ", "Shop Products", "Calculator"])

if menu == "Shop Products":
    st.subheader("ARIE'S SHOP PRODUCTS:")
    st.write("To see all available products, please click below:")

    if st.button("Show All Products"):
        shop_list()
    st.write("To see available products in shop:")
    session_sec()

if menu == "Calculator":
    math_operations()
