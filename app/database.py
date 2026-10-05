import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).resolve().parent.parent / "data" / "paradise.db"


def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DB_PATH)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id TEXT NOT NULL,
            role TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()

    return connection


def save_message(customer_id, role, message):
    connection = get_connection()

    connection.execute(
        """
        INSERT INTO messages (customer_id, role, message)
        VALUES (?, ?, ?)
        """,
        (customer_id, role, message)
    )

    connection.commit()
    connection.close()


def get_history(customer_id):
    connection = get_connection()

    rows = connection.execute(
        """
        SELECT role, message
        FROM messages
        WHERE customer_id = ?
        ORDER BY id ASC
        """,
        (customer_id,)
    ).fetchall()

    connection.close()

    return rows