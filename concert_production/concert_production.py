import sqlite3

# Connecting to the database
conn = sqlite3.connect('concerts.db')
cursor = conn.cursor()

# Define the ID of the concert for which details are to be fetched
concert_id = 1

# Query to retrieve the band info for that particular concert
cursor.execute('''
SELECT bands.*
FROM concerts
JOIN bands ON concerts.band_id = bands.id
WHERE concerts.id = ?
''', (concert_id,))

# Fetching the result
band = cursor.fetchone()
if band:
    print(f'Ensemble: {band}')
else:
    print('No band found for the concert.')

# Query to retrieve the venue information for that particular concert
cursor.execute('''
SELECT venues.*
FROM concerts
JOIN venues ON concerts.venue_id = venues.id
WHERE concerts.id = ?
''', (concert_id,))

# Fetching the result
venue = cursor.fetchone()
if venue:
    print(f'Location: {venue}')
else:
    print('No venue found for the concert.')

# Closing the connection
conn.close()
