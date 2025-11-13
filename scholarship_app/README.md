# Scholarship Management System

A comprehensive local application for managing scholarships, students, and scholarship applications.

## Features

### Scholarship Management
- Create, read, update, and delete scholarship records
- Track scholarship details including:
  - Name and description
  - Award amount
  - Deadline
  - Eligibility criteria
  - Provider/organization
- Search scholarships by keyword
- Filter scholarships by amount range

### Student Management
- Maintain student/applicant records
- Track student information:
  - Personal details (name, email, phone, address)
  - Academic information (GPA, graduation year)
- Search students by name or email
- Filter students by GPA range

### Application Tracking
- Submit scholarship applications
- Track application status (pending, under review, approved, rejected, awarded)
- View applications by student
- View applications by scholarship
- Filter applications by status
- Add notes to applications
- Prevent duplicate applications

### Statistics & Reporting
- View overall application statistics
- Track pending, approved, rejected, and awarded applications
- Monitor total students and scholarships

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Navigate to the scholarship_app directory:
```bash
cd scholarship_app
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. (Optional) Load sample data:
```bash
python utils/sample_data.py
```

## Usage

### Running the Application

Start the application by running:
```bash
python main.py
```

Or alternatively:
```bash
python cli.py
```

### Main Menu Options

The application provides an intuitive menu-driven interface:

1. **Manage Scholarships** - Add, view, update, delete, and search scholarships
2. **Manage Students** - Add, view, update, delete, and search students
3. **Manage Applications** - Submit and track scholarship applications
4. **View Statistics** - See overall system statistics
5. **Search** - Quick search for scholarships or students
0. **Exit** - Close the application

### Sample Workflows

#### Adding a New Scholarship
1. Select "Manage Scholarships" from main menu
2. Choose "Add New Scholarship"
3. Enter scholarship details (name, amount, deadline, etc.)
4. Scholarship is saved to the database

#### Submitting an Application
1. Select "Manage Applications" from main menu
2. Choose "Submit New Application"
3. Enter student ID and scholarship ID
4. Add optional notes
5. Application is created with 'pending' status

#### Updating Application Status
1. Select "Manage Applications" from main menu
2. Choose "Update Application Status"
3. Enter application ID
4. Select new status (pending, under review, approved, rejected, awarded)
5. Add optional notes
6. Status is updated in the database

## Database Structure

The application uses SQLite database with three main tables:

### scholarships
- id (Primary Key)
- name
- description
- amount
- deadline
- eligibility_criteria
- provider
- created_at
- updated_at

### students
- id (Primary Key)
- first_name
- last_name
- email (Unique)
- phone
- address
- gpa
- graduation_year
- created_at
- updated_at

### applications
- id (Primary Key)
- student_id (Foreign Key)
- scholarship_id (Foreign Key)
- application_date
- status
- notes
- created_at
- updated_at

## Project Structure

```
scholarship_app/
│
├── database/
│   ├── __init__.py
│   ├── db_manager.py          # Database connection and schema
│   └── scholarship.db          # SQLite database (created on first run)
│
├── models/
│   ├── __init__.py
│   ├── scholarship.py          # Scholarship model and operations
│   ├── student.py              # Student model and operations
│   └── application.py          # Application model and operations
│
├── utils/
│   ├── __init__.py
│   └── sample_data.py          # Sample data loader
│
├── tests/                      # Test directory (for future tests)
│
├── __init__.py
├── main.py                     # Main entry point
├── cli.py                      # Command-line interface
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Features Explained

### CRUD Operations
- **Create**: Add new scholarships, students, and applications
- **Read**: View all records or individual details
- **Update**: Modify existing records
- **Delete**: Remove records (with confirmation)

### Search Functionality
- Search scholarships by name, provider, or description
- Search students by name or email
- All searches are case-insensitive and support partial matches

### Data Validation
- Email uniqueness for students
- Prevents duplicate applications (same student + scholarship)
- Foreign key constraints ensure data integrity

### User Interface
- Clean, menu-driven CLI
- Tabular data display using tabulate library
- Clear prompts and confirmations
- Status indicators (✓ for success, ✗ for errors)

## Sample Data

The application includes a sample data loader that creates:
- 5 sample scholarships
- 5 sample students
- 8 sample applications

To load sample data:
```bash
python utils/sample_data.py
```

## Tips

1. **Start with Sample Data**: Load sample data to explore the application features
2. **Unique Emails**: Student emails must be unique
3. **Application Statuses**: Available statuses are:
   - pending
   - under review
   - approved
   - rejected
   - awarded
4. **Date Format**: Use YYYY-MM-DD format for deadlines
5. **Backup**: The database file (scholarship.db) can be backed up by copying it

## Future Enhancements

Potential features for future versions:
- Web-based interface
- Email notifications for deadlines
- Document upload support
- Reporting and analytics dashboard
- Export to CSV/PDF
- Multi-user support with authentication
- Scholarship recommendation system

## Technical Details

- **Language**: Python 3.7+
- **Database**: SQLite3
- **UI Library**: tabulate (for table formatting)
- **Architecture**: Model-based with separated database layer

## Troubleshooting

### Database Locked Error
If you get a "database is locked" error, ensure no other instance of the application is running.

### Import Errors
Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Module Not Found
Ensure you're running the application from the correct directory (scholarship_app).

## License

This project is provided as-is for educational and local use.

## Contact

For questions or issues, please refer to the project repository.

---

**Version**: 1.0.0
**Last Updated**: November 2024
