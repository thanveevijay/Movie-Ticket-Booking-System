# Movie Ticket Booking System

A Python desktop mini-project for managing movie records with a Tkinter interface and a SQLite data-access layer. The current backend supports adding, viewing, searching, updating, and deleting movie catalogue entries.

## Requirements

- Python 3.9+
- Tkinter (included with many standard Python distributions; Linux users may need their distribution's Tk package)
- No third-party package is required for the SQLite backend or its unit tests.
- pytest is optional if you prefer running the tests with pytest.

## Run the application

Clone the repository and run the frontend from the repository root:

```bash
python MiniProject_Frontend.py
```

The backend creates the SQLite database file `movie1.db` in the current working directory by default. To use a different database location, set `MOVIE_DB_PATH` before starting the application:

```bash
# macOS/Linux
MOVIE_DB_PATH=./data/movies.db python MiniProject_Frontend.py

# PowerShell
$env:MOVIE_DB_PATH = ".\data\movies.db"
python MiniProject_Frontend.py
```

Ensure the parent directory of a custom database path exists before launching the application.

## Run regression tests

The backend tests use a temporary SQLite database, so they do not modify your application database.

```bash
python -m unittest discover -s tests -v
```

Or, if pytest is installed:

```bash
python -m pytest -q
```

## Backend API

The data-access functions are implemented in `MiniProject_Backend.py`:

- `MovieData()` — initialize the database table.
- `AddMovieRec(...)` — insert a movie and return its generated record ID.
- `ViewMovieData()` — list records in insertion order.
- `SearchMovieData(...)` — search using any supplied non-empty fields.
- `UpdateMovieData(record_id, ...)` — update the selected record.
- `DeleteMovieRec(record_id)` — delete a record and return whether a row was removed.

Search values are passed as SQL parameters. The searchable field names are selected from a fixed internal list rather than taken from user input.

## Project scope

This is an academic DBMS mini-project and a local desktop catalogue. It does not currently implement live cinema listings, seat inventory, payment processing, or real ticket issuance.
