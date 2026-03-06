import psycopg2
import time


# === CONFIGURATION ===
CSV_FILES = {
    'DimDate': 'clean_calendar.csv',
    'DimProduct': 'clean_products.csv',
    'DimStore': 'clean_stores.csv',
    'FactSales': 'clean_sales.csv'
}

DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'cityretail',
    'user': 'postgres',
    'password': 'itc6050_SK'
}

LOG_FILE = "load_errors.log"


# === CONNECT TO POSTGRES ===
try:
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    print(" Connected to PostgreSQL.")
except Exception as e:
    print(" Connection failed:", e)
    exit(1)


# === OPTIONAL: TRUNCATE TABLES FOR RERUNS ===
tables_order = ['FactSales', 'DimStore', 'DimProduct', 'DimDate']  # reverse order for truncation

print("\n Truncating tables...")
for table in tables_order:
    try:
        cur.execute(f"TRUNCATE TABLE {table} RESTART IDENTITY CASCADE;")
        print(f"  Truncated: {table}")
    except Exception as e:
        with open(LOG_FILE, "a") as log:
            log.write(f"[TRUNCATE ERROR] {table}: {str(e)}\n")
        print(f" Failed to truncate: {table}")

conn.commit()


# === LOAD CSVs TO TABLES ===
tables_order = ['DimDate', 'DimProduct', 'DimStore', 'FactSales']  # correct FK order

for table in tables_order:
    file_path = CSV_FILES[table]
    print(f"\n Loading {table} from {file_path}...")
    
    try:
        start = time.time()
        with open(file_path, 'r') as f:
            next(f)  # skip header
            cur.copy_expert(f"COPY {table} FROM STDIN WITH CSV", f)
        conn.commit()
        duration = time.time() - start
        print(f" Loaded {table} in {duration:.2f} seconds")
    
    except Exception as e:
        with open(LOG_FILE, "a") as log:
            log.write(f"[LOAD ERROR] {table}: {str(e)}\n")
        print(f" Failed to load {table}. Error logged.")


# === FINAL CHECK: Show table counts ===
print("\n Row counts after load:")
for table in tables_order:
    try:
        cur.execute(f"SELECT COUNT(*) FROM {table};")
        count = cur.fetchone()[0]
        print(f"{table}: {count} rows")
    except:
        print(f"{table}:  Error counting rows")

cur.close()
conn.close()
print("\n All done.")
