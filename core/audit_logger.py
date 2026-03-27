import sqlite3
import datetime

class AuditLogger:
    def __init__(self, db_path="workflow_audit.db"):
        self.conn = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS audit_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            request_id TEXT,
            stage TEXT,
            rule TEXT,
            status TEXT,
            message TEXT,
            timestamp TEXT
        )
        """)
        self.conn.commit()

    def log(self, request_id, stage, rule, status, message=""):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO audit_log (request_id, stage, rule, status, message, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (request_id, stage, rule, status, message, datetime.datetime.utcnow().isoformat()))
        self.conn.commit()

    def get_logs(self, request_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM audit_log WHERE request_id=?", (request_id,))
        return cursor.fetchall()
