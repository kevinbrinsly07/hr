# HR Management System

A modern, responsive HR management system built with Flask, SQLAlchemy, and Bootstrap-inspired CSS. This application provides comprehensive HR functionality with a clean, professional interface.

## 🚀 Features

### Core HR Modules
- **👥 Employee Management**: Add, view, and manage employee records
- **💼 Job Management**: Create and manage job postings
- **📋 Application Tracking**: Track job applications and candidates
- **💰 Payroll Processing**: Manage employee payroll records
- **🎁 Benefits Administration**: Handle employee benefits and enrollments
- **📊 Performance Reviews**: Conduct and track performance evaluations
- **💵 Compensation Management**: Manage salary and compensation data

### User Experience
- **🔐 Secure Authentication**: User registration and login system
- **📱 Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- **🔔 Real-time Notifications**: Toast-style notifications with auto-dismiss
- **🎨 Modern UI**: Clean, professional interface with glassmorphism effects
- **📊 Data Tables**: Sortable, responsive tables with mobile card layouts

### Technical Features
- **🗄️ SQLite Database**: Lightweight, file-based database
- **🔒 User Sessions**: Secure login sessions with Flask-Login
- **📝 Form Validation**: WTForms for robust form handling
- **🛡️ CSRF Protection**: Built-in security measures
- **📁 Modular Architecture**: Blueprint-based routing structure

## 🛠️ Technology Stack

- **Backend**: Python Flask 2.3.3
- **Database**: SQLAlchemy 3.0.5 with SQLite
- **Authentication**: Flask-Login 0.6.3
- **Forms**: Flask-WTF 1.1.1 with WTForms 3.0.1
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Styling**: Custom CSS with modern design principles

## 📋 Prerequisites

- Python 3.8 or higher
- pip package manager
- Git (for cloning the repository)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd hr-management-system
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```

### 5. Access the Application
Open your browser and navigate to: `http://localhost:5000`

### 6. Initial Setup
- Register a new user account
- Login with your credentials
- Start managing HR data through the dashboard

## 📁 Project Structure

```
hr-management-system/
├── app.py                 # Main Flask application
├── config.py             # Application configuration
├── models.py             # SQLAlchemy database models
├── forms.py              # WTForms definitions
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore rules
├── README.md            # Project documentation
├── instance/            # SQLite database (auto-generated)
├── routes/              # Flask blueprints
│   ├── __init__.py
│   ├── auth.py          # Authentication routes
│   └── main.py          # Main application routes
├── static/              # Static assets
│   └── css/
│       └── style.css    # Application styles
└── templates/           # Jinja2 templates
    ├── base.html        # Base template with navigation
    ├── index.html       # Dashboard
    ├── login.html       # Login page (standalone)
    ├── register.html    # Registration page (standalone)
    ├── employees.html   # Employee management
    ├── jobs.html        # Job management
    ├── applications.html # Application tracking
    ├── payroll.html     # Payroll management
    ├── benefits.html    # Benefits administration
    ├── performance.html # Performance reviews
    ├── compensation.html # Compensation management
    └── [additional templates...]
```

## 🗄️ Database Schema

The application uses SQLite with the following main entities:

- **Users**: Authentication and user management
- **Employees**: Employee personal and professional information
- **Jobs**: Job postings and descriptions
- **Applications**: Job applications and candidate tracking
- **Payroll**: Salary and payroll records
- **Benefits**: Available benefits and employee enrollments
- **Performance Reviews**: Employee performance evaluations
- **Compensation**: Salary and compensation data

## 🎯 Usage Guide

### Getting Started
1. **Registration**: Create a new account or use the default admin account
2. **Dashboard**: Access the main dashboard with navigation to all modules
3. **Navigation**: Use the responsive navigation menu to access different sections

### Key Workflows
- **Add Employees**: Navigate to Employees → Add New Employee
- **Create Jobs**: Go to Jobs → Add New Job
- **Process Payroll**: Access Payroll → Add Payroll Record
- **Manage Benefits**: Benefits section for enrollment and administration

### Mobile Experience
- **Responsive Tables**: Desktop tables convert to mobile-friendly cards
- **Touch Navigation**: Optimized for touch interactions
- **Notification System**: Toast notifications work across all devices

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the root directory:

```env
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///hr_system.db
```

### Database Configuration
The application automatically creates and initializes the SQLite database on first run. Database files are stored in the `instance/` directory.

## 🧪 Development

### Running in Development Mode
```bash
export FLASK_ENV=development
flask run
```

### Database Migrations
```bash
# Reset database (development only)
rm instance/hr_system.db
python app.py  # Recreates database
```

### Code Style
- Follow PEP 8 Python style guidelines
- Use descriptive variable and function names
- Add docstrings to functions and classes

## 🚀 Deployment

### Production Considerations
- Set `FLASK_ENV=production`
- Use a production WSGI server (Gunicorn, uWSGI)
- Configure proper database (PostgreSQL recommended)
- Enable HTTPS
- Set strong SECRET_KEY
- Configure proper logging

### Basic Production Setup
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:create_app()
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🐛 Known Issues & Future Enhancements

### Current Limitations
- Basic authentication (enhance with role-based access)
- SQLite database (consider PostgreSQL for production)
- No file upload functionality
- Limited reporting capabilities

### Planned Features
- Advanced user roles and permissions
- Email notifications
- File upload for documents/resumes
- Advanced reporting and analytics
- API endpoints for integrations
- Multi-language support

## 📞 Support

For questions, issues, or contributions:
- Create an issue in the repository
- Contact the development team
- Check the documentation for common solutions

---

**Built with ❤️ using Flask and modern web technologies**