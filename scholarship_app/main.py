"""
Main entry point for the Scholarship Management Application
"""

from cli import ScholarshipCLI


def main():
    """Run the application"""
    app = ScholarshipCLI()
    app.run()


if __name__ == '__main__':
    main()
