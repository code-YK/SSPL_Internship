import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Car Sales Dashboard")

# File upload
file = st.file_uploader("Upload your CSV file", type=["csv"])

if file:
    df = pd.read_csv(file)

    # Data preview
    st.subheader("Data Preview")
    st.dataframe(df)

    # Summary statistics
    st.subheader("Summary Statistics")
    st.write(df.describe())

    # City filter
    cities = df["City"].unique()
    selected_city = st.selectbox("Filter by City", cities)

    filtered_data = df[df["City"] == selected_city]
    st.subheader("Filtered Data")
    st.dataframe(filtered_data)

    # Graph selection
    st.subheader("Sales Visualization")

    chart_type = st.radio(
        "Choose chart type",
        ["Bar Chart", "Pie Chart"]
    )

    # Prepare data for plotting
    sales_by_brand = (
        filtered_data
        .groupby("Brand")["Units_Sold"]
        .sum()
    )

    # Plot graph
    fig, ax = plt.subplots()

    if chart_type == "Bar Chart":
        sales_by_brand.plot(kind="bar", ax=ax)
        ax.set_ylabel("Units Sold")
        ax.set_title(f"Units Sold by Brand in {selected_city}")

    elif chart_type == "Pie Chart":
        sales_by_brand.plot(kind="pie", autopct="%1.1f%%", ax=ax)
        ax.set_ylabel("")
        ax.set_title(f"Market Share by Brand in {selected_city}")

    st.pyplot(fig)
else:
    st.info("Please upload a CSV file to get started.")