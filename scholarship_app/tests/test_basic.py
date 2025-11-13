"""
Basic tests for scholarship app functionality
"""

import sys
import os

# Add parent directory to path
parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parent_dir)

from scholarship_app.models import Scholarship, Student, Application


def test_scholarships():
    """Test scholarship operations"""
    print("Testing Scholarship operations...")

    # Get all scholarships
    scholarships = Scholarship.get_all()
    print(f"  ✓ Found {len(scholarships)} scholarships")

    # Get a specific scholarship
    if scholarships:
        s = Scholarship.get_by_id(1)
        if s:
            print(f"  ✓ Retrieved scholarship: {s['name']}")

    # Search scholarships
    results = Scholarship.search("STEM")
    print(f"  ✓ Search found {len(results)} STEM scholarships")

    return True


def test_students():
    """Test student operations"""
    print("\nTesting Student operations...")

    # Get all students
    students = Student.get_all()
    print(f"  ✓ Found {len(students)} students")

    # Get a specific student
    if students:
        s = Student.get_by_id(1)
        if s:
            print(f"  ✓ Retrieved student: {s['first_name']} {s['last_name']}")

    # Search students
    results = Student.search("Johnson")
    print(f"  ✓ Search found {len(results)} students with 'Johnson'")

    return True


def test_applications():
    """Test application operations"""
    print("\nTesting Application operations...")

    # Get all applications
    applications = Application.get_all()
    print(f"  ✓ Found {len(applications)} applications")

    # Get applications by status
    pending = Application.get_by_status('pending')
    print(f"  ✓ Found {len(pending)} pending applications")

    approved = Application.get_by_status('approved')
    print(f"  ✓ Found {len(approved)} approved applications")

    # Get statistics
    stats = Application.get_statistics()
    if stats:
        print(f"  ✓ Statistics:")
        print(f"    - Total: {stats['total_applications']}")
        print(f"    - Pending: {stats['pending']}")
        print(f"    - Approved: {stats['approved']}")
        print(f"    - Awarded: {stats['awarded']}")

    return True


def run_tests():
    """Run all tests"""
    print("="*60)
    print(" RUNNING TESTS ".center(60, "="))
    print("="*60)

    try:
        test_scholarships()
        test_students()
        test_applications()

        print("\n" + "="*60)
        print(" ALL TESTS PASSED ".center(60, "="))
        print("="*60)

    except Exception as e:
        print(f"\n✗ Test failed with error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    run_tests()
