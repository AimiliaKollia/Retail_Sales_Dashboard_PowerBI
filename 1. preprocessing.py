# === Import Libraries ===
import pandas as pd


# === Load & Inspect Datasets ===

# Calendar
print("\n" + "="*20 + " Calendar " + "="*20)
calendar_df = pd.read_csv('calendar.csv')
print(calendar_df.info())
print(calendar_df.head())
print("Missing values:\n", calendar_df.isnull().sum())

# Cities Lookup
print("\n" + "="*20 + " Cities " + "="*20)
cities_df = pd.read_csv('cities_lookup.csv')
print(cities_df.info())
print(cities_df.head())
print("Missing values:\n", cities_df.isnull().sum())

# Products
print("\n" + "="*20 + " Products " + "="*20)
products_df = pd.read_csv('products.csv')
print(products_df.info())
print(products_df.head())
print("Missing values:\n", products_df.isnull().sum())

# Sales
print("\n" + "="*20 + " Sales " + "="*20)
sales_df = pd.read_csv('sales.csv')
print(sales_df.info())
print(sales_df.head())
print("Missing values:\n", sales_df.isnull().sum())

# Stores
print("\n" + "="*20 + " Stores " + "="*20)
stores_df = pd.read_csv('stores.csv')
print(stores_df.info())
print(stores_df.head())
print("Missing values:\n", stores_df.isnull().sum())

# === Cleaning Steps ===

# Convert calendar Date column to datetime
print("\n Converting 'Date' in calendar_df to datetime...")
calendar_df['Date'] = pd.to_datetime(calendar_df['Date'], errors='coerce')

# Standardize city names in stores_df
print(" Standardizing city names in stores_df...")
city_map = dict(zip(cities_df['RawCity'], cities_df['StandardCity']))
stores_df['City'] = stores_df['City'].replace(city_map)

# === Duplicate Check Summary ===
print("\n Duplicate Rows Summary:")
print("Calendar:", calendar_df.duplicated().sum())
print("Cities:", cities_df.duplicated().sum())
print("Products:", products_df.duplicated().sum())
print("Sales:", sales_df.duplicated().sum())
print("Stores:", stores_df.duplicated().sum())

# === Reorder columns for PostgreSQL compatibility ===
calendar_df = calendar_df[['DateID', 'Date', 'Year', 'Quarter', 'Month', 'Day', 'Weekday']]
products_df = products_df[['ProductID', 'ProductName', 'Category', 'Subcategory', 'CostPrice', 'SalePrice']]
stores_df   = stores_df[['StoreID', 'StoreName', 'City', 'Region']]
sales_df    = sales_df[['SalesID', 'DateID', 'ProductID', 'StoreID', 'QtySold', 'Revenue']]

# === Export cleaned and ordered data ===
calendar_df.to_csv('clean_calendar.csv', index=False)
products_df.to_csv('clean_products.csv', index=False)
stores_df.to_csv('clean_stores.csv', index=False)
sales_df.to_csv('clean_sales.csv', index=False)

print(" All cleaned CSV files exported in correct column order.")


