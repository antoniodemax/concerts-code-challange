# Concert Domain Management with Python

## Question Summary
This document outlines the implementation of a concert management system using Python and raw SQL queries. The system involves three main entities: Band, Venue, and Concert, with specific relationships and functionalities defined for each.

## Answer
In this project, we will create a concert management system that utilizes raw SQL queries to interact with a SQLite or PostgreSQL database. The schema consists of three tables: `bands`, `venues`, and `concerts`. The `concerts` table will establish relationships between bands and venues, including a date column for concert scheduling.

### Database Schema
1. **bands Table**:
   - `name`: String
   - `hometown`: String

2. **venues Table**:
   - `title`: String
   - `city`: String

3. **concerts Table**:
   - `band_id`: Foreign Key referencing `bands`
   - `venue_id`: Foreign Key referencing `venues`
   - `date`: String

### Key Methods
- **Concert Methods**:
  - `band()`: Returns the associated Band instance.
  - `venue()`: Returns the associated Venue instance.
  - `hometown_show()`: Checks if the concert is in the band's hometown.
  - `introduction()`: Generates a concert introduction string.

- **Venue Methods**:
  - `concerts()`: Retrieves all concerts at the venue.
  - `bands()`: Lists all bands that have performed at the venue.
  - `concert_on(date)`: Finds the first concert on a specified date.
  - `most_frequent_band()`: Identifies the band that has performed most frequently at the venue.

- **Band Methods**:
  - `concerts()`: Lists all concerts the band has played.
  - `venues()`: Lists all venues the band has performed at.
  - `play_in_venue(venue, date)`: Schedules a new concert.
  - `all_introductions()`: Returns all introductions for the band.
  - `most_performances()`: Identifies the band with the most concerts.

### Example Code Snippet
Here is a simple example of how to create the `bands` table using raw SQL in Python:

```python
import sqlite3

# Connect to the database
conn = sqlite3.connect('concerts.db')
cursor = conn.cursor()


# Commit changes and close the connection
conn.commit()
conn.close()
