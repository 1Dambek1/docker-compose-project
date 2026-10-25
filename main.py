import psycopg2


conn = psycopg2.connect(
 host= "localhost",
 port=5432,
 user= 'postgres',
 password = "12345",
 dbname = 'mydb'
)


cur = conn.cursor()

cur.execute("SELECT version()")
print(cur.fetchone())
