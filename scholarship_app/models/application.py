"""
Application Model
Handles scholarship application tracking
"""

from datetime import datetime
from ..database import DatabaseManager


class Application:
    def __init__(self, application_id=None, student_id=None, scholarship_id=None,
                 application_date=None, status='pending', notes=None):
        self.id = application_id
        self.student_id = student_id
        self.scholarship_id = scholarship_id
        self.application_date = application_date
        self.status = status
        self.notes = notes
        self.db = DatabaseManager()

    @staticmethod
    def create(student_id, scholarship_id, status='pending', notes=None):
        """Create a new scholarship application"""
        db = DatabaseManager()
        now = datetime.now().isoformat()

        query = '''
            INSERT INTO applications
            (student_id, scholarship_id, application_date, status, notes, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        '''
        params = (student_id, scholarship_id, now, status, notes, now, now)

        try:
            application_id = db.execute_update(query, params)
            return application_id
        except Exception as e:
            print(f"Error creating application: {e}")
            return None

    @staticmethod
    def get_all():
        """Get all applications with student and scholarship details"""
        db = DatabaseManager()
        query = '''
            SELECT
                a.*,
                s.first_name || ' ' || s.last_name as student_name,
                s.email as student_email,
                sc.name as scholarship_name,
                sc.amount as scholarship_amount
            FROM applications a
            JOIN students s ON a.student_id = s.id
            JOIN scholarships sc ON a.scholarship_id = sc.id
            ORDER BY a.application_date DESC
        '''
        results = db.execute_query(query)
        return [dict(row) for row in results]

    @staticmethod
    def get_by_id(application_id):
        """Get application by ID with details"""
        db = DatabaseManager()
        query = '''
            SELECT
                a.*,
                s.first_name || ' ' || s.last_name as student_name,
                s.email as student_email,
                sc.name as scholarship_name,
                sc.amount as scholarship_amount
            FROM applications a
            JOIN students s ON a.student_id = s.id
            JOIN scholarships sc ON a.scholarship_id = sc.id
            WHERE a.id = ?
        '''
        results = db.execute_query(query, (application_id,))
        if results:
            return dict(results[0])
        return None

    @staticmethod
    def get_by_student(student_id):
        """Get all applications for a specific student"""
        db = DatabaseManager()
        query = '''
            SELECT
                a.*,
                sc.name as scholarship_name,
                sc.amount as scholarship_amount,
                sc.deadline as scholarship_deadline
            FROM applications a
            JOIN scholarships sc ON a.scholarship_id = sc.id
            WHERE a.student_id = ?
            ORDER BY a.application_date DESC
        '''
        results = db.execute_query(query, (student_id,))
        return [dict(row) for row in results]

    @staticmethod
    def get_by_scholarship(scholarship_id):
        """Get all applications for a specific scholarship"""
        db = DatabaseManager()
        query = '''
            SELECT
                a.*,
                s.first_name || ' ' || s.last_name as student_name,
                s.email as student_email,
                s.gpa as student_gpa
            FROM applications a
            JOIN students s ON a.student_id = s.id
            WHERE a.scholarship_id = ?
            ORDER BY a.application_date DESC
        '''
        results = db.execute_query(query, (scholarship_id,))
        return [dict(row) for row in results]

    @staticmethod
    def get_by_status(status):
        """Get all applications with a specific status"""
        db = DatabaseManager()
        query = '''
            SELECT
                a.*,
                s.first_name || ' ' || s.last_name as student_name,
                s.email as student_email,
                sc.name as scholarship_name,
                sc.amount as scholarship_amount
            FROM applications a
            JOIN students s ON a.student_id = s.id
            JOIN scholarships sc ON a.scholarship_id = sc.id
            WHERE a.status = ?
            ORDER BY a.application_date DESC
        '''
        results = db.execute_query(query, (status,))
        return [dict(row) for row in results]

    @staticmethod
    def update_status(application_id, status, notes=None):
        """Update application status"""
        db = DatabaseManager()
        now = datetime.now().isoformat()

        if notes:
            query = 'UPDATE applications SET status = ?, notes = ?, updated_at = ? WHERE id = ?'
            params = (status, notes, now, application_id)
        else:
            query = 'UPDATE applications SET status = ?, updated_at = ? WHERE id = ?'
            params = (status, now, application_id)

        db.execute_update(query, params)
        return True

    @staticmethod
    def delete(application_id):
        """Delete an application"""
        db = DatabaseManager()
        query = 'DELETE FROM applications WHERE id = ?'
        db.execute_update(query, (application_id,))
        return True

    @staticmethod
    def get_statistics():
        """Get application statistics"""
        db = DatabaseManager()
        query = '''
            SELECT
                COUNT(*) as total_applications,
                SUM(CASE WHEN status = 'pending' THEN 1 ELSE 0 END) as pending,
                SUM(CASE WHEN status = 'approved' THEN 1 ELSE 0 END) as approved,
                SUM(CASE WHEN status = 'rejected' THEN 1 ELSE 0 END) as rejected,
                SUM(CASE WHEN status = 'awarded' THEN 1 ELSE 0 END) as awarded
            FROM applications
        '''
        results = db.execute_query(query)
        if results:
            return dict(results[0])
        return None
