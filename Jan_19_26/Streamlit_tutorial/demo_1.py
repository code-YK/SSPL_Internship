import streamlit as st

# Demo Streamlit App
# This demonstrates basic Streamlit functionalities:
#    - Title and Subheader
#    - Text display
#    - Selectbox for user input
#    - Success message

st.title("Hello Streamlit!")
st.subheader("This is my first interactive app")
st.text("Welcome to the world of Streamlit")
st.write("Let's make a simple app to choose your favorite chai.")

chai = st.selectbox("Your fav chai: ", ["Masala chai", "Lemon Tea", "Adrak Chai", "Kesar Chai"])
st.write(f"You choose {chai}. Excellent choice")

st.success("Your chai has been brewed")