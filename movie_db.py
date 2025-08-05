import sqlite3

conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Movies (
        MovieID INTEGER PRIMARY KEY AUTOINCREMENT, 
        Title TEXT NOT NULL,
        ReleaseDate DATE,
        DirectorID INTEGER
    )
    """)



conn.commit()
conn.close()
