import psycopg2
from datetime import datetime
import os

class SignalDatabase:
    def __init__(self):
        # Fetches the connection string from your .env file
        self.db_url = os.getenv("DATABASE_URL")
        self.conn = None
        self._connect()

    def _connect(self):
        try:
            self.conn = psycopg2.connect(self.db_url)
            self.create_table()
        except Exception as e:
            print(f"Database Connection Error: {e}")

    def create_table(self):
        """Initializes the signals table based on Architecture v2.0."""
        query = """
        CREATE TABLE IF NOT EXISTS signals (
            id SERIAL PRIMARY KEY,
            symbol VARCHAR(20),
            score INTEGER,
            direction VARCHAR(10),
            indicators TEXT,
            stop_loss FLOAT,
            target FLOAT,
            ai_explanation TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        with self.conn.cursor() as cur:
            cur.execute(query)
            self.conn.commit()

    def log_signal(self, symbol, score, direction, indicators, sl, tp, ai_insight):
        """Logs a high-confidence signal into the journal."""
        query = """
        INSERT INTO signals (symbol, score, direction, indicators, stop_loss, target, ai_explanation)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute(query, (symbol, score, direction, ",".join(indicators), sl, tp, ai_insight))
                self.conn.commit()
        except Exception as e:
            print(f"Error logging signal: {e}")