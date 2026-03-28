
import sqlite3
import json
from datetime import datetime

DB_NAME = "metrics.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            cpu REAL,
            memory REAL,
            disk REAL,
            network REAL,
            docker TEXT,
            processes TEXT,
            alerts TEXT
        )
    """)

    conn.commit()
    conn.close()


def insert_metrics(data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO metrics (
            timestamp, cpu, memory, disk, network, docker, processes, alerts
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        datetime.now().isoformat(),
        data.get("cpu"),
        data.get("memory"),
        data.get("disk"),
        data.get("network"),
        json.dumps(data.get("docker")),
        json.dumps(data.get("processes")),
        json.dumps(data.get("alerts"))
    ))

    conn.commit()
    conn.close()
