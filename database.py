import sqlite3

DB_NAME = "metrics.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cpu REAL,
            memory REAL,
            disk REAL,
            network REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


# 🔥 Insert ALL metrics (including network)
def insert_metrics(cpu, memory, disk, network):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
        INSERT INTO metrics (cpu, memory, disk, network)
        VALUES (?, ?, ?, ?)
    """, (cpu, memory, disk, network))

    conn.commit()
    conn.close()


# 🔥 Get history (including network)
def get_last_metrics(limit=20):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
        SELECT cpu, memory, disk, network, timestamp
        FROM metrics
        ORDER BY timestamp DESC
        LIMIT ?
    """, (limit,))

    rows = c.fetchall()
    conn.close()

    data = []
    for row in rows:
        data.append({
            "cpu": row[0],
            "memory": row[1],
            "disk": row[2],
            "network": row[3],
            "timestamp": row[4]
        })

    return data[::-1]
