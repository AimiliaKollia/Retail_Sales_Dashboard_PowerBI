import psycopg2


# Connect to your PostgreSQL Docker container
conn = psycopg2.connect(
    host='localhost',
    port=5432,
    database='cityretail',
    user='postgres',
    password='itc6050_SK'  
)
cur = conn.cursor()

# Read SQL file
with open("star_schema.sql", "r") as f:
    sql = f.read()

# Execute SQL commands
cur.execute(sql)
conn.commit()

print(" Tables created successfully!")

cur.close()
conn.close()
