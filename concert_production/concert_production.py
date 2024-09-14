import sqlite3

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

# Connecting to the database
conn = sqlite3.connect('concerts.db')
cursor = conn.cursor()

# # Define the ID of the concert for which details are to be fetched
# concert_id = 1

# # Query to retrieve the band info for that particular concert
# cursor.execute('''
# SELECT bands.*
# FROM concerts
# JOIN bands ON concerts.band_id = bands.id
# WHERE concerts.id = ?
# ''', (concert_id,))

# # Fetching the result
# band = cursor.fetchone()
# if band:
#     print(f'Ensemble: {band}')
# else:
#     print('No band found for the concert.')

# # Query to retrieve the venue information for that particular concert
# cursor.execute('''
# SELECT venues.*
# FROM concerts
# JOIN venues ON concerts.venue_id = venues.id
# WHERE concerts.id = ?
# ''', (concert_id,))

# # Fetching the result
# venue = cursor.fetchone()
# if venue:
#     print(f'Location: {venue}')
# else:
#     print('No venue found for the concert.')
# Create the concerts table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS concerts (
        id INTEGER PRIMARY KEY,
        name TEXT,
        venue TEXT
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
