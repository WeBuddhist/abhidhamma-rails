"""
connect_db.py
-------------
Singleton connection manager for dpd.db.
The connection is created lazily on first call to get_connection().
"""

import sqlite3


class DBConnection:
    """
    Singleton SQLite connection manager.

    Usage:
        conn = DBConnection.get_connection()  # creates if not exists
        conn = DBConnection.get_connection()  # returns same instance
        DBConnection.close()
    """

    DB_PATH = "pali-english/db_query/dpd.db/dpd.db"

    _instance: sqlite3.Connection | None = None

    @classmethod
    def get_connection(cls) -> sqlite3.Connection:
        """
        Returns the existing connection, or creates a new one if null.
        Always call this — no need to manually instantiate the class.
        """
        if cls._instance is None:
            cls._instance = sqlite3.connect(cls.DB_PATH)
            cls._instance.row_factory = sqlite3.Row
            print(f"Connected to {cls.DB_PATH}")
        return cls._instance

    @classmethod
    def close(cls):
        """Closes the connection and resets the singleton."""
        if cls._instance is not None:
            cls._instance.close()
            print(f"Connection to {cls.DB_PATH} closed.")
            cls._instance = None