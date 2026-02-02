from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from models import db, Employee, Job, Application, Payroll, Benefit, EmployeeBenefit, PerformanceReview, Compensation
from forms import EmployeeForm, JobForm, ApplicationForm, PayrollForm, BenefitForm, EmployeeBenefitForm, PerformanceReviewForm, CompensationForm

main = Blueprint('main', __name__)

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    return render_template('index.html')

@main.route('/employees')
@login_required
def employees():
    employees = Employee.query.all()
    return render_template('employees.html', employees=employees)

@main.route('/jobs')
@login_required
def jobs():
    jobs = Job.query.all()
    return render_template('jobs.html', jobs=jobs)

@main.route('/applications')
@login_required
def applications():
    applications = Application.query.all()
    return render_template('applications.html', applications=applications)

@main.route('/payroll')
@login_required
def payroll():
    payrolls = Payroll.query.all()
    return render_template('payroll.html', payrolls=payrolls)

@main.route('/benefits')
@login_required
def benefits():
    benefits = Benefit.query.all()
    return render_template('benefits.html', benefits=benefits)

@main.route('/performance')
@login_required
def performance():
    reviews = PerformanceReview.query.all()
    return render_template('performance.html', reviews=reviews)

@main.route('/compensation')
@login_required
def compensation():
    compensations = Compensation.query.all()
    return render_template('compensation.html', compensations=compensations)

@main.route('/employees/add', methods=['GET', 'POST'])
@login_required
def add_employee():
    form = EmployeeForm()
    if form.validate_on_submit():
        employee = Employee(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            phone=form.phone.data,
            hire_date=form.hire_date.data,
            department=form.department.data,
            position=form.position.data,
            salary=form.salary.data
        )
        db.session.add(employee)
        db.session.commit()
        flash('Employee added successfully!')
        return redirect(url_for('main.employees'))
    return render_template('add_employee.html', form=form)

@main.route('/jobs/add', methods=['GET', 'POST'])
@login_required
def add_job():
    form = JobForm()
    if form.validate_on_submit():
        job = Job(
            title=form.title.data,
            description=form.description.data,
            department=form.department.data,
            requirements=form.requirements.data
        )
        db.session.add(job)
        db.session.commit()
        flash('Job posted successfully!')
        return redirect(url_for('main.jobs'))
    return render_template('add_job.html', form=form)

@main.route('/applications/add', methods=['GET', 'POST'])
@login_required
def add_application():
    form = ApplicationForm()
    form.job_id.choices = [(j.id, j.title) for j in Job.query.all()]
    if form.validate_on_submit():
        application = Application(
            job_id=form.job_id.data,
            applicant_name=form.applicant_name.data,
            applicant_email=form.applicant_email.data,
            resume=form.resume.data
        )
        db.session.add(application)
        db.session.commit()
        flash('Application submitted successfully!')
        return redirect(url_for('main.applications'))
    return render_template('add_application.html', form=form)

@main.route('/payroll/add', methods=['GET', 'POST'])
@login_required
def add_payroll():
    form = PayrollForm()
    form.employee_id.choices = [(e.id, f"{e.first_name} {e.last_name}") for e in Employee.query.all()]
    if form.validate_on_submit():
        payroll = Payroll(
            employee_id=form.employee_id.data,
            pay_period_start=form.pay_period_start.data,
            pay_period_end=form.pay_period_end.data,
            hours_worked=form.hours_worked.data,
            overtime_hours=form.overtime_hours.data,
            gross_pay=form.gross_pay.data,
            deductions=form.deductions.data,
            net_pay=form.gross_pay.data - form.deductions.data
        )
        db.session.add(payroll)
        db.session.commit()
        flash('Payroll processed successfully!')
        return redirect(url_for('main.payroll'))
    return render_template('add_payroll.html', form=form)

@main.route('/benefits/add', methods=['GET', 'POST'])
@login_required
def add_benefit():
    form = BenefitForm()
    if form.validate_on_submit():
        benefit = Benefit(
            name=form.name.data,
            description=form.description.data,
            cost=form.cost.data,
            type=form.type.data
        )
        db.session.add(benefit)
        db.session.commit()
        flash('Benefit added successfully!')
        return redirect(url_for('main.benefits'))
    return render_template('add_benefit.html', form=form)

@main.route('/benefits/enroll', methods=['GET', 'POST'])
@login_required
def enroll_benefit():
    form = EmployeeBenefitForm()
    form.employee_id.choices = [(e.id, f"{e.first_name} {e.last_name}") for e in Employee.query.all()]
    form.benefit_id.choices = [(b.id, b.name) for b in Benefit.query.all()]
    if form.validate_on_submit():
        enrollment = EmployeeBenefit(
            employee_id=form.employee_id.data,
            benefit_id=form.benefit_id.data
        )
        db.session.add(enrollment)
        db.session.commit()
        flash('Employee enrolled in benefit successfully!')
        return redirect(url_for('main.benefits'))
    return render_template('enroll_benefit.html', form=form)

@main.route('/performance/add', methods=['GET', 'POST'])
@login_required
def add_performance():
    form = PerformanceReviewForm()
    form.employee_id.choices = [(e.id, f"{e.first_name} {e.last_name}") for e in Employee.query.all()]
    form.reviewer_id.choices = [(e.id, f"{e.first_name} {e.last_name}") for e in Employee.query.all()]
    if form.validate_on_submit():
        review = PerformanceReview(
            employee_id=form.employee_id.data,
            reviewer_id=form.reviewer_id.data,
            review_date=form.review_date.data,
            rating=form.rating.data,
            comments=form.comments.data,
            goals=form.goals.data
        )
        db.session.add(review)
        db.session.commit()
        flash('Performance review added successfully!')
        return redirect(url_for('main.performance'))
    return render_template('add_performance.html', form=form)

@main.route('/compensation/add', methods=['GET', 'POST'])
@login_required
def add_compensation():
    form = CompensationForm()
    form.employee_id.choices = [(e.id, f"{e.first_name} {e.last_name}") for e in Employee.query.all()]
    if form.validate_on_submit():
        compensation = Compensation(
            employee_id=form.employee_id.data,
            base_salary=form.base_salary.data,
            bonuses=form.bonuses.data,
            equity=form.equity.data
        )
        db.session.add(compensation)
        db.session.commit()
        flash('Compensation updated successfully!')
        return redirect(url_for('main.compensation'))
    return render_template('add_compensation.html', form=form)