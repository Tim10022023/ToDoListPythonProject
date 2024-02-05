from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from flask_wtf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash
from models import db, Task, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eingaben.db'
app.config['SECRET_KEY'] = '123456789'
csrf = CSRFProtect(app)
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('homepage'))
        else:
            flash('Ungültiger Benutzername oder Passwort.')
    return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')

    if User.query.filter_by(username=username).first():
        # Benutzername bereits vergeben
        flash('Benutzername ist bereits vergeben.')
        return redirect(url_for('login'))

    new_user = User(username=username, password_hash=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()

    flash('Registrierung erfolgreich. Sie können sich jetzt anmelden.')
    return redirect(url_for('login'))


@app.route('/')
@login_required
def homepage():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', tasks=tasks)

@app.route('/popup', methods=['POST','GET'])
def popup():
    task_content=[]
    task_date=[]
    task_person=[]
    task_done=False
    if request.method == 'POST' and current_user.is_authenticated:
        task_content = request.form["content"]
        task_date = request.form["date"]
        task_person = request.form["person"]
        task_done = 'done' in request.form
        new_task = Task(content=task_content, date=task_date, person=task_person, done=task_done, user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        return "<script>window.opener.location.reload(); window.close();</script>"
    return render_template('popup.html')


@app.route('/delete_task', methods=['POST'])
def delete_task():
    task_ids = request.form.getlist('task_ids')
    for task_id in task_ids:
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
    db.session.commit()
    return redirect(url_for('homepage'))

@app.route('/update_task_status/<int:task_id>', methods=['POST'])
def update_task_status(task_id):
    data = request.get_json()
    task = Task.query.get_or_404(task_id)
    task.done = data['done']
    db.session.commit()
    return jsonify({'success': True}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) #wird benötigt damit man vom lokalen Netz zugreifen kann
    with app.app_context():
        db.create_all()
    app.run(debug=True)
