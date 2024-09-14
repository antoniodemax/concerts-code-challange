import sqlite3

#connecting the database
conn = sqlite3.connect('concerts.db')
cursor = conn,cursor()

#Bands table
cursor.execute('''
CREATE TABLE IF NOT EXISTS bands (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    hometown TEXT NOT NULL
)
''')

#venues table
cursor.execute('''
CREATE TABLE IF NOT EXISTS venues (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    city TEXT NOT NULL
)
''')

#concerts table
cursor.execute('''
CREATE TABLE IF NOT EXISTS venues (
    id INTEGER PRIMARY KEY,
    band_id INTEGER,
    venue_id INTEGER,
    date TEXT NOT NULL,
    FOREIGN KEY (band_id) REFERENCES bands (id),
    FOREIGN KEY (venue_id) REFERENCES venues (id)
)
''')

#insert data into concerts table
cursor.execute('''
INSERT INTO concerts (band_id, venue_id, concert_date) 
VALUES (1, 1, '2023-10-15')
''')

#commiting the changes and closing the connection
conn.commit()
conn.close()