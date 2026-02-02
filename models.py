from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), default='employee')  # admin, hr, employee

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    hire_date = db.Column(db.Date, nullable=False)
    department = db.Column(db.String(50))
    position = db.Column(db.String(50))
    salary = db.Column(db.Float)
    manager_id = db.Column(db.Integer, db.ForeignKey('employee.id'))

    applications = db.relationship('Application', backref='employee', lazy=True)
    payrolls = db.relationship('Payroll', backref='employee', lazy=True)
    benefits = db.relationship('EmployeeBenefit', backref='employee', lazy=True)
    reviews = db.relationship('PerformanceReview', foreign_keys='PerformanceReview.employee_id', backref='reviewed_employee', lazy=True)
    given_reviews = db.relationship('PerformanceReview', foreign_keys='PerformanceReview.reviewer_id', backref='reviewer', lazy=True)
    compensations = db.relationship('Compensation', backref='employee', lazy=True)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    department = db.Column(db.String(50))
    requirements = db.Column(db.Text)
    posted_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='open')  # open, closed

    applications = db.relationship('Application', backref='job', lazy=True)

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=True)
    applicant_name = db.Column(db.String(100), nullable=False)
    applicant_email = db.Column(db.String(120), nullable=False)
    resume = db.Column(db.Text)
    status = db.Column(db.String(20), default='pending')  # pending, reviewed, accepted, rejected
    applied_date = db.Column(db.DateTime, default=datetime.utcnow)

class Payroll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    pay_period_start = db.Column(db.Date, nullable=False)
    pay_period_end = db.Column(db.Date, nullable=False)
    hours_worked = db.Column(db.Float, default=0)
    overtime_hours = db.Column(db.Float, default=0)
    gross_pay = db.Column(db.Float, nullable=False)
    deductions = db.Column(db.Float, default=0)
    net_pay = db.Column(db.Float, nullable=False)
    processed_date = db.Column(db.DateTime, default=datetime.utcnow)

class Benefit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    cost = db.Column(db.Float, default=0)
    type = db.Column(db.String(50))  # health, dental, etc.

    employees = db.relationship('EmployeeBenefit', backref='benefit', lazy=True)

class EmployeeBenefit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    benefit_id = db.Column(db.Integer, db.ForeignKey('benefit.id'), nullable=False)
    enrollment_date = db.Column(db.Date, default=datetime.utcnow)

class PerformanceReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    reviewer_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    review_date = db.Column(db.Date, nullable=False)
    rating = db.Column(db.Integer)  # 1-5
    comments = db.Column(db.Text)
    goals = db.Column(db.Text)

class Compensation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    base_salary = db.Column(db.Float, nullable=False)
    bonuses = db.Column(db.Float, default=0)
    equity = db.Column(db.Float, default=0)
    last_review_date = db.Column(db.Date)
    next_review_date = db.Column(db.Date)