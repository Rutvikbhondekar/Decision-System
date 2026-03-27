import sqlite3
import datetime

class StateManager:
    def __init__(self, db_path="workflow_state.db"):
        self.conn = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS workflow_state (
            request_id TEXT PRIMARY KEY,
            workflow TEXT,
            status TEXT,
            updated_at TEXT
        )
        """)
        self.conn.commit()

    def save_state(self, request_id, workflow, status):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT OR REPLACE INTO workflow_state (request_id, workflow, status, updated_at)
        VALUES (?, ?, ?, ?)
        """, (request_id, workflow, status, datetime.datetime.utcnow().isoformat()))
        self.conn.commit()

    def get_state(self, request_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM workflow_state WHERE request_id=?", (request_id,))
        return cursor.fetchone()
