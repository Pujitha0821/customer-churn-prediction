# Quick Start Guide

## Get Started in 3 Steps

### 1. Install Dependencies
```bash
cd scholarship_app
pip install -r requirements.txt
```

### 2. Load Sample Data (Optional)
```bash
python utils/sample_data.py
```

This will create:
- 5 sample scholarships
- 5 sample students
- 8 sample applications

### 3. Run the Application
```bash
python main.py
```

or

```bash
python cli.py
```

## First Time Usage

When you first run the application, the menu will appear:

```
============================================================
========== SCHOLARSHIP MANAGEMENT SYSTEM ==================
============================================================

[1] Manage Scholarships
[2] Manage Students
[3] Manage Applications
[4] View Statistics
[5] Search
[0] Exit
```

### Try These Common Tasks

#### View All Scholarships
1. Select `[1] Manage Scholarships`
2. Select `[2] View All Scholarships`

#### Submit an Application
1. Select `[3] Manage Applications`
2. Select `[1] Submit New Application`
3. Enter Student ID (e.g., 1)
4. Enter Scholarship ID (e.g., 1)
5. Add optional notes

#### View Statistics
- Select `[4] View Statistics` from main menu

#### Search for a Scholarship
1. Select `[1] Manage Scholarships`
2. Select `[6] Search Scholarships`
3. Enter keyword (e.g., "STEM")

## Sample IDs (if you loaded sample data)

**Students:**
- ID 1: Emily Johnson
- ID 2: Michael Chen
- ID 3: Sarah Williams
- ID 4: David Martinez
- ID 5: Jessica Taylor

**Scholarships:**
- ID 1: Merit Excellence Scholarship ($5,000)
- ID 2: STEM Innovation Award ($7,500)
- ID 3: Community Service Scholarship ($3,000)
- ID 4: First Generation College Student Grant ($4,000)
- ID 5: Arts and Humanities Scholarship ($3,500)

## Testing

Run the test suite to verify everything is working:
```bash
python tests/test_basic.py
```

## Need Help?

See the full [README.md](README.md) for detailed documentation.

## Common Issues

**Module not found error:**
- Make sure you're in the `scholarship_app` directory
- Verify dependencies are installed: `pip install -r requirements.txt`

**Database locked error:**
- Close any other instances of the application
- Check if the database file exists: `ls database/scholarship.db`

---

Enjoy managing scholarships! 🎓
