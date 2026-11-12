import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
st.set_page_config(page_title="Sales Data Analysis Dashboard", page_icon="📊", layout="wide")
st.title("📊 Sales Data Analysis & Business Intelligence Dashboard")
st.markdown("Welcome to your interactive e-commerce sales dashboard! Explore trends,"" categories, and top cities.")
@st.cache_data
def load_data():
  df = pd.read_csv("train.csv")
  df["Order Date"] = pd.to_datetime(df["Order Date"], format="%d/%m/%Y", errors="coerce")
  df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="%d/%m/%Y", errors="coerce")
  df["Year"] = df["Order Date"].dt.year
  return df
df = load_data()
st.sidebar.header("🔍 Filter Data")
selected_category = st.sidebar.selectbox("Select Product Category:", ["All"] + list(df["Category"].unique()))
if selected_category != "All":
  df_filtered = df[df["Category"] == selected_category]
else:df_filtered = df
total_sales = df_filtered["Sales"].sum()
total_orders = df_filtered.shape[0]
col1, col2 = st.columns(2)
col1.metric(label="💰 Total Sales", value=f"${total_sales:,.2f}")
col2.metric(label="📦 Total Orders", value=f"{total_orders:,}")
st.markdown("---")
st.subheader("📈 Visual Data Analysis")
col_a, col_b = st.columns(2)
with col_a:
  st.write("### Total Sales by Product Category")
  cat_sales = df_filtered.groupby("Category")["Sales"].sum().reset_index()
  fig, ax = plt.subplots(figsize=(6, 4))
  sns.barplot(x="Category",y="Sales",data=cat_sales,palette="viridis",ax=ax,hue="Category",legend=False,)
  plt.xticks(rotation=15)
  st.pyplot(fig)
with col_b:
  st.write("### Top 5 Cities by Sales")
  top_cities = (df_filtered.groupby("City")["Sales"].sum().reset_index().nlargest(5, "Sales"))
  fig, ax = plt.subplots(figsize=(6, 4))
  sns.barplot(x="City",y="Sales",data=top_cities,palette="magma",ax=ax,hue="City",legend=False,)
  plt.xticks(rotation=30)
  st.pyplot(fig)
st.subheader("📅 Yearly Sales Trend")
yearly_sales = df.groupby("Year")["Sales"].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 4))
sns.lineplot(x="Year",y="Sales",data=yearly_sales,marker="o",color="b",linewidth=2.5,ax=ax,)
plt.title("Sales Performance Over Years", fontsize=12, fontweight="bold")
plt.xlabel("Year", fontsize=10)
plt.ylabel("Total Sales ($)", fontsize=10)
plt.grid(True)
st.pyplot(fig)
st.markdown("---")
st.subheader("📌 Key Business Insights")
st.markdown("""
- **Technology Category** consistently generates the highest revenue, pointing to a strong consumer demand for electronics.
- **Top Cities** account for a major share of the total sales volume, highlighting key hubs for targeted regional marketing and shipping optimization.
- **Yearly Trends** show fluctuations that help management identify peak seasons for promotional campaigns.
""")