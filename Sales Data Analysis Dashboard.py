import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('train.csv')
print("--- First 5 Rows Of The Dataset (Head) ---")
print(df.head())
print("\n--- Dataset Information (Info) ---")
print(df.info())
print("\n--- Dataset Shape (Rows, Columns) ---")
print(df.shape)
print("\n--- Missing Values Count ---")
print(df.isnull().sum())
print("\n--- Duplicated Rows Count ---")
print(df.duplicated().sum())
df['Order Date'] = pd.to_datetime(df['Order Date'] , format = '%d/%m/%Y' , errors= 'coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d/%m/%Y', errors='coerce')
print("\n--- Data Tybes After Conversion ---")
print(df[['Order Date','Ship Date']].dtypes)
category_sales = df.groupby('Category')['Sales'].sum().reset_index() # بتجمعلك المنتجات حسب الفئه بعدين بعدين بتجمع اجمالي المبيعات لكل فئه لحال
category_sales = category_sales.sort_values(by='Sales', ascending=False) # بترتب الناتج تنازليا من الفئه الاكبر في المبيعات الى الفئه الاقل
print("\n--- Total Sales by Product Category ---")
print(category_sales)
sns.set_theme(style='whitegrid') # هيك انا اعطيت خلفيه لونها ابيض
plt.figure(figsize=(6,3)) # حددت ابعادها
sns.barplot(x='Category',y='Sales',data=category_sales ,palette='viridis')
plt.title('Total Sales by Product Category', fontsize=14, fontweight='bold')
plt.xlabel('Product Category', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
df['Year'] = df['Order Date'].dt.year
yearly_sales = df.groupby('Year')['Sales'].sum().reset_index()
print("\n--- Total Sales by Year ---")
print(yearly_sales)
plt.figure(figsize=(6, 3))
sns.lineplot( x='Year', y='Sales',data=yearly_sales,marker='o', color='b',linewidth=2.5,)
plt.title('Total Sales Trend Over Years', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.grid(True)
top_cities = (df.groupby('City')['Sales'].sum().reset_index().nlargest(10, 'Sales'))
print('\n--- Top 10 Cities by Sales ---')
print(top_cities)
plt.figure(figsize=(8, 5))
sns.barplot(x='City', y='Sales', data=top_cities, palette='magma')
plt.title('Top 10 Cities by Total Sales', fontsize=14, fontweight='bold')
plt.xlabel('City', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
