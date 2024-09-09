import psycopg2





    ## Connection Details
hostname = 'localhost'
port=5433
username = 'postgres'
password = '12345678' # your password
database = 'books'

## Create/Connect to database
connection = psycopg2.connect(host=hostname,port=port,user=username, password=password, dbname=database)

## Create cursor, used to execute commands
cur = connection.cursor()

## Create quotes table if none exists
cur.execute("""
CREATE TABLE IF NOT EXISTS quotes(
    id serial PRIMARY KEY, 
    title text,
    category text,
    description VARCHAR(255)
)
""")

connection.commit()
cur.close()
connection.close()