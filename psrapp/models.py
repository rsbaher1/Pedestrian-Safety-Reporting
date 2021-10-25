from psrapp import app, db, login_manager
from datetime import datetime
from flask_login import UserMixin



@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(int(user_id))
    except SQLAlchemyError as e:
        flask.flash(
            "Please report this error to the admin", "error" ,"error")


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    reports = db.relationship('Report', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"



class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    attachment = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    def __repr__(self):
        return f"Report('{self.title}', '{self.date_posted}')"


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    reports_c = db.relationship('Report', backref='reports_c', lazy=True)
    def __repr__(self):
        return f"Category('{self.id}', '{self.title}')"

db.create_all()
db.session.commit()








