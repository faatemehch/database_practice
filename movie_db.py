import sqlite3

conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Movies (
        MovieID INTEGER PRIMARY KEY AUTOINCREMENT, 
        Title TEXT NOT NULL,
        ReleaseDate DATE,
        Studio VARCHAR (255)
    )
    """)

cursor.execute("""
    INSERT INTO Movies (MovieID, Title, ReleaseDate, Studio) VALUES
    (1, 'Titanic', 1997, '20th Century Fox, Paramount Pictures'),
    (2, '3 Idiots', 2009, 'Vinod Chopra Films'),
    (3, 'The Dark Knight', 2008, 'Warner Bros. Pictures, Legendary Pictures, Syncopy'),
    (4, 'Batman Begins', 2005, 'Warner Bros. Pictures, Legendary Pictures, Syncopy, DC Comics, Patalex III Productions');
        
""")

conn.commit()
conn.close()
