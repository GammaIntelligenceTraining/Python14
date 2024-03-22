from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
import hashlib
from datetime import timedelta, datetime

app = Flask(__name__)
app.secret_key = 'hello world'
app.permanent_session_lifetime = timedelta(minutes=30)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost/flask_python14'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):

    _id = db.Column('id', db.Integer, primary_key=True)
    login = db.Column('login', db.String(20))
    password = db.Column('password', db.String(32))
    email = db.Column('email', db.String(100))

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email


class Post(db.Model):
    _id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String(50))
    content = db.Column('content', db.String(1000))
    owner = db.Column('owner', db.String(20))
    date_added = db.Column('date_added', db.DateTime())

    def __init__(self, title, content, owner):
        self.title = title
        self.content = content
        self.owner = owner
        self.date_added = datetime.now()


@app.route('/')
def home():
    posts = Post.query.order_by(desc('date_added')).all()
    return render_template('home.html', posts=posts)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user_login = request.form['user-login']
        password = hashlib.md5(request.form['user-password'].encode()).hexdigest()
        user_in_db = User.query.filter_by(login=user_login).first()
        if user_in_db:
            if password == user_in_db.password:
                session['login'] = user_login
                session['email'] = user_in_db.email
                flash('Logged in', 'success')
                return redirect(url_for('user'))
            else:
                flash('Incorrect password', 'danger')
                return redirect(url_for('login'))
        else:
            new_user = User(user_login, password, '')
            db.session.add(new_user)
            db.session.commit()
            session['login'] = user_login
            session['email'] = new_user.email
            flash('User created', 'success')
            return redirect(url_for('user'))
    else:
        if 'login' in session:
            flash('Already logged in', 'info')
            return redirect(url_for('user'))
        else:
            return render_template('login.html')


@app.route('/user/', methods=['GET', 'POST'])
def user():
    if 'login' in session:
        user_login = session['login']
        if request.method == 'POST':
            user_email = request.form['user-email']
            user_in_db = User.query.filter_by(login=user_login).first()
            user_in_db.email = user_email
            db.session.commit()
            session['email'] = user_email
            flash('Email saved', 'success')
        return render_template('user.html', user_email=session['email'])
    else:
        flash('You are not logged in', 'danger')
        return redirect(url_for('login'))


@app.route('/logout/')
def logout():
    session.pop('login', None)
    session.pop('email', None)
    flash('Logged out', 'success')
    return redirect(url_for('login'))


@app.route('/delete/')
def delete():
    user_login = session['login']
    User.query.filter_by(login=user_login).delete()
    db.session.commit()
    session.pop('login', None)
    session.pop('email', None)
    flash('Account was deleted', 'info')
    return redirect(url_for('login'))


@app.route('/post/', methods=['GET', 'POST'])
def post():
    if 'login' in session:
        if request.method == 'POST':
            title = request.form['post-title']
            content = request.form['post-content']
            owner = session['login']
            new_post = Post(title, content, owner)
            db.session.add(new_post)
            db.session.commit()
            flash('Post was saved', 'success')
            return redirect(url_for('post'))
        else:
            return render_template('post.html')
    else:
        return redirect(url_for('login'))


@app.route('/my_posts/')
def my_posts():
    if 'login' in session:
        posts = Post.query.filter_by(owner=session['login']).order_by(desc('date_added'))
        return render_template('my_posts.html', posts=posts)
    else:
        flash('You are not logged in', 'warning')
        return redirect(url_for('login'))


@app.route('/delete_post/<post_id>')
def delete_post(post_id):
    Post.query.filter_by(_id=post_id).delete()
    db.session.commit()
    flash('Post was deleted', 'info')
    return redirect(url_for('my_posts'))


@app.route('/admin/')
def admin():
    return redirect(url_for('user', name='Admin'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)