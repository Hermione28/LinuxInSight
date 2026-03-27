import sqlite3

def init_db():
    conn = sqlite3.connect("metrics.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS metrics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp REAL,
        cpu REAL,
        memory REAL
    )
    """)

    conn.commit()
    conn.close()