from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm, ReportForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = 'cQeThWmZq4t7w!z%C*F-JaNdRgUjXn2r5u8x/A?D(G+KbPeShVmYp3s6v9y$B&E)'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

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
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@reporting.com' and form.password.data == '123':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('report'))
        else:
            flash(f'Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)

@app.route("/report", methods=['GET', 'POST'])
def report():
    form = ReportForm()
    if form.validate_on_submit():
        flash(f'Report submitted for {form.category.data}!', 'success')
        return redirect(url_for('report'))
    return render_template('report.html', form=form)

@app.route("/reports")
def reports():
    return render_template('reports.html')

if __name__ == '__main__':
    app.run(debug=False)
