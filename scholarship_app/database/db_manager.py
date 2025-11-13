"""
Database Manager for Scholarship Application
Handles SQLite database connection and schema creation
"""

import sqlite3
import os
from datetime import datetime


class DatabaseManager:
    def __init__(self, db_name='scholarship.db'):
        """Initialize database connection"""
        self.db_path = os.path.join(os.path.dirname(__file__), db_name)
        self.conn = None
        self.cursor = None

    def connect(self):
        """Establish database connection"""
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row  # Access columns by name
        self.cursor = self.conn.cursor()

    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()

    def create_tables(self):
        """Create all required tables"""
        self.connect()

        # Scholarships table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS scholarships (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                amount REAL NOT NULL,
                deadline TEXT NOT NULL,
                eligibility_criteria TEXT,
                provider TEXT,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        ''')

        # Students table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT,
                address TEXT,
                gpa REAL,
                graduation_year INTEGER,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        ''')

        # Applications table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS applications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                scholarship_id INTEGER NOT NULL,
                application_date TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'pending',
                notes TEXT,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL,
                FOREIGN KEY (student_id) REFERENCES students (id) ON DELETE CASCADE,
                FOREIGN KEY (scholarship_id) REFERENCES scholarships (id) ON DELETE CASCADE,
                UNIQUE(student_id, scholarship_id)
            )
        ''')

        self.conn.commit()
        self.close()

    def execute_query(self, query, params=None):
        """Execute a query and return results"""
        self.connect()
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        results = self.cursor.fetchall()
        self.close()
        return results

    def execute_update(self, query, params=None):
        """Execute an update/insert/delete query"""
        self.connect()
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.conn.commit()
        last_id = self.cursor.lastrowid
        self.close()
        return last_id
