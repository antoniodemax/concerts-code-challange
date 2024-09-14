import sqlite3

# fetch a band by concert ID
def fetch_band_by_concert(concert_id, db_cursor):
    db_cursor.execute('''
    SELECT bands.*
    FROM concerts
    INNER JOIN bands ON concerts.band_id = bands.id
    WHERE concerts.id = ?
    ''', (concert_id,))
    return db_cursor.fetchone()

# fetch concerts by venue ID
def fetch_concerts(venue_id, db_cursor):
    db_cursor.execute('''
    SELECT concerts.*
    FROM concerts
    WHERE venue_id = ?
    ''', (venue_id,))
    return db_cursor.fetchall()

# Function to get distinct bands performing at a venue
def get_bands_per_venue(venue_id, db_cursor):
    db_cursor.execute('''
    SELECT DISTINCT bands.*
    FROM bands
    INNER JOIN concerts ON bands.id = concerts.band_id
    WHERE concerts.venue_id = ?
    ''', (venue_id,))
    return db_cursor.fetchall()

# Main execution block
def execute_main():
    # Connect to the SQLite database
    connection = sqlite3.connect('concerts.db')
    cursor = connection.cursor()

    # Example usage
    venue_id = 1  
    concert_id = 1  

    print("Bands performing at the venue:")
    bands = get_bands_per_venue(venue_id, cursor)
    for band in bands:
        print(band)

    print("\nConcerts at the venue:")
    concerts = fetch_concerts(venue_id, cursor)
    for concert in concerts:
        print(concert)

    print("\nBand for the concert:")
    band = fetch_band_by_concert(concert_id, cursor)
    print(band)

    # Close the connection
    connection.close()

# Run the main function
if __name__ == "__main__":
    execute_main()
