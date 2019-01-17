'''
The database connection is set up here.
'''
import os
import psycopg2

# Connect to a test database and create a table to confirm connection
db_url = os.getenv("TEST_DATABASE_URL")

print(db_url)

con = psycopg2.connect("dbname='testdb' host='localhost' user='yunis' password='yunis' port='5432'")
print("succesfully connected")
cursor = con.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS meetup(
        id serial PRIMARY KEY NOT NULL,
        createdOn TIMESTAMP NOT NULL,
        topic VARCHAR(80) NOT NULL,
        location VARCHAR(55) NOT NULL,
        images VARCHAR(80),
        tags VARCHAR(80),
        happeningOn TIMESTAMP NOT NULL
    );''')
con.commit()
print("Successfully connected, no proceed with serious work!")