import streamlit as st

st.title('HELLO WORLD')

st.button("Reset", type = "primary")
if st.button("say hello"):
    st.write("why hello there")
else:
    st.write("Goodbye")    




st.title('Calculator App Using Streamlit 📖')


num1 = st.number_input(label = "Enter first number")
num2 = st.number_input(label = "Enter secoond number")

st.write("operation")
operation = st.radio("select an operation to perform :", ("Add", "Subtract", "Multiply", "Divide"))

ans = 0

def calculate():
    if operation == "Add":
        ans = num1 + num2
    elif operation == "Subtract":
        ans = num1 - num2
    elif operation == "Multiply":
        ans = num1 * num2
    elif operation=="Divide" and num2!=0:
        ans = num1 / num2
    else:
        st.warning("Division by 0 error. Please enter a non-zero number.")
        ans = "Not defined"
    
    st.success(f"Answer = {ans}")

if st.button("Calculate result"):
    calculate()