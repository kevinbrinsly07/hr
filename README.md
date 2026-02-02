# HR Management System

A comprehensive HR management system built with Flask and HTML/CSS.

## Features

- **Hiring & Onboarding**: Job postings, candidate tracking, streamlined onboarding
- **HR Data & Reporting**: Employee database, reporting dashboards
- **Payroll & Time**: Payroll processing, time tracking, tax calculations
- **Benefits Administration**: Benefits enrollment and management
- **Employee Experience**: Self-service portals, communication tools
- **Performance Management**: Reviews, goal setting, development planning
- **Compensation Management**: Pay benchmarking, compensation planning

## Setup

1. Clone or download the project files.

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Open your browser and go to `http://localhost:5000`

5. Register a new user or login with existing credentials.

## Project Structure

- `app.py`: Main application file
- `models.py`: Database models
- `config.py`: Configuration settings
- `routes/`: Blueprint routes
- `templates/`: HTML templates
- `static/css/`: CSS stylesheets
- `requirements.txt`: Python dependencies

## Database

The application uses SQLite for simplicity. The database file `hr_system.db` will be created automatically when you run the app.

## Usage

- Register as a new user
- Login to access the dashboard
- Navigate through different sections to manage HR data

## Notes

This is a basic implementation. In a production environment, you would need to add:
- Input validation and sanitization
- Error handling
- Security measures (HTTPS, CSRF protection)
- More advanced features like file uploads for resumes
- Email notifications
- Role-based access control