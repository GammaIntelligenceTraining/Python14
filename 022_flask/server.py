from flask import Flask, redirect, url_for, render_template, request, session
import hashlib
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'hello world'
app.permanent_session_lifetime = timedelta(minutes=30)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user_login = request.form['user-login']
        password = hashlib.md5(request.form['user-password'].encode()).hexdigest()
        session['login'] = user_login
        return redirect(url_for('user'))
    else:
        if 'login' in session:
            return redirect(url_for('user'))
        return render_template('login.html')



@app.route('/user/')
def user():
    if 'login' in session:
        user_login = session['login']
        return f'<h2>Hello {user_login}!</h2>'
    else:
        return redirect(url_for('login'))


@app.route('/logout/')
def logout():
    session.pop('login', None)
    return redirect(url_for('login'))

@app.route('/admin/')
def admin():
    return redirect(url_for('user', name='Admin'))

if __name__ == '__main__':
    app.run(debug=True)