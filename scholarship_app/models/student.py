"""
Student Model
Handles all student/applicant-related database operations
"""

from datetime import datetime
from ..database import DatabaseManager


class Student:
    def __init__(self, student_id=None, first_name=None, last_name=None,
                 email=None, phone=None, address=None, gpa=None, graduation_year=None):
        self.id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address
        self.gpa = gpa
        self.graduation_year = graduation_year
        self.db = DatabaseManager()

    @staticmethod
    def create(first_name, last_name, email, phone=None, address=None,
               gpa=None, graduation_year=None):
        """Create a new student"""
        db = DatabaseManager()
        now = datetime.now().isoformat()

        query = '''
            INSERT INTO students
            (first_name, last_name, email, phone, address, gpa, graduation_year, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        params = (first_name, last_name, email, phone, address, gpa, graduation_year, now, now)

        try:
            student_id = db.execute_update(query, params)
            return student_id
        except Exception as e:
            print(f"Error creating student: {e}")
            return None

    @staticmethod
    def get_all():
        """Get all students"""
        db = DatabaseManager()
        query = 'SELECT * FROM students ORDER BY last_name, first_name'
        results = db.execute_query(query)
        return [dict(row) for row in results]

    @staticmethod
    def get_by_id(student_id):
        """Get student by ID"""
        db = DatabaseManager()
        query = 'SELECT * FROM students WHERE id = ?'
        results = db.execute_query(query, (student_id,))
        if results:
            return dict(results[0])
        return None

    @staticmethod
    def get_by_email(email):
        """Get student by email"""
        db = DatabaseManager()
        query = 'SELECT * FROM students WHERE email = ?'
        results = db.execute_query(query, (email,))
        if results:
            return dict(results[0])
        return None

    @staticmethod
    def update(student_id, **kwargs):
        """Update student details"""
        db = DatabaseManager()
        now = datetime.now().isoformat()

        # Build dynamic update query based on provided fields
        fields = []
        values = []

        allowed_fields = ['first_name', 'last_name', 'email', 'phone',
                         'address', 'gpa', 'graduation_year']

        for field, value in kwargs.items():
            if field in allowed_fields:
                fields.append(f'{field} = ?')
                values.append(value)

        if not fields:
            return False

        fields.append('updated_at = ?')
        values.append(now)
        values.append(student_id)

        query = f"UPDATE students SET {', '.join(fields)} WHERE id = ?"
        try:
            db.execute_update(query, tuple(values))
            return True
        except Exception as e:
            print(f"Error updating student: {e}")
            return False

    @staticmethod
    def delete(student_id):
        """Delete a student"""
        db = DatabaseManager()
        query = 'DELETE FROM students WHERE id = ?'
        db.execute_update(query, (student_id,))
        return True

    @staticmethod
    def search(keyword):
        """Search students by name or email"""
        db = DatabaseManager()
        query = '''
            SELECT * FROM students
            WHERE first_name LIKE ? OR last_name LIKE ? OR email LIKE ?
            ORDER BY last_name, first_name
        '''
        search_term = f'%{keyword}%'
        results = db.execute_query(query, (search_term, search_term, search_term))
        return [dict(row) for row in results]

    @staticmethod
    def get_by_gpa_range(min_gpa, max_gpa):
        """Get students within a GPA range"""
        db = DatabaseManager()
        query = '''
            SELECT * FROM students
            WHERE gpa BETWEEN ? AND ?
            ORDER BY gpa DESC
        '''
        results = db.execute_query(query, (min_gpa, max_gpa))
        return [dict(row) for row in results]
