from flaskapp.application_logging import logger
from flask import current_app
from flaskapp import db, bcrypt
from flaskapp.models import User, Job, Profile
import pandas as pd
import os, sys, csv
from dateutil.parser import parse
from pprint import pprint

fileDir = os.path.dirname(__file__)
fileDir = os.path.join(fileDir,'..')
dataPath = os.path.abspath(os.path.join(fileDir, 'data'))
logPath = os.path.abspath(os.path.join(fileDir, 'logs'))
sys.path.insert(0, dataPath)
sys.path.insert(0,logPath)

#rootPath = current_app.root_path
#dataPath = os.path.join(rootPath, 'data')
jobs_file = os.path.join(dataPath, 'jobs.csv')
profiles_file = os.path.join(dataPath, 'profiles.csv')

def PopulateDB():
    log_writer = logger.App_Logger()
    processLog = open(os.path.join(logPath, 'database_logs/Populate_DB_Process_Log.txt'), 'a+')
    
    with open(jobs_file) as file:
        print('Populating Jobs')
        reader = csv.reader(file, delimiter=',')
        row_count = 0
        for row in reader:
            if row_count == 0:
                row_count += 1
            else:
                job = Job(id=row[0], date=parse(row[1]), user_id=row[3], title=row[6], description=row[9], skills=row[11], category=row[7], subcategory=row[8], payment_type=row[4], budget=row[5], links_quoters=row[15], links_invited=row[19], links_hired=row[21], min_budget=row[23], job_cluster_id=row[22])
                db.session.add(job)

                name = row[10]
                firstname = name.split()[0]
                lastname = ' '.join(name.split()[1:])
                username = '-'.join([firstname, lastname.replace(' ', '-')]).lower() if lastname != '' else firstname.lower()
                email = username+'@xyz.com'

                user = User(id=row[3], usertype='employer', firstname=firstname, lastname=lastname, username=username, email=email)
                test_user = User.query.filter_by(id=row[3]).first()
                if not test_user:
                    db.session.add(user)

                db.session.commit()
                row_count += 1
        
        print('Jobs Populated Successfully')
        log_writer.log(processLog, 'Jobs Populated Successfully')

    with open(profiles_file) as file:
        print('Populating Freelancer Profiles')
        reader = csv.reader(file, delimiter=',')
        row_count = 0
        for row in reader:
            if row_count == 0:
                row_count += 1
            else:
                profile = Profile(id=row[0], user_id=row[3], total_feedbacks=row[4], location=row[10], min_hourly_rate=row[20], max_hourly_rate=row[21], min_starting_rate=row[18], max_starting_rate=row[19], member_since=row[16], rating=row[9], earnings_annual=row[11], earnings_alltime=row[12], earnings_avg=row[17], transactions_completed=row[13], weighted_rating=row[22], profile_cluster_id=row[23], skills=row[24])
                db.session.add(profile)

                name = row[2]
                firstname = name.split()[0]
                lastname = ' '.join(name.split()[1:])
                username = '-'.join([firstname, lastname.replace(' ', '-')]).lower() if lastname != '' else firstname.lower()
                email = username+'@xyz.com'

                user = User(id=row[3], usertype='freelancer', firstname=firstname, lastname=lastname, username=username, email=email)
                
                test_user = User.query.filter_by(id=row[3]).first()
                if not test_user:
                    db.session.add(user)
                
                db.session.commit()
                row_count += 1
        
        print('Freelancer Profiles Populated Successfully')
        log_writer.log(processLog, 'Profiles Populated Successfully')

    print('Hashing User Passwords. This may take some time. Do not abort')
    users = User.query.all()
    for user in users:
        hashed_password = bcrypt.generate_password_hash(user.password).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
    print('All Passwords Hashed')
    log_writer.log(processLog, 'All Passwords Hashed')
    print('Database Populated Successfully')
    log_writer.log(processLog, 'Database Populated Successfully')

    processLog.close()