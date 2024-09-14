import sqlite3

# Creates the database and tables if they don't exist
def setup_database():
    connection = sqlite3.connect('concerts.db')
    cursor = connection.cursor()

    # Create bands table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bands (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            hometown TEXT NOT NULL
        )
    ''')

    # Create venues table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS venues (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            city TEXT NOT NULL
        )
    ''')

    # Create concerts table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS concerts (
            id INTEGER PRIMARY KEY,
            band_id INTEGER,
            venue_id INTEGER,
            date TEXT NOT NULL,
            FOREIGN KEY (band_id) REFERENCES bands (id),
            FOREIGN KEY (venue_id) REFERENCES venues (id)
        )
    ''')

    connection.commit()
    connection.close()

class Band:
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown
        self.id = None  # Will be set when the band is inserted into the database

    def save(self):
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO bands (name, hometown) VALUES (?, ?)
        ''', (self.name, self.hometown))
        self.id = cursor.lastrowid
        connection.commit()
        connection.close()

    def play_in_venue(self, venue, date):
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()

        # Get the venue ID
        cursor.execute('SELECT id FROM venues WHERE title = ? AND city = ?', (venue.title, venue.city))
        venue_row = cursor.fetchone()
        if venue_row:
            venue_id = venue_row[0]
        else:
            cursor.execute('INSERT INTO venues (title, city) VALUES (?, ?)', (venue.title, venue.city))
            venue_id = cursor.lastrowid

        cursor.execute('INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?)', 
                       (self.id, venue_id, date))
        connection.commit()
        connection.close()

class Venue:
    def __init__(self, title, city):
        self.title = title
        self.city = city

def fetch_band_by_concert(concert_id, db_cursor):
    db_cursor.execute('''
    SELECT bands.*
    FROM concerts
    INNER JOIN bands ON concerts.band_id = bands.id
    WHERE concerts.id = ?
    ''', (concert_id,))
    return db_cursor.fetchone()

def fetch_concerts(venue_id, db_cursor):
    db_cursor.execute('''
    SELECT concerts.*
    FROM concerts
    WHERE venue_id = ?
    ''', (venue_id,))
    return db_cursor.fetchall()

def get_bands_per_venue(venue_id, db_cursor):
    db_cursor.execute('''
    SELECT DISTINCT bands.*
    FROM bands
    INNER JOIN concerts ON bands.id = concerts.band_id
    WHERE concerts.venue_id = ?
    ''', (venue_id,))
    return db_cursor.fetchall()

def execute_main():
    # Connect to the SQLite database
    connection = sqlite3.connect('concerts.db')
    cursor = connection.cursor()

    # Create a band and save it
    my_band = Band("The Rockers", "New York")
    my_band.save()

    # Create venues
    venue1 = Venue("Madison Square Garden", "New York")
    venue2 = Venue("Mombasa", "Kenya")
    venue3 = Venue("Kisumu", "Kenya")

    # Band plays in venues
    my_band.play_in_venue(venue1, "2022-01-01")
    my_band.play_in_venue(venue2, "2022-01-02")
    my_band.play_in_venue(venue3, "2022-01-03")

    # Fetch and display data
    print("Bands performing at the venue:")
    bands = get_bands_per_venue(1, cursor)
    for band in bands:
        print(band)

    print("\nConcerts at the venue:")
    concerts = fetch_concerts(1, cursor)
    for concert in concerts:
        print(concert)

    print("\nBand for the concert:")
    band = fetch_band_by_concert(1, cursor)
    print(band)

    # Close the connection
    connection.close()

# Run the main function
if __name__ == "__main__":
    setup_database()
    execute_main()
