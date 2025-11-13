"""
Command Line Interface for Scholarship Management Application
"""

import sys
import os
from datetime import datetime
from tabulate import tabulate

# Add parent directory to path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from scholarship_app.database import DatabaseManager
from scholarship_app.models import Scholarship, Student, Application


class ScholarshipCLI:
    def __init__(self):
        self.db = DatabaseManager()
        self.db.create_tables()

    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('clear' if os.name == 'posix' else 'cls')

    def display_menu(self):
        """Display main menu"""
        print("\n" + "="*60)
        print(" SCHOLARSHIP MANAGEMENT SYSTEM ".center(60, "="))
        print("="*60)
        print("\n[1] Manage Scholarships")
        print("[2] Manage Students")
        print("[3] Manage Applications")
        print("[4] View Statistics")
        print("[5] Search")
        print("[0] Exit")
        print("-"*60)

    def scholarship_menu(self):
        """Scholarship management menu"""
        while True:
            print("\n" + "="*60)
            print(" SCHOLARSHIP MANAGEMENT ".center(60, "="))
            print("="*60)
            print("\n[1] Add New Scholarship")
            print("[2] View All Scholarships")
            print("[3] View Scholarship Details")
            print("[4] Update Scholarship")
            print("[5] Delete Scholarship")
            print("[6] Search Scholarships")
            print("[0] Back to Main Menu")
            print("-"*60)

            choice = input("\nEnter your choice: ").strip()

            if choice == '1':
                self.add_scholarship()
            elif choice == '2':
                self.view_all_scholarships()
            elif choice == '3':
                self.view_scholarship_details()
            elif choice == '4':
                self.update_scholarship()
            elif choice == '5':
                self.delete_scholarship()
            elif choice == '6':
                self.search_scholarships()
            elif choice == '0':
                break
            else:
                print("Invalid choice. Please try again.")

    def student_menu(self):
        """Student management menu"""
        while True:
            print("\n" + "="*60)
            print(" STUDENT MANAGEMENT ".center(60, "="))
            print("="*60)
            print("\n[1] Add New Student")
            print("[2] View All Students")
            print("[3] View Student Details")
            print("[4] Update Student")
            print("[5] Delete Student")
            print("[6] Search Students")
            print("[0] Back to Main Menu")
            print("-"*60)

            choice = input("\nEnter your choice: ").strip()

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_all_students()
            elif choice == '3':
                self.view_student_details()
            elif choice == '4':
                self.update_student()
            elif choice == '5':
                self.delete_student()
            elif choice == '6':
                self.search_students()
            elif choice == '0':
                break
            else:
                print("Invalid choice. Please try again.")

    def application_menu(self):
        """Application management menu"""
        while True:
            print("\n" + "="*60)
            print(" APPLICATION MANAGEMENT ".center(60, "="))
            print("="*60)
            print("\n[1] Submit New Application")
            print("[2] View All Applications")
            print("[3] View Application Details")
            print("[4] Update Application Status")
            print("[5] View Applications by Student")
            print("[6] View Applications by Scholarship")
            print("[7] View Applications by Status")
            print("[8] Delete Application")
            print("[0] Back to Main Menu")
            print("-"*60)

            choice = input("\nEnter your choice: ").strip()

            if choice == '1':
                self.submit_application()
            elif choice == '2':
                self.view_all_applications()
            elif choice == '3':
                self.view_application_details()
            elif choice == '4':
                self.update_application_status()
            elif choice == '5':
                self.view_applications_by_student()
            elif choice == '6':
                self.view_applications_by_scholarship()
            elif choice == '7':
                self.view_applications_by_status()
            elif choice == '8':
                self.delete_application()
            elif choice == '0':
                break
            else:
                print("Invalid choice. Please try again.")

    # ==================== Scholarship Methods ====================

    def add_scholarship(self):
        """Add a new scholarship"""
        print("\n--- Add New Scholarship ---")
        name = input("Scholarship Name: ").strip()
        description = input("Description: ").strip()
        amount = float(input("Amount ($): "))
        deadline = input("Deadline (YYYY-MM-DD): ").strip()
        eligibility = input("Eligibility Criteria: ").strip()
        provider = input("Provider/Organization: ").strip()

        scholarship_id = Scholarship.create(
            name=name,
            amount=amount,
            deadline=deadline,
            description=description,
            eligibility_criteria=eligibility,
            provider=provider
        )

        print(f"\n✓ Scholarship added successfully! (ID: {scholarship_id})")

    def view_all_scholarships(self):
        """View all scholarships"""
        scholarships = Scholarship.get_all()

        if not scholarships:
            print("\nNo scholarships found.")
            return

        print(f"\n--- All Scholarships (Total: {len(scholarships)}) ---")
        table_data = []
        for s in scholarships:
            table_data.append([
                s['id'],
                s['name'][:30],
                f"${s['amount']:.2f}",
                s['deadline'],
                s['provider'][:20] if s['provider'] else 'N/A'
            ])

        headers = ['ID', 'Name', 'Amount', 'Deadline', 'Provider']
        print(tabulate(table_data, headers=headers, tablefmt='grid'))

    def view_scholarship_details(self):
        """View detailed information about a scholarship"""
        scholarship_id = int(input("\nEnter Scholarship ID: "))
        scholarship = Scholarship.get_by_id(scholarship_id)

        if not scholarship:
            print(f"\nScholarship with ID {scholarship_id} not found.")
            return

        print("\n--- Scholarship Details ---")
        print(f"ID: {scholarship['id']}")
        print(f"Name: {scholarship['name']}")
        print(f"Description: {scholarship['description'] or 'N/A'}")
        print(f"Amount: ${scholarship['amount']:.2f}")
        print(f"Deadline: {scholarship['deadline']}")
        print(f"Eligibility: {scholarship['eligibility_criteria'] or 'N/A'}")
        print(f"Provider: {scholarship['provider'] or 'N/A'}")

        # Show applications for this scholarship
        applications = Application.get_by_scholarship(scholarship_id)
        print(f"\nTotal Applications: {len(applications)}")

    def update_scholarship(self):
        """Update scholarship information"""
        scholarship_id = int(input("\nEnter Scholarship ID to update: "))
        scholarship = Scholarship.get_by_id(scholarship_id)

        if not scholarship:
            print(f"\nScholarship with ID {scholarship_id} not found.")
            return

        print("\nLeave blank to keep current value")
        name = input(f"Name [{scholarship['name']}]: ").strip()
        description = input(f"Description [{scholarship['description']}]: ").strip()
        amount = input(f"Amount [{scholarship['amount']}]: ").strip()
        deadline = input(f"Deadline [{scholarship['deadline']}]: ").strip()
        eligibility = input(f"Eligibility [{scholarship['eligibility_criteria']}]: ").strip()
        provider = input(f"Provider [{scholarship['provider']}]: ").strip()

        update_data = {}
        if name:
            update_data['name'] = name
        if description:
            update_data['description'] = description
        if amount:
            update_data['amount'] = float(amount)
        if deadline:
            update_data['deadline'] = deadline
        if eligibility:
            update_data['eligibility_criteria'] = eligibility
        if provider:
            update_data['provider'] = provider

        if update_data:
            Scholarship.update(scholarship_id, **update_data)
            print("\n✓ Scholarship updated successfully!")
        else:
            print("\nNo changes made.")

    def delete_scholarship(self):
        """Delete a scholarship"""
        scholarship_id = int(input("\nEnter Scholarship ID to delete: "))
        scholarship = Scholarship.get_by_id(scholarship_id)

        if not scholarship:
            print(f"\nScholarship with ID {scholarship_id} not found.")
            return

        confirm = input(f"\nAre you sure you want to delete '{scholarship['name']}'? (yes/no): ")
        if confirm.lower() == 'yes':
            Scholarship.delete(scholarship_id)
            print("\n✓ Scholarship deleted successfully!")
        else:
            print("\nDeletion cancelled.")

    def search_scholarships(self):
        """Search scholarships"""
        keyword = input("\nEnter search keyword: ").strip()
        scholarships = Scholarship.search(keyword)

        if not scholarships:
            print(f"\nNo scholarships found matching '{keyword}'.")
            return

        print(f"\n--- Search Results (Found: {len(scholarships)}) ---")
        table_data = []
        for s in scholarships:
            table_data.append([
                s['id'],
                s['name'][:30],
                f"${s['amount']:.2f}",
                s['deadline'],
                s['provider'][:20] if s['provider'] else 'N/A'
            ])

        headers = ['ID', 'Name', 'Amount', 'Deadline', 'Provider']
        print(tabulate(table_data, headers=headers, tablefmt='grid'))

    # ==================== Student Methods ====================

    def add_student(self):
        """Add a new student"""
        print("\n--- Add New Student ---")
        first_name = input("First Name: ").strip()
        last_name = input("Last Name: ").strip()
        email = input("Email: ").strip()
        phone = input("Phone (optional): ").strip()
        address = input("Address (optional): ").strip()
        gpa = input("GPA (optional): ").strip()
        graduation_year = input("Graduation Year (optional): ").strip()

        student_id = Student.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone if phone else None,
            address=address if address else None,
            gpa=float(gpa) if gpa else None,
            graduation_year=int(graduation_year) if graduation_year else None
        )

        if student_id:
            print(f"\n✓ Student added successfully! (ID: {student_id})")
        else:
            print("\n✗ Error adding student. Email might already exist.")

    def view_all_students(self):
        """View all students"""
        students = Student.get_all()

        if not students:
            print("\nNo students found.")
            return

        print(f"\n--- All Students (Total: {len(students)}) ---")
        table_data = []
        for s in students:
            table_data.append([
                s['id'],
                f"{s['first_name']} {s['last_name']}",
                s['email'],
                s['gpa'] if s['gpa'] else 'N/A',
                s['graduation_year'] if s['graduation_year'] else 'N/A'
            ])

        headers = ['ID', 'Name', 'Email', 'GPA', 'Grad Year']
        print(tabulate(table_data, headers=headers, tablefmt='grid'))

    def view_student_details(self):
        """View detailed information about a student"""
        student_id = int(input("\nEnter Student ID: "))
        student = Student.get_by_id(student_id)

        if not student:
            print(f"\nStudent with ID {student_id} not found.")
            return

        print("\n--- Student Details ---")
        print(f"ID: {student['id']}")
        print(f"Name: {student['first_name']} {student['last_name']}")
        print(f"Email: {student['email']}")
        print(f"Phone: {student['phone'] or 'N/A'}")
        print(f"Address: {student['address'] or 'N/A'}")
        print(f"GPA: {student['gpa'] or 'N/A'}")
        print(f"Graduation Year: {student['graduation_year'] or 'N/A'}")

        # Show applications by this student
        applications = Application.get_by_student(student_id)
        print(f"\nTotal Applications: {len(applications)}")

    def update_student(self):
        """Update student information"""
        student_id = int(input("\nEnter Student ID to update: "))
        student = Student.get_by_id(student_id)

        if not student:
            print(f"\nStudent with ID {student_id} not found.")
            return

        print("\nLeave blank to keep current value")
        first_name = input(f"First Name [{student['first_name']}]: ").strip()
        last_name = input(f"Last Name [{student['last_name']}]: ").strip()
        email = input(f"Email [{student['email']}]: ").strip()
        phone = input(f"Phone [{student['phone']}]: ").strip()
        address = input(f"Address [{student['address']}]: ").strip()
        gpa = input(f"GPA [{student['gpa']}]: ").strip()
        graduation_year = input(f"Graduation Year [{student['graduation_year']}]: ").strip()

        update_data = {}
        if first_name:
            update_data['first_name'] = first_name
        if last_name:
            update_data['last_name'] = last_name
        if email:
            update_data['email'] = email
        if phone:
            update_data['phone'] = phone
        if address:
            update_data['address'] = address
        if gpa:
            update_data['gpa'] = float(gpa)
        if graduation_year:
            update_data['graduation_year'] = int(graduation_year)

        if update_data:
            Student.update(student_id, **update_data)
            print("\n✓ Student updated successfully!")
        else:
            print("\nNo changes made.")

    def delete_student(self):
        """Delete a student"""
        student_id = int(input("\nEnter Student ID to delete: "))
        student = Student.get_by_id(student_id)

        if not student:
            print(f"\nStudent with ID {student_id} not found.")
            return

        confirm = input(f"\nAre you sure you want to delete '{student['first_name']} {student['last_name']}'? (yes/no): ")
        if confirm.lower() == 'yes':
            Student.delete(student_id)
            print("\n✓ Student deleted successfully!")
        else:
            print("\nDeletion cancelled.")

    def search_students(self):
        """Search students"""
        keyword = input("\nEnter search keyword: ").strip()
        students = Student.search(keyword)

        if not students:
            print(f"\nNo students found matching '{keyword}'.")
            return

        print(f"\n--- Search Results (Found: {len(students)}) ---")
        table_data = []
        for s in students:
            table_data.append([
                s['id'],
                f"{s['first_name']} {s['last_name']}",
                s['email'],
                s['gpa'] if s['gpa'] else 'N/A',
                s['graduation_year'] if s['graduation_year'] else 'N/A'
            ])

        headers = ['ID', 'Name', 'Email', 'GPA', 'Grad Year']
        print(tabulate(table_data, headers=headers, tablefmt='grid'))

    # ==================== Application Methods ====================

    def submit_application(self):
        """Submit a new scholarship application"""
        print("\n--- Submit New Application ---")

        # Show available students
        students = Student.get_all()
        if not students:
            print("No students found. Please add a student first.")
            return

        # Show available scholarships
        scholarships = Scholarship.get_all()
        if not scholarships:
            print("No scholarships found. Please add a scholarship first.")
            return

        student_id = int(input("Enter Student ID: "))
        if not Student.get_by_id(student_id):
            print("Invalid Student ID.")
            return

        scholarship_id = int(input("Enter Scholarship ID: "))
        if not Scholarship.get_by_id(scholarship_id):
            print("Invalid Scholarship ID.")
            return

        notes = input("Notes (optional): ").strip()

        application_id = Application.create(
            student_id=student_id,
            scholarship_id=scholarship_id,
            status='pending',
            notes=notes if notes else None
        )

        if application_id:
            print(f"\n✓ Application submitted successfully! (ID: {application_id})")
        else:
            print("\n✗ Error submitting application. Application might already exist.")

    def view_all_applications(self):
        """View all applications"""
        applications = Application.get_all()

        if not applications:
            print("\nNo applications found.")
            return

        print(f"\n--- All Applications (Total: {len(applications)}) ---")
        table_data = []
        for a in applications:
            table_data.append([
                a['id'],
                a['student_name'][:25],
                a['scholarship_name'][:25],
                f"${a['scholarship_amount']:.2f}",
                a['status'],
                a['application_date'][:10]
            ])

        headers = ['ID', 'Student', 'Scholarship', 'Amount', 'Status', 'Date']
        print(tabulate(table_data, headers=headers, tablefmt='grid'))

    def view_application_details(self):
        """View detailed information about an application"""
        application_id = int(input("\nEnter Application ID: "))
        application = Application.get_by_id(application_id)

        if not application:
            print(f"\nApplication with ID {application_id} not found.")
            return

        print("\n--- Application Details ---")
        print(f"ID: {application['id']}")
        print(f"Student: {application['student_name']} ({application['student_email']})")
        print(f"Scholarship: {application['scholarship_name']}")
        print(f"Amount: ${application['scholarship_amount']:.2f}")
        print(f"Status: {application['status'].upper()}")
        print(f"Application Date: {application['application_date']}")
        print(f"Notes: {application['notes'] or 'N/A'}")

    def update_application_status(self):
        """Update application status"""
        application_id = int(input("\nEnter Application ID: "))
        application = Application.get_by_id(application_id)

        if not application:
            print(f"\nApplication with ID {application_id} not found.")
            return

        print(f"\nCurrent Status: {application['status']}")
        print("\nAvailable statuses:")
        print("[1] Pending")
        print("[2] Under Review")
        print("[3] Approved")
        print("[4] Rejected")
        print("[5] Awarded")

        choice = input("\nSelect new status: ").strip()

        status_map = {
            '1': 'pending',
            '2': 'under review',
            '3': 'approved',
            '4': 'rejected',
            '5': 'awarded'
        }

        if choice in status_map:
            new_status = status_map[choice]
            notes = input("Additional notes (optional): ").strip()

            Application.update_status(
                application_id,
                new_status,
                notes if notes else None
            )
            print(f"\n✓ Application status updated to '{new_status}'!")
        else:
            print("\nInvalid choice.")

    def view_applications_by_student(self):
        """View all applications for a student"""
        student_id = int(input("\nEnter Student ID: "))
        student = Student.get_by_id(student_id)

        if not student:
            print(f"\nStudent with ID {student_id} not found.")
            return

        applications = Application.get_by_student(student_id)

        if not applications:
            print(f"\nNo applications found for {student['first_name']} {student['last_name']}.")
            return

        print(f"\n--- Applications by {student['first_name']} {student['last_name']} ---")
        table_data = []
        for a in applications:
            table_data.append([
                a['id'],
                a['scholarship_name'][:30],
                f"${a['scholarship_amount']:.2f}",
                a['status'],
                a['application_date'][:10]
            ])

        headers = ['ID', 'Scholarship', 'Amount', 'Status', 'Date']
        print(tabulate(table_data, headers=headers, tablefmt='grid'))

    def view_applications_by_scholarship(self):
        """View all applications for a scholarship"""
        scholarship_id = int(input("\nEnter Scholarship ID: "))
        scholarship = Scholarship.get_by_id(scholarship_id)

        if not scholarship:
            print(f"\nScholarship with ID {scholarship_id} not found.")
            return

        applications = Application.get_by_scholarship(scholarship_id)

        if not applications:
            print(f"\nNo applications found for {scholarship['name']}.")
            return

        print(f"\n--- Applications for {scholarship['name']} ---")
        table_data = []
        for a in applications:
            table_data.append([
                a['id'],
                a['student_name'][:30],
                a['student_email'],
                a['student_gpa'] if a['student_gpa'] else 'N/A',
                a['status'],
                a['application_date'][:10]
            ])

        headers = ['ID', 'Student', 'Email', 'GPA', 'Status', 'Date']
        print(tabulate(table_data, headers=headers, tablefmt='grid'))

    def view_applications_by_status(self):
        """View applications filtered by status"""
        print("\nFilter by status:")
        print("[1] Pending")
        print("[2] Under Review")
        print("[3] Approved")
        print("[4] Rejected")
        print("[5] Awarded")

        choice = input("\nSelect status: ").strip()

        status_map = {
            '1': 'pending',
            '2': 'under review',
            '3': 'approved',
            '4': 'rejected',
            '5': 'awarded'
        }

        if choice not in status_map:
            print("\nInvalid choice.")
            return

        status = status_map[choice]
        applications = Application.get_by_status(status)

        if not applications:
            print(f"\nNo applications found with status '{status}'.")
            return

        print(f"\n--- Applications with Status: {status.upper()} ---")
        table_data = []
        for a in applications:
            table_data.append([
                a['id'],
                a['student_name'][:25],
                a['scholarship_name'][:25],
                f"${a['scholarship_amount']:.2f}",
                a['application_date'][:10]
            ])

        headers = ['ID', 'Student', 'Scholarship', 'Amount', 'Date']
        print(tabulate(table_data, headers=headers, tablefmt='grid'))

    def delete_application(self):
        """Delete an application"""
        application_id = int(input("\nEnter Application ID to delete: "))
        application = Application.get_by_id(application_id)

        if not application:
            print(f"\nApplication with ID {application_id} not found.")
            return

        confirm = input(f"\nAre you sure you want to delete this application? (yes/no): ")
        if confirm.lower() == 'yes':
            Application.delete(application_id)
            print("\n✓ Application deleted successfully!")
        else:
            print("\nDeletion cancelled.")

    # ==================== Statistics ====================

    def view_statistics(self):
        """View application statistics"""
        stats = Application.get_statistics()

        if not stats:
            print("\nNo statistics available.")
            return

        print("\n" + "="*60)
        print(" APPLICATION STATISTICS ".center(60, "="))
        print("="*60)
        print(f"\nTotal Applications: {stats['total_applications']}")
        print(f"Pending: {stats['pending']}")
        print(f"Approved: {stats['approved']}")
        print(f"Rejected: {stats['rejected']}")
        print(f"Awarded: {stats['awarded']}")
        print("\nTotal Students: ", len(Student.get_all()))
        print("Total Scholarships: ", len(Scholarship.get_all()))

    # ==================== Main Run ====================

    def run(self):
        """Main application loop"""
        print("\n" + "="*60)
        print(" WELCOME TO SCHOLARSHIP MANAGEMENT SYSTEM ".center(60, "="))
        print("="*60)

        while True:
            self.display_menu()
            choice = input("\nEnter your choice: ").strip()

            if choice == '1':
                self.scholarship_menu()
            elif choice == '2':
                self.student_menu()
            elif choice == '3':
                self.application_menu()
            elif choice == '4':
                self.view_statistics()
            elif choice == '5':
                print("\n[1] Search Scholarships")
                print("[2] Search Students")
                search_choice = input("Enter your choice: ").strip()
                if search_choice == '1':
                    self.search_scholarships()
                elif search_choice == '2':
                    self.search_students()
            elif choice == '0':
                print("\nThank you for using Scholarship Management System!")
                print("Goodbye!\n")
                break
            else:
                print("\nInvalid choice. Please try again.")


if __name__ == '__main__':
    app = ScholarshipCLI()
    app.run()
