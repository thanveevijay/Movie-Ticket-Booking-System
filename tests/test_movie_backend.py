"""Regression tests for the movie catalogue SQLite data layer."""

import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import MiniProject_Backend as backend


class MovieBackendTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = str(Path(self.temp_dir.name) / "test_movies.db")
        self.db_patch = patch.object(backend, "DB_NAME", self.db_path)
        self.db_patch.start()
        backend.MovieData()

    def tearDown(self):
        self.db_patch.stop()
        self.temp_dir.cleanup()

    def add_movie(self, movie_id="M001", name="Example Film"):
        return backend.AddMovieRec(
            movie_id, name, "2025-01-01", "Director", "Cast", "10",
            "2h", "4.5"
        )

    def test_add_and_list_movie(self):
        record_id = self.add_movie()
        rows = backend.ViewMovieData()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], record_id)
        self.assertEqual(rows[0][1:3], ("M001", "Example Film"))

    def test_search_ignores_empty_fields(self):
        self.add_movie()
        self.add_movie("M002", "Another Film")
        rows = backend.SearchMovieData(Movie_Name="Another Film")
        self.assertEqual([row[2] for row in rows], ["Another Film"])

    def test_empty_search_returns_all_records(self):
        self.add_movie()
        self.add_movie("M002", "Another Film")
        self.assertEqual(len(backend.SearchMovieData()), 2)

    def test_update_targets_the_selected_record(self):
        record_id = self.add_movie()
        updated = backend.UpdateMovieData(
            record_id, "M001", "Updated Film", "2025-01-01",
            "Director", "Cast", "10", "2h", "4.8"
        )
        self.assertTrue(updated)
        self.assertEqual(backend.ViewMovieData()[0][2], "Updated Film")

    def test_delete_returns_false_for_unknown_id(self):
        self.assertFalse(backend.DeleteMovieRec(9999))

    def test_delete_removes_existing_record(self):
        record_id = self.add_movie()
        self.assertTrue(backend.DeleteMovieRec(record_id))
        self.assertEqual(backend.ViewMovieData(), [])


if __name__ == "__main__":
    unittest.main()
