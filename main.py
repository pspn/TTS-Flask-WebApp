# app.py
from flask import Flask, request, render_template, redirect, url_for
from flask import send_file
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from flask_login import current_user
from werkzeug.security import check_password_hash, generate_password_hash
from forms import LoginForm
from utils import text_to_speech
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

# This would ideally be fetched from a database
users = [
    User(1, os.environ.get('USER_NAME'), generate_password_hash(os.environ.get('USER_PASS')))
]

@login_manager.user_loader
def load_user(user_id):
    return next((user for user in users if user.id == int(user_id)), None)

@app.route('/', methods=['GET'])
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    else:
        return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = next((user for user in users if user.username == form.username.data), None)
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/convert', methods=['POST'])
@login_required
def convert_text_to_speech():
    data = request.get_json()
    text = data['text']
    filename = text_to_speech(text)
    # Return the URL in the API response
    return {"result": "success", "filename": filename}


if __name__ == "__main__":
    app.run(port=5000)

