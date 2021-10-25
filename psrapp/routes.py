from flask import render_template, url_for, flash, redirect
from psrapp import  app, db, bcrypt
from psrapp.forms import RegistrationForm, LoginForm, ReportForm
from psrapp.models import User, Report, Category
from flask_login import login_user, current_user, logout_user, login_required
from flask import request

posts = [
    {
        'category': 'Accident',
        'title': 'Pedestrian dies after being stuck by a vehicle',
        'content': 'Pedestrian dies after being stuck by a vehicle on dd/mm/yyyy. For more details, please visit: www....com.   ',
        'date_posted': 'October 15, 2021'
    },
    {
        'category': 'Update',
        'title': 'Bridge open to pedestrian traffic',
        'content': 'A new bridge open to pedestrian traffic on dd/mm/yyyy. For more details, please visit: www....com',
        'date_posted': 'October 16, 2021'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pwd= bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email= form.email.data, password= hashed_pwd)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}! Please log in', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('report'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('report'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')

@app.route("/report", methods=['GET', 'POST'])
@login_required
def report():
    form = ReportForm()
    if form.validate_on_submit():
        flash(f'Report submitted for {form.category.data}!', 'success')
        return redirect(url_for('report'))
    return render_template('report.html', form=form)


@app.route("/reports", methods=['GET', 'POST'])
@login_required
def reports():
    return render_template('reports.html')

