"""
Sample data loader for demonstration purposes
"""

import sys
import os

# Add parent directory to path
parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parent_dir)

from scholarship_app.database import DatabaseManager
from scholarship_app.models import Scholarship, Student, Application


def load_sample_data():
    """Load sample scholarships, students, and applications"""

    # Initialize database
    db = DatabaseManager()
    db.create_tables()

    print("Loading sample data...")

    # Sample Scholarships
    scholarships = [
        {
            'name': 'Merit Excellence Scholarship',
            'description': 'For students with outstanding academic performance',
            'amount': 5000.00,
            'deadline': '2024-06-30',
            'eligibility_criteria': 'GPA 3.5 or higher, Full-time student',
            'provider': 'Community Foundation'
        },
        {
            'name': 'STEM Innovation Award',
            'description': 'Supporting students pursuing STEM fields',
            'amount': 7500.00,
            'deadline': '2024-07-15',
            'eligibility_criteria': 'STEM major, GPA 3.0 or higher',
            'provider': 'Tech Corp Foundation'
        },
        {
            'name': 'Community Service Scholarship',
            'description': 'Recognizing students with strong community involvement',
            'amount': 3000.00,
            'deadline': '2024-08-01',
            'eligibility_criteria': '100+ hours of community service',
            'provider': 'Local Community Center'
        },
        {
            'name': 'First Generation College Student Grant',
            'description': 'Supporting first-generation college students',
            'amount': 4000.00,
            'deadline': '2024-07-30',
            'eligibility_criteria': 'First generation college student',
            'provider': 'Education Alliance'
        },
        {
            'name': 'Arts and Humanities Scholarship',
            'description': 'For students excelling in arts and humanities',
            'amount': 3500.00,
            'deadline': '2024-06-15',
            'eligibility_criteria': 'Arts or Humanities major, Portfolio required',
            'provider': 'Arts Council'
        }
    ]

    for s in scholarships:
        Scholarship.create(**s)
        print(f"  ✓ Added scholarship: {s['name']}")

    # Sample Students
    students = [
        {
            'first_name': 'Emily',
            'last_name': 'Johnson',
            'email': 'emily.johnson@email.com',
            'phone': '555-0101',
            'address': '123 Main St, City, State 12345',
            'gpa': 3.8,
            'graduation_year': 2025
        },
        {
            'first_name': 'Michael',
            'last_name': 'Chen',
            'email': 'michael.chen@email.com',
            'phone': '555-0102',
            'address': '456 Oak Ave, City, State 12345',
            'gpa': 3.9,
            'graduation_year': 2024
        },
        {
            'first_name': 'Sarah',
            'last_name': 'Williams',
            'email': 'sarah.williams@email.com',
            'phone': '555-0103',
            'address': '789 Pine Rd, City, State 12345',
            'gpa': 3.6,
            'graduation_year': 2025
        },
        {
            'first_name': 'David',
            'last_name': 'Martinez',
            'email': 'david.martinez@email.com',
            'phone': '555-0104',
            'address': '321 Elm St, City, State 12345',
            'gpa': 3.7,
            'graduation_year': 2024
        },
        {
            'first_name': 'Jessica',
            'last_name': 'Taylor',
            'email': 'jessica.taylor@email.com',
            'phone': '555-0105',
            'address': '654 Maple Dr, City, State 12345',
            'gpa': 3.5,
            'graduation_year': 2026
        }
    ]

    for st in students:
        Student.create(**st)
        print(f"  ✓ Added student: {st['first_name']} {st['last_name']}")

    # Sample Applications
    applications = [
        {'student_id': 1, 'scholarship_id': 1, 'status': 'approved', 'notes': 'Excellent application'},
        {'student_id': 1, 'scholarship_id': 2, 'status': 'pending', 'notes': None},
        {'student_id': 2, 'scholarship_id': 2, 'status': 'awarded', 'notes': 'Outstanding STEM project'},
        {'student_id': 2, 'scholarship_id': 1, 'status': 'approved', 'notes': None},
        {'student_id': 3, 'scholarship_id': 3, 'status': 'under review', 'notes': 'Impressive volunteer work'},
        {'student_id': 3, 'scholarship_id': 5, 'status': 'pending', 'notes': None},
        {'student_id': 4, 'scholarship_id': 4, 'status': 'approved', 'notes': 'Strong background'},
        {'student_id': 5, 'scholarship_id': 1, 'status': 'pending', 'notes': None},
    ]

    for app in applications:
        Application.create(**app)
        print(f"  ✓ Added application: Student {app['student_id']} -> Scholarship {app['scholarship_id']}")

    print("\n✓ Sample data loaded successfully!")
    print(f"  - {len(scholarships)} scholarships")
    print(f"  - {len(students)} students")
    print(f"  - {len(applications)} applications")


if __name__ == '__main__':
    load_sample_data()
