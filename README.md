# 📊 Sales Data Analysis & Business Intelligence Dashboard

An interactive e-commerce sales analysis project built with **Python**. It includes an exploratory analysis script and a **Streamlit** dashboard to explore sales by category, city, and year.

---

## ✨ Features

- 🔍 Filter data by product category (Furniture, Office Supplies, Technology).
- 💰 Key metrics: total sales and total number of orders.
- 📈 Total sales by product category.
- 🏙️ Top 5 cities by sales.
- 📅 Yearly sales trend.
- 📌 Key business insights summary.

---

## 📁 Project Structure

```
├── app.py                           # Streamlit dashboard
├── Sales_Data_Analysis_Dashboard.py # Exploratory data analysis script (EDA)
├── train.csv                        # Dataset
├── requirements.txt                 # Project dependencies
└── README.md
```

---

## 🗂️ Dataset

`train.csv` contains ~9,800 retail orders with the following columns:

| Column | Description |
|---|---|
| Row ID | Row number |
| Order ID | Order identifier |
| Order Date / Ship Date | Order and shipping dates (`dd/mm/yyyy`) |
| Ship Mode | Shipping method |
| Customer ID / Customer Name | Customer information |
| Segment | Customer segment (Consumer, Corporate, Home Office) |
| Country / City / State / Postal Code / Region | Location details |
| Product ID / Category / Sub-Category / Product Name | Product details |
| Sales | Sales amount ($) |

---

## 🛠️ Technologies

- Python 3
- Pandas & NumPy
- Matplotlib & Seaborn
- Streamlit

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit dashboard

```bash
streamlit run app.py
```

Then open the link shown in your terminal (usually `http://localhost:8501`).

### 4. Run the analysis script (optional)

```bash
python Sales_Data_Analysis_Dashboard.py
```

This prints a data overview (head, info, shape, missing values, duplicates) and generates the charts.

---

## 🔎 Analysis Steps

1. Load the data and inspect it (shape, missing values, duplicates).
2. Convert `Order Date` and `Ship Date` to datetime.
3. Calculate total sales by category.
4. Extract the year and analyze the yearly sales trend.
5. Find the top cities by sales.
6. Present everything in an interactive dashboard.

---

## 💡 Key Insights

- **Technology** is among the top revenue-generating categories.
- A few **top cities** account for a major share of total sales, useful for targeted regional marketing.
- **Yearly trends** help identify peak seasons for promotional campaigns.

---
