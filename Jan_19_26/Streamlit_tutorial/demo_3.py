import streamlit as st

# Streamlit App demonstrating various widgets and layout options:
#    - Columns
#    - Sidebar
#    - Expander

# Page title
st.title("Programming Language Poll")

# Create two columns
col1, col2 = st.columns(2)

with col1:
    st.header("Python")
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg",
        width=180
    )
    vote_python = st.button("Vote Python")

with col2:
    st.header("Java")
    st.image(
        "https://upload.wikimedia.org/wikipedia/en/3/30/Java_programming_language_logo.svg",
        width=180
    )
    vote_java = st.button("Vote Java")

# Button click handling
if vote_python:
    st.success("Thanks for voting Python")
elif vote_java:
    st.success("Thanks for voting Java")

# Sidebar inputs
st.sidebar.header("User Details")

name = st.sidebar.text_input("Enter your name")
language = st.sidebar.selectbox(
    "Select your favorite programming language",
    ["Python", "Java", "C++", "JavaScript", "Go"]
)

experience = st.sidebar.slider(
    "Years of programming experience",
    min_value=0,
    max_value=10,
    value=1
)

# Display user selection
st.write(f"Welcome {name}")
st.write(f"Preferred language: {language}")
st.write(f"Experience: {experience} years")

# Expander section
with st.expander("Why learn programming?"):
    st.write("""
    1. Programming helps automate tasks
    2. It improves logical thinking
    3. It enables software and application development
    4. It is essential for modern technology careers
    """)

# Markdown examples
st.markdown("# Learning Programming")
st.markdown("## Practice consistently")
st.markdown("> Code is read more often than it is written")
st.markdown("Consistency is the key to mastering programming.")
