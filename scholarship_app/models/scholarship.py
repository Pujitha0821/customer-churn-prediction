"""
Scholarship Model
Handles all scholarship-related database operations
"""

from datetime import datetime
from ..database import DatabaseManager


class Scholarship:
    def __init__(self, scholarship_id=None, name=None, description=None,
                 amount=None, deadline=None, eligibility_criteria=None, provider=None):
        self.id = scholarship_id
        self.name = name
        self.description = description
        self.amount = amount
        self.deadline = deadline
        self.eligibility_criteria = eligibility_criteria
        self.provider = provider
        self.db = DatabaseManager()

    @staticmethod
    def create(name, amount, deadline, description=None,
               eligibility_criteria=None, provider=None):
        """Create a new scholarship"""
        db = DatabaseManager()
        now = datetime.now().isoformat()

        query = '''
            INSERT INTO scholarships
            (name, description, amount, deadline, eligibility_criteria, provider, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        '''
        params = (name, description, amount, deadline, eligibility_criteria, provider, now, now)

        scholarship_id = db.execute_update(query, params)
        return scholarship_id

    @staticmethod
    def get_all():
        """Get all scholarships"""
        db = DatabaseManager()
        query = 'SELECT * FROM scholarships ORDER BY deadline ASC'
        results = db.execute_query(query)
        return [dict(row) for row in results]

    @staticmethod
    def get_by_id(scholarship_id):
        """Get scholarship by ID"""
        db = DatabaseManager()
        query = 'SELECT * FROM scholarships WHERE id = ?'
        results = db.execute_query(query, (scholarship_id,))
        if results:
            return dict(results[0])
        return None

    @staticmethod
    def update(scholarship_id, **kwargs):
        """Update scholarship details"""
        db = DatabaseManager()
        now = datetime.now().isoformat()

        # Build dynamic update query based on provided fields
        fields = []
        values = []

        allowed_fields = ['name', 'description', 'amount', 'deadline',
                         'eligibility_criteria', 'provider']

        for field, value in kwargs.items():
            if field in allowed_fields:
                fields.append(f'{field} = ?')
                values.append(value)

        if not fields:
            return False

        fields.append('updated_at = ?')
        values.append(now)
        values.append(scholarship_id)

        query = f"UPDATE scholarships SET {', '.join(fields)} WHERE id = ?"
        db.execute_update(query, tuple(values))
        return True

    @staticmethod
    def delete(scholarship_id):
        """Delete a scholarship"""
        db = DatabaseManager()
        query = 'DELETE FROM scholarships WHERE id = ?'
        db.execute_update(query, (scholarship_id,))
        return True

    @staticmethod
    def search(keyword):
        """Search scholarships by name or provider"""
        db = DatabaseManager()
        query = '''
            SELECT * FROM scholarships
            WHERE name LIKE ? OR provider LIKE ? OR description LIKE ?
            ORDER BY deadline ASC
        '''
        search_term = f'%{keyword}%'
        results = db.execute_query(query, (search_term, search_term, search_term))
        return [dict(row) for row in results]

    @staticmethod
    def get_by_amount_range(min_amount, max_amount):
        """Get scholarships within an amount range"""
        db = DatabaseManager()
        query = '''
            SELECT * FROM scholarships
            WHERE amount BETWEEN ? AND ?
            ORDER BY amount DESC
        '''
        results = db.execute_query(query, (min_amount, max_amount))
        return [dict(row) for row in results]
