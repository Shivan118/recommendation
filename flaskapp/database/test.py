
import pandas as pd 
from pprint import pprint
import csv
#from flaskapp.models import User, Job, Profile

'''
jobs_df = pd.read_csv('flaskapp/data/jobs.csv', 
                      converters={'Budget': eval, 'Link_of_quoters': eval, 'Link_of_premium_quoters': eval,
                                  'Link_of_invited_freelancers': eval, 'Link_of_hired_freelancers': eval})

profiles_df = pd.read_csv('flaskapp/data/profiles.csv', 
                        converters={'Hourly Rate':eval, 'Starting Rate':eval, 'Skills':eval})






with open('flaskapp/data/jobs.csv') as file:
    reader = csv.reader(file, delimiter=',')
    row_count = 0
    for row in reader:
        if row_count == 0:
            row_count += 1
        else:
            job = Job(date=row[1], user_id=row[3], title=row[6], description=row[9], skills=row[11], category=row[7], subcategory=row[8], payment_type=row[4], budget=row[5], links_quoters=row[15], links_invited=row[19], links_hired=row[21])
            
            name = row[10]
            firstname = name.split()[0]
            lastname = ' '.join(name.split()[1:])
            username = '-'.join([firstname, lastname.replace(' ', '-')]).lower()
            email = username+'@xyz.com'
            user = User(id=row[3], usertype='employer', firstname=firstname, lastname=lastname, username=username, email=email)
            
            row_count += 1


with open('flaskapp/data/profiles.csv') as file:
    reader = csv.reader(file, delimiter=',')
    row_count = 0
    for row in reader:
        if row_count == 0:
            row_count += 1
        else:
            profile = Profile(id=row[0], user_id=row[3], total_feedbacks=row[4], location=row[10], skills=row[17], rate_hourly=row[5], rate_starting=row[6], freelancer_type=row[7], member_since=row[16], rating=row[9], earnings_annual=row[11], earnings_alltime=row[12], transactions_completed=row[13])
            
            name = row[2]
            firstname = name.split()[0]
            lastname = ' '.join(name.split()[1:])
            username = '-'.join([firstname, lastname.replace(' ', '-')]).lower()
            email = username+'@xyz.com'
            user = User(id=row[3], usertype='freelancer', firstname=firstname, lastname=lastname, username=username, email=email)
            
            row_count += 1

'''


with open('flaskapp/data/profiles.csv') as file:
        reader = csv.reader(file, delimiter=',')
        row_count = 0
        for row in reader:
            if row_count == 0:
                for item in row:
                    print(item, row.index(item))
                row_count += 1