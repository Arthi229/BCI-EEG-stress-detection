import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("eeg_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT,
            patient_id TEXT,
            alpha REAL,
            beta REAL,
            gamma REAL,
            alpha_pct REAL,
            beta_pct REAL,
            gamma_pct REAL,
            prediction TEXT,
            confidence REAL,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()


def insert_record(data):
    conn = sqlite3.connect("eeg_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO records (
            patient_name, patient_id,
            alpha, beta, gamma,
            alpha_pct, beta_pct, gamma_pct,
            prediction, confidence, timestamp
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, data)

    conn.commit()
    conn.close()


def fetch_records():
    conn = sqlite3.connect("eeg_records.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM records ORDER BY id DESC")
    rows = cursor.fetchall()

    conn.close()
    return rows