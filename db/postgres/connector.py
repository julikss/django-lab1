import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect("dbname=decanatdb user=postgres password=password")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM decanat1")

# Retrieve query results
records = cur.fetchall()

print(records)