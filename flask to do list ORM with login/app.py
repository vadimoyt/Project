from flask_login import LoginManager, login_user, login_required, UserMixin, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from webbrowser import Error
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import sessionmaker
from werkzeug.utils import secure_filename
import os


DATABASE_URL = "postgresql://postgres:postgres@localhost/lesson_14"

engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
app.config['SECRET_KEY'] = 'your_secret_key'

class Users(Base, UserMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password_hash = Column(String(255), nullable=False)

    tasks = relationship("Tasks", back_populates="user", cascade="all, delete-orphan")

class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    category = Column(String(50))
    title = Column(String(50))
    description = Column(String)
    status = Column(String(50))
    created_at = Column(DATETIME)
    dead_line = Column(DATETIME)
    file_path = Column(String(255))
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("Users", back_populates="tasks")

@login_manager.user_loader
def load_user(user_id):
    return session.query(Users).get(int(user_id))

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email_or_username = request.form.get('username')
        password = request.form.get('password')
        user = session.query(Users).filter((Users.email == email_or_username) | (Users.username == email_or_username)).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('home_page'))
        else:
            flash('User not found. Please try again', 'danger')
            return redirect(url_for('login'))
    return render_template('/login.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        new_username = request.form.get('username')
        new_email = request.form.get('email')
        new_password = request.form.get('password')
        hashed_password = generate_password_hash(new_password, method='pbkdf2:sha256')
        new_user = Users(
            username=new_username,
            email=new_email,
            password_hash=hashed_password
        )
        session.add(new_user)
        session.commit()
        return redirect(url_for('login'))
    return render_template('/register.html')

@app.route('/')
@login_required
def home_page():
    user_name = current_user.username
    user_id = current_user.id
    tasks = session.query(Tasks).filter_by(user_id=user_id).all()
    return render_template('index.html', tasks=tasks, user_name=user_name)

@app.route('/sorted')
def sorted_by_category():
    user_name = current_user.username
    selected_category = request.args.get('category')
    user_id = current_user.id
    if selected_category:
        tasks = session.query(Tasks).filter_by(category=selected_category, user_id=user_id).all()
    else:
        tasks = session.query(Tasks).all()
    return render_template('index.html', tasks=tasks, user_name=user_name)

@login_required
@app.route('/add_task', methods=['POST', 'GET'])
def add_task():
    if request.method == 'POST':
        try:
            selected_category = request.form.get('category')
            selected_title = request.form.get('title')
            selected_description = request.form.get('description')
            selected_status = request.form.get('status')
            selected_dead_line = request.form.get('dead_line')
            selected_file = request.files.get('file')
            file_path = None
            if selected_file:
                file_name = secure_filename(selected_file.filename)
                selected_file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
                file_path = file_name

            new_task = Tasks(
                category=selected_category,
                title=selected_title,
                description=selected_description,
                status=selected_status,
                dead_line=selected_dead_line,
                file_path=file_path,
                user_id=current_user.id
            )
            session.add(new_task)
            session.commit()
            return redirect(url_for('success'))
        except Error as e:
            return f"Error, {e}"
    return render_template('add_task.html')

@app.route('/success', methods=['GET'])
def success():
    return render_template('success.html')

@app.route('/delete', methods=['POST'])
def delete_task():
    selected_task = request.form.get('task_id')
    task = session.query(Tasks).get(selected_task)
    if task:
        session.delete(task)
        session.commit()
    return redirect(url_for('home_page'))

@app.route('/task')
def open_task():
    selected_task = request.args.get('task_id')
    task = session.query(Tasks).filter_by(id=selected_task).one()
    return render_template('task.html', task=task)

@app.route('/update_task', methods=['POST', 'GET'])
def update_task():
    if request.method == 'GET':
        selected_task = request.args.get('task_id')
        task = session.query(Tasks).filter_by(id=selected_task).one()
        return render_template('update_task.html', task=task)
    else:
        task_id = request.form.get('id')
        field_name = request.form.get('field')
        new_value = request.form.get('new_value')
        task = session.query(Tasks).get(task_id)
        if task:
            setattr(task, field_name, new_value)
            session.commit()
        return render_template('update_task.html', task=task)


@app.route('/update_task_field')
def update_task_field():
    field_name = request.args.get('field')
    task_id = request.args.get('id')
    return render_template('/update_task_field.html', field_name=field_name, id=task_id)

@app.route('/uploads/<file_name>')
def uploaded_file(file_name):
    return send_from_directory(app.config['UPLOAD_FOLDER'], file_name, as_attachment=True)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home_page'))


if __name__ == '__main__':
    app.run(debug=True, port=5001)
