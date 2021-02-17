from flaskapp.application_logging import logger
from flask import current_app
from flaskapp import db
from flaskapp.models import Job, Profile, User
import pandas as pd
import os, sys

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

class DB_Reader(object):
    def __init__(self):
        self.processLog = open(os.path.join(logPath, 'data_read_logs/Data_Read_Process_Log.txt'), 'a+')
        self.errorLog = open(os.path.join(logPath, 'data_read_logs/_Data_Read_Error_Log.txt'), 'a+')
        self.log_writer = logger.App_Logger()
        self.jobs_file = jobs_file
        self.profiles_file = profiles_file
        self.jobs_csv = ''
        self.profiles_csv = ''
        self.jobs_db = ''
        self.profiles_db = ''
        self.jobs = ''
        self.profiles = ''
        self.read_jobs()
        self.read_profiles()

    def read_jobs(self):
        self.jobs_csv = pd.read_csv(self.jobs_file,
                           converters={'Budget': eval, 'Link_of_quoters': eval, 'Link_of_premium_quoters': eval,
                                       'Link_of_invited_freelancers': eval, 'Link_of_hired_freelancers': eval})
        new_cols = list(self.jobs_csv.drop(['Unnamed: 0', 'Due_date', 'Name_of_employer', 'Link_of_employer', 'Employer_id', 'No_of_quotes', 'No_of_Premium_quotes', 'Link_of_premium_quoters', 'No_of_inviited', 'No_of_Hired'], axis=1).columns) + ['Min_budget', 'Job_cluster_id']
        del self.jobs_csv
        self.jobs = pd.DataFrame(columns = new_cols)

        self.jobs_db = Job.query.all()
        for job in self.jobs_db:
            self.jobs.append({'Id':job.id, 'Created_date':job.date, 'User_id':job.user_id, 'Payment_type':job.payment_type, 'Budget':job.budget, 'Job_title':job.title, 'Category':job.category, 'Subcategory':job.subcategory, 'Job_description':job.description, 'Skills':job.skills, 'Link_of_quoters':job.links_quoters, 'Link_of_invited_freelancers':job.links_invited, 'Link_of_hired_freelancers':job.links_hired, 'Min_budget':job.min_budget, 'Job_cluster_id':job.job_cluster_id}, ignore_index=True)
        del self.jobs_db
        self.log_writer.log(self.processLog, 'Failed to read jobs data.')

    def read_profiles(self):
        self.profiles_csv = pd.read_csv(self.profiles_file, converters={'Hourly Rate':eval, 'Starting Rate':eval, 'Skills':eval})
        new_columns = list(profiles.drop(['Freelancer Name', 'Freelancer Type', 'Member', 'Employers', 'Largest Employer'], axis=1).columns) + ['Average Earnings', 'Profile Cluster Id']
        del self.profiles.csv
        self.profiles = pd.DataFrame(columns = new_columns)

        self.profiles_db = Profile.query.all()
        for profile in self.profiles_db:
            self.profiles.append({'Id':profile.id, 'Freelancer_Link':profile.link, 'User_id':profile.user_id, 'Total_Feedback_Received':profile.total_feedbacks, 'Hourly Rate':profile.rate_hourly, 'Starting Rate':profile.rate_starting, 'Rating':profile.rating, 'Location':profile.location, 'Annual Earnings':profile.earnings_annual, 'All-Time Earnings':profile.earnings_alltime, 'Transactions Completed':profile.transactions_completed, 'Member Since':profile.member_since, 'Skills':profile.skills, 'Average Earnings':profile.earnings_avg, 'Profile Cluster Id':profile.profile_cluster_id}, ignore_index=True)
        del self.jobs_db
        self.log_writer.log(self.processLog, 'Failed to read freelancers data.')

    def get_jobs(self):
        return self.jobs

    def get_profiles(self):
        return self.profiles

    def close_logs(self):
        self.processLog.close()
        self.errorLog.close()