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
