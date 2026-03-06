import psycopg2

# === Connect to PostgreSQL ===
conn = psycopg2.connect(
    host='localhost',
    port=5432,
    database='cityretail',
    user='postgres',
    password='itc6050_SK'
)
cur = conn.cursor()


# === CREATE VIEWS ===
print("\n Creating views...")

views_sql = [

    # View 1: Sales by Region
    """
    CREATE OR REPLACE VIEW v_sales_by_region AS
    SELECT 
        ds.Region,
        SUM(fs.Revenue) AS total_revenue,
        SUM(fs.QtySold) AS total_quantity
    FROM FactSales fs
    JOIN DimStore ds ON fs.StoreID = ds.StoreID
    GROUP BY ds.Region;
    """,

    # View 2: Profit Margin by Product
    """
    CREATE OR REPLACE VIEW v_product_profit_margin AS
    SELECT 
        dp.ProductID,
        dp.ProductName,
        dp.Category,
        SUM(fs.Revenue) AS total_revenue,
        SUM(fs.QtySold) AS total_quantity,
        SUM(fs.QtySold * dp.CostPrice) AS total_cost,
        SUM(fs.Revenue - fs.QtySold * dp.CostPrice) AS total_profit,
        ROUND(SUM(fs.Revenue - fs.QtySold * dp.CostPrice) / NULLIF(SUM(fs.Revenue), 0), 2) AS profit_margin
    FROM FactSales fs
    JOIN DimProduct dp ON fs.ProductID = dp.ProductID
    GROUP BY dp.ProductID, dp.ProductName, dp.Category;
    """,

    # View 3: Average Sale Value by Store
    """
    CREATE OR REPLACE VIEW v_avg_sale_by_store AS
    SELECT 
        ds.StoreName,
        ds.Region,
        SUM(fs.Revenue) AS total_revenue,
        SUM(fs.QtySold) AS total_quantity,
        ROUND(SUM(fs.Revenue) / NULLIF(SUM(fs.QtySold), 0), 2) AS avg_sale_value
    FROM FactSales fs
    JOIN DimStore ds ON fs.StoreID = ds.StoreID
    GROUP BY ds.StoreName, ds.Region;
    """
]

for view_sql in views_sql:
    try:
        cur.execute(view_sql)
        conn.commit()
        print(" View created.")
    except Exception as e:
        print(f" View creation failed: {str(e)}")


# === CREATE INDEXES ===
print("\n Creating indexes...")

index_statements = [
    "CREATE INDEX IF NOT EXISTS idx_factsales_dateid ON FactSales(DateID);",
    "CREATE INDEX IF NOT EXISTS idx_factsales_productid ON FactSales(ProductID);",
    "CREATE INDEX IF NOT EXISTS idx_factsales_storeid ON FactSales(StoreID);",
    "CREATE INDEX IF NOT EXISTS idx_dimstore_region ON DimStore(Region);",
    "CREATE INDEX IF NOT EXISTS idx_dimproduct_category ON DimProduct(Category);"
]

for stmt in index_statements:
    try:
        cur.execute(stmt)
        conn.commit()
        print(f" Index created: {stmt.split()[4]}")
    except Exception as e:
        print(f" Index creation failed: {str(e)}")

# === Done ===
cur.close()
conn.close()
print("\n Views and indexes created successfully.")




