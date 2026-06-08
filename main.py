from fastapi import FastAPI
import sqlite3

app = FastAPI()

DB_PATH = "data.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS visits (
            id INTEGER PRIMARY KEY AUTOINCREMENT
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.get("/")
def home():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("INSERT INTO visits DEFAULT VALUES")
    conn.commit()

    count = conn.execute("SELECT COUNT(*) FROM visits").fetchone()[0]
    conn.close()

    return {"visits": count}