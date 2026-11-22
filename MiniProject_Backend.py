"""SQLite data-access layer for the movie catalogue desktop application."""

import os
import sqlite3
from contextlib import closing

DB_NAME = os.environ.get("MOVIE_DB_PATH", "movie1.db")
MOVIE_FIELDS = (
    "Movie_ID",
    "Movie_Name",
    "Release_Date",
    "Director",
    "Cast",
    "Budget",
    "Duration",
    "Rating",
)


def _connect():
    """Open a connection with consistent SQLite safety settings."""
    connection = sqlite3.connect(DB_NAME, timeout=10)
    connection.execute("PRAGMA foreign_keys = ON")
    connection.execute("PRAGMA busy_timeout = 10000")
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS book (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Movie_ID TEXT NOT NULL,
            Movie_Name TEXT,
            Release_Date TEXT,
            Director TEXT,
            Cast TEXT,
            Budget TEXT,
            Duration TEXT,
            Rating TEXT
        )
        """
    )
    return connection


def MovieData():
    """Initialize the local movie catalogue database."""
    with closing(_connect()) as connection:
        connection.commit()


def AddMovieRec(Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating):
    """Insert a movie record and return its generated database id."""
    values = (Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating)
    with closing(_connect()) as connection:
        cursor = connection.execute(
            """
            INSERT INTO book
                (Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            values,
        )
        connection.commit()
        return cursor.lastrowid


def ViewMovieData():
    """Return all movie records, ordered by their database id."""
    with closing(_connect()) as connection:
        return connection.execute("SELECT * FROM book ORDER BY id").fetchall()


def DeleteMovieRec(record_id):
    """Delete one movie by its database id; return whether a row was removed."""
    with closing(_connect()) as connection:
        cursor = connection.execute("DELETE FROM book WHERE id = ?", (record_id,))
        connection.commit()
        return cursor.rowcount > 0


def SearchMovieData(Movie_ID="", Movie_Name="", Release_Date="", Director="", Cast="", Budget="", Duration="", Rating=""):
    """Find records matching any non-empty supplied field."""
    values = (Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating)
    filters = [(field, value) for field, value in zip(MOVIE_FIELDS, values) if value != ""]
    if not filters:
        return ViewMovieData()

    where_clause = " OR ".join(f"{field} = ?" for field, _ in filters)
    parameters = tuple(value for _, value in filters)
    with closing(_connect()) as connection:
        return connection.execute(
            f"SELECT * FROM book WHERE {where_clause} ORDER BY id", parameters
        ).fetchall()


def UpdateMovieData(record_id, Movie_ID="", Movie_Name="", Release_Date="", Director="", Cast="", Budget="", Duration="", Rating=""):
    """Update all editable fields for a movie selected by its database id."""
    values = (Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating)
    assignments = ", ".join(f"{field} = ?" for field in MOVIE_FIELDS)
    with closing(_connect()) as connection:
        cursor = connection.execute(
            f"UPDATE book SET {assignments} WHERE id = ?",
            values + (record_id,),
        )
        connection.commit()
        return cursor.rowcount > 0
