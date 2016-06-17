from views import db, app



if __name__ == '__main__':
    db.create_all()
    app.run('0.0.0.0',8000,debug=True)