from database_todo import User, db, app, Task, Completed_task
from flask import render_template,request
import time


@app.route('/', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        _username = request.form['username']
        _password = request.form['password']
        old_user = User.query.filter_by(username= _username).first()
        if old_user == None:
            new_user = User(_username, _password)
            db.session.add(new_user)
            db.session.commit()
            return render_template('user_page.html', _Completed_task=Completed_task.query.filter(Completed_task.date == time.strftime("%Y-%m-%d")).all(),
                                    todays_task=Task.query.filter(Task.date == time.strftime("%Y-%m-%d")).all(),
                                    upcomings=Task.query.filter(Task.date != time.strftime("%Y-%m-%d")).all())
        else:
            old_user_password = old_user.password
            print old_user.id
            if old_user_password == _password:
               # today=Task.query.filter_by(date=)
               return render_template('user_page.html', _Completed_task=Completed_task.query.filter(Completed_task.date == time.strftime("%Y-%m-%d")).all(),
                                       todays_task=Task.query.filter(Task.date == time.strftime("%Y-%m-%d")).all(),
                                       upcomings=Task.query.filter(Task.date != time.strftime("%Y-%m-%d")).all())
            else:
                return render_template('login.html',message='Login Incorret please retry')
    return render_template('login.html', message = 'welcome')

@app.route('/user', methods=['POST','GET'])
def _user():
    if request.method == 'POST':
        new_task=request.form['new_task']
        date_dt =  request.form['dt']
        if len(new_task) > 0:
            if len(date_dt) > 0:

                _task = Task(new_task,date_dt)

                db.session.add(_task)
                db.session.commit()

        return render_template('user_page.html', _Completed_task=Completed_task.query.filter(Completed_task.date == time.strftime("%Y-%m-%d")).all(), todays_task=Task.query.filter( Task.date == time.strftime("%Y-%m-%d")).all(), upcomings=Task.query.filter( Task.date != time.strftime("%Y-%m-%d")).all())

    return render_template('user_page.html', _Completed_task=Completed_task.query.filter(Completed_task.date == time.strftime("%Y-%m-%d")).all(),
                           todays_task=Task.query.filter(Task.date == time.strftime("%Y-%m-%d")).all(),
                           upcomings=Task.query.filter(Task.date != time.strftime("%Y-%m-%d")).all())


@app.route('/completion', methods=['POST','GET'])
def _task_comp():
    if request.method == 'POST':
        checking = request.form['task_completion']
        removing = Task.query.filter(Task.id == int(checking)).first()
        __complete_task = Completed_task(removing.Task_event, removing.date)

        db.session.add(__complete_task)
        db.session.commit()
        db.session.delete(removing)
        db.session.commit()
        return render_template('user_page.html', _Completed_task=Completed_task.query.filter(Completed_task.date == time.strftime("%Y-%m-%d")).all(), todays_task=Task.query.filter( Task.date == time.strftime("%Y-%m-%d")).all(), upcomings=Task.query.filter( Task.date != time.strftime("%Y-%m-%d")).all())
    return render_template('user_page.html',
                           _Completed_task=Completed_task.query.filter(Completed_task.date == time.strftime("%Y-%m-%d")).all(),
                           todays_task=Task.query.filter(Task.date == time.strftime("%Y-%m-%d")).all(),
                           upcomings=Task.query.filter(Task.date != time.strftime("%Y-%m-%d")).all())
