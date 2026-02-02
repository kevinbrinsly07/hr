from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, FloatField, SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, Optional

class EmployeeForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[Optional()])
    hire_date = DateField('Hire Date', validators=[DataRequired()])
    department = StringField('Department', validators=[Optional()])
    position = StringField('Position', validators=[Optional()])
    salary = FloatField('Salary', validators=[Optional()])
    submit = SubmitField('Add Employee')

class JobForm(FlaskForm):
    title = StringField('Job Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Optional()])
    department = StringField('Department', validators=[Optional()])
    requirements = TextAreaField('Requirements', validators=[Optional()])
    submit = SubmitField('Post Job')

class ApplicationForm(FlaskForm):
    job_id = SelectField('Job', coerce=int, validators=[DataRequired()])
    applicant_name = StringField('Applicant Name', validators=[DataRequired()])
    applicant_email = StringField('Applicant Email', validators=[DataRequired(), Email()])
    resume = TextAreaField('Resume', validators=[Optional()])
    submit = SubmitField('Submit Application')

class PayrollForm(FlaskForm):
    employee_id = SelectField('Employee', coerce=int, validators=[DataRequired()])
    pay_period_start = DateField('Pay Period Start', validators=[DataRequired()])
    pay_period_end = DateField('Pay Period End', validators=[DataRequired()])
    hours_worked = FloatField('Hours Worked', validators=[DataRequired()])
    overtime_hours = FloatField('Overtime Hours', default=0)
    gross_pay = FloatField('Gross Pay', validators=[DataRequired()])
    deductions = FloatField('Deductions', default=0)
    submit = SubmitField('Process Payroll')

class BenefitForm(FlaskForm):
    name = StringField('Benefit Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Optional()])
    cost = FloatField('Cost', default=0)
    type = StringField('Type', validators=[Optional()])
    submit = SubmitField('Add Benefit')

class EmployeeBenefitForm(FlaskForm):
    employee_id = SelectField('Employee', coerce=int, validators=[DataRequired()])
    benefit_id = SelectField('Benefit', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Enroll Employee')

class PerformanceReviewForm(FlaskForm):
    employee_id = SelectField('Employee', coerce=int, validators=[DataRequired()])
    reviewer_id = SelectField('Reviewer', coerce=int, validators=[DataRequired()])
    review_date = DateField('Review Date', validators=[DataRequired()])
    rating = IntegerField('Rating (1-5)', validators=[DataRequired()])
    comments = TextAreaField('Comments', validators=[Optional()])
    goals = TextAreaField('Goals', validators=[Optional()])
    submit = SubmitField('Submit Review')

class CompensationForm(FlaskForm):
    employee_id = SelectField('Employee', coerce=int, validators=[DataRequired()])
    base_salary = FloatField('Base Salary', validators=[DataRequired()])
    bonuses = FloatField('Bonuses', default=0)
    equity = FloatField('Equity', default=0)
    submit = SubmitField('Update Compensation')