import sqlite3

class Venue:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def concert_on(self, date):
        query = "SELECT * FROM concerts WHERE date = ? ORDER BY time LIMIT 1"
        self.cursor.execute(query, (date,))
        return self.cursor.fetchone()

    def most_frequent_band(self):
        query = """
        SELECT band_name, COUNT(*) as performance_count 
        FROM concerts 
        GROUP BY band_name 
        ORDER BY performance_count DESC 
        LIMIT 1
        """
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def close(self):
        self.connection.close()


class Concert:
    def __init__(self, name, venue):
        self.name = name
        self.venue = venue


class Band:
    def __init__(self, name):
        self.name = name
        self.concerts_list = []

    def add_concert(self, concert):
        self.concerts_list.append(concert)

    def concerts(self):
        return [concert.name for concert in self.concerts_list]

    def venues(self):
        return list(set(concert.venue for concert in self.concerts_list))


# Connect to the database
conn = sqlite3.connect('concerts.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS concerts')

# Create the concerts table with the correct schema
cursor.execute('''
    CREATE TABLE concerts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        venue TEXT NOT NULL
    )
''')

# Create a band and add concerts
band = Band("The Rockers")
band.add_concert(Concert("Jazz session", "Nairobi"))
band.add_concert(Concert("Winter Jam", "Mombasa"))
band.add_concert(Concert("Ladies Night", "Kisumu"))

# Insert concert data into the database
for concert in band.concerts_list:
    cursor.execute("INSERT INTO concerts (name, venue) VALUES (?, ?)",
                   (concert.name, concert.venue))

# Commit the changes
conn.commit()

# Closing the connection
conn.close()
