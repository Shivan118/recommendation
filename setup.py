from flaskapp import create_app, db


app = create_app()


def appSetup():   
    #create a new db
    print('Creating New Database')
    db.create_all(app=app)

    #populate the new empty db with the past csv data
    print('Populating the database with past data')
    from flaskapp.database.populate_db import PopulateDB
    with app.app_context():
        PopulateDB()
    

if __name__ == '__main__':
    appSetup()
    print('App setup complete. Run "python run.py" from your terminal to start the app')
