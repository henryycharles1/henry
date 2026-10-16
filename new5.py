import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt


df = pd.read_csv("chocolate_sales.csv")

st.title("Sample Dashboard")
st.markdown("### This is a practice dashboard we are building with streamlit")

# for kpis

kpi1, kpi2, kpi3 = st.columns(3)

with kpi1:
    st.metric(label="Total Boxes Shipped", value=df["Boxes Shipped"].sum())

with kpi2:
    st.metric(label="Total Revenue Generated", value=df["Amount"].sum())

with kpi3:
    st.metric(label="Most Purchased Product", value=df["Product"].mode()[0])

# for charts

chart1, chart2 = st.columns(2)

with chart1:
    product_revenue = df.groupby("Product")["Amount"].sum()

    fig, ax = plt.subplots()
    product_revenue.plot(kind="bar", color="red", ax=ax)
    plt.ylabel("Total Revenue")
    plt.title = ("Total Revenue Per Product")
    st.pyplot(fig=fig)

with chart2:
    total_per_person = df.groupby("Sales Person")["Amount"].sum()

    fig, ax = plt.subplots()
    total_per_person.plot(kind="line", color="blue")
    plt.title = ("Total Revenue Per Person")
    plt.ylabel("Total Revenue")
    plt.xticks(rotation=45)
    st.pyplot(fig=fig)

chart3, chart4 = st.columns(2)

with chart3:
    country_income = df.groupby("Country")["Amount"].sum()

    fig, ax = plt.subplots()
    country_income.plot.pie()
    plt.title = ("Total Revenue Per Country")
    st.pyplot(fig=fig)

with chart4:
    boxes_shipped_revenue = df.groupby("Country")["Amount"].sum()

    fig, ax = plt.subplots()
    boxes_shipped_revenue.plot(kind="bar", color="red")
    plt.figure(figsize=(12, 6))
    plt.title = ("Revenue Per Country")
    st.pyplot(fig=fig)



st.write("Sample Dataframe")
st.dataframe(df.head(20))

# do 4 more
