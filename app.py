from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eingaben.db'

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(255), nullable=False)
    date = db.Column(db.String(255), nullable=False)
    person = db.Column(db.String(255), nullable=False)
    #done = db.Column(db.Boolean, default=False)

@app.route('/')
def homepage():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/popup', methods=['POST','GET'])
def popup():
    task_content=[]
    task_date=""
    task_person=""
    #task_done=False
    if request.method == 'POST':
        task_content = request.form["content"]
        task_date = request.form["date"]
        task_person = request.form["person"]
        # task_done = request.form["done"]

        new_task = Task(content=task_content, date=task_date, person=task_person) #done=task_done)
        db.session.add(new_task)
        db.session.commit()

    return render_template('popup.html', task_content=task_content, task_date=task_date,task_person=task_person) #task_done=task_done)



@app.route('/delete_task', methods=['POST'])
def delete_task():
    task_ids = request.form.getlist('task_ids')
    for task_id in task_ids:
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
    db.session.commit()
    return redirect(url_for('homepage'))

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=5000) #wird benötigt damit man vom lokalen Netz zugreifen kann
    with app.app_context():
        db.create_all()
    app.run(debug=True)
