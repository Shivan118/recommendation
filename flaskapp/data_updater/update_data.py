from flaskapp.application_logging import logger
from flask import current_app
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

class Data_Updater(object):
    def __init__(self):
        self.processLog = open(os.path.join(logPath, 'data_read_logs/Data_Read_Process_Log.txt'), 'a+')
        self.errorLog = open(os.path.join(logPath, 'data_read_logs/_Data_Read_Error_Log.txt'), 'a+')
        self.log_writer = logger.App_Logger()
        self.jobs_file = jobs_file
        self.profiles_file = profiles_file
        self.jobs = ''
        self.profiles = ''

    def delete_job(self, job):
        self.jobs = pd.read_csv(self.jobs_file)
        print('jobid: ',job.id)
        index_todrop = self.jobs.loc[(self.jobs['Id']==job.id)].index[0]
        print('index: ',index_todrop)
        self.jobs = self.jobs.drop(index_todrop).copy().reset_index(drop=True)
        self.jobs.drop(self.jobs.columns[self.jobs.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
        self.jobs.to_csv(self.jobs_file, index=False)
        self.log_writer.log(self.processLog, 'Failed to read jobs data.')

    def delete_profile(self, profile):
        self.profiles = pd.read_csv(self.profiles_file)
        self.profiles = self.profiles.drop(self.profiles[self.profiles['Id'] == profile.id].index).copy().reset_index(drop=True)
        #self.profiles = self.profiles.drop(profile.id-1).copy().reset_index(drop=True)
        self.profiles.drop(self.profiles.columns[self.profiles.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
        self.profiles.to_csv(self.profiles_file, index=False)
        self.log_writer.log(self.processLog, 'Failed to read freelancers data.')

    def add_job(self, job):
        self.jobs = pd.read_csv(self.jobs_file)
        self.jobs = self.jobs.append({'Id':job.id, 'Created_date':job.date, 'User_id':job.user_id, 'Payment_type':job.payment_type, 'Budget':job.budget, 'Job_title':job.title, 'Category':job.category, 'Subcategory':job.subcategory, 'Job_description':job.description, 'Skills':job.skills, 'Link_of_quoters':job.links_quoters, 'Link_of_invited_freelancers':job.links_invited, 'Link_of_hired_freelancers':job.links_hired, 'Min_budget':job.min_budget, 'Job_cluster_id':job.job_cluster_id}, ignore_index=True)
        self.jobs['Id'] = (self.jobs.index.values+1)
        self.jobs.drop(self.jobs.columns[self.jobs.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
        self.jobs.to_csv(self.jobs_file, index=False)
        self.log_writer.log(self.processLog, 'Failed to read jobs data.')

    def add_profile(self, profile):
        self.profiles = pd.read_csv(self.profiles_file)
        self.profiles = self.profiles.append({'Id':profile.id, 'Freelancer Name':(profile.user.firstname+' '+profile.user.lastname), 'User Id':profile.user_id, 'Freelancer_Link':profile.link, 'Total_Feedback_Received':profile.total_feedbacks, 'Min_Hourly_Rate':profile.min_hourly_rate, 'Max_Hourly_Rate':profile.max_hourly_rate,'Min_Starting_Rate':profile.min_starting_rate, 'Max_Starting_Rate':profile.max_starting_rate, 'Rating':profile.rating, 'Location':profile.location, 'Annual Earnings':profile.earnings_annual, 'All-Time Earnings':profile.earnings_alltime, 'Transactions Completed':profile.transactions_completed, 'Member Since':profile.member_since, 'Skills':profile.skills, 'Average Earnings':profile.earnings_avg, 'Weighted_Rating':profile.weighted_rating, 'Profile Cluster Id':profile.profile_cluster_id}, ignore_index=True)
        self.profiles['Id'] = (self.profiles.index.values+1)
        self.profiles.drop(self.profiles.columns[self.profiles.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
        self.profiles.to_csv(self.profiles_file, index=False)
        self.log_writer.log(self.processLog, 'Failed to read freelancers data.')

    def update_job(self, job):
        self.jobs = pd.read_csv(self.jobs_file)
        index_toupdate = self.jobs.loc[(self.jobs['Id']==job.id)].index[0]
        #self.jobs = self.jobs.drop(job.id-1).copy().reset_index(drop=True)
        self.jobs.loc[index_toupdate] = pd.Series({'Id':job.id, 'Created_date':job.date, 'User_id':job.user_id, 'Payment_type':job.payment_type, 'Budget':job.budget, 'Job_title':job.title, 'Category':job.category, 'Subcategory':job.subcategory, 'Job_description':job.description, 'Skills':job.skills, 'Link_of_quoters':job.links_quoters, 'Link_of_invited_freelancers':job.links_invited, 'Link_of_hired_freelancers':job.links_hired, 'Min_budget':job.min_budget, 'Job_cluster_id':job.job_cluster_id})
        #self.jobs['Id'] = (self.jobs.index.values+1)
        self.jobs.drop(self.jobs.columns[self.jobs.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
        self.jobs.to_csv(self.jobs_file, index=False)
        self.log_writer.log(self.processLog, 'Failed to read jobs data.')

    def update_profile(self, profile):
        self.profiles = pd.read_csv(self.profiles_file)
        index_toupdate = self.profiles.loc[(self.profiles['Id']==profile.id)].index[0]
        #self.profiles = self.profiles.drop(profile.id-1).copy().reset_index(drop=True)
        self.profiles.loc[index_toupdate] = pd.Series({'Id':profile.id, 'Freelancer Name':(profile.user.firstname+' '+profile.user.lastname), 'User Id':profile.user_id, 'Freelancer_Link':profile.link, 'Total_Feedback_Received':profile.total_feedbacks, 'Min_Hourly_Rate':profile.min_hourly_rate, 'Max_Hourly_Rate':profile.max_hourly_rate,'Min_Starting_Rate':profile.min_starting_rate, 'Max_Starting_Rate':profile.max_starting_rate, 'Rating':profile.rating, 'Location':profile.location, 'Annual Earnings':profile.earnings_annual, 'All-Time Earnings':profile.earnings_alltime, 'Transactions Completed':profile.transactions_completed, 'Member Since':profile.member_since, 'Skills':profile.skills, 'Average Earnings':profile.earnings_avg, 'Weighted_Rating':profile.weighted_rating, 'Profile Cluster Id':profile.profile_cluster_id})
        #self.profiles['Id'] = (self.profiles.index.values+1)
        self.profiles.drop(self.profiles.columns[self.profiles.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
        self.profiles.to_csv(self.profiles_file, index=False)
        self.log_writer.log(self.processLog, 'Failed to read jobs data.')

    def close_logs(self):
        self.processLog.close()
        self.errorLog.close()

    def resetJobIds(self):
        self.jobs = pd.read_csv(self.jobs_file)
        self.jobs['Id'] = self.jobs.index.values+1
        self.jobs.to_csv(self.jobs_file, index=False)

    def resetProfileIds(self):
        self.profiles = pd.read_csv(self.profiles_file)
        self.profiles['Id'] = self.profiles.index.values+1
        self.profiles.to_csv(self.profiles_file, index=False)
    