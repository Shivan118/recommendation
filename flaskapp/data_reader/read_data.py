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

class Data_Reader(object):
    def __init__(self):
        self.processLog = open(os.path.join(logPath, 'data_read_logs/Data_Read_Process_Log.txt'), 'a+')
        self.errorLog = open(os.path.join(logPath, 'data_read_logs/_Data_Read_Error_Log.txt'), 'a+')
        self.log_writer = logger.App_Logger()
        self.jobs_file = jobs_file
        self.profiles_file = profiles_file
        self.jobs = ''
        self.profiles = ''
        self.read_jobs()
        self.read_profiles()

    def read_jobs(self):
        self.jobs = pd.read_csv(self.jobs_file)
        self.jobs.drop(self.jobs.columns[self.jobs.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
        self.log_writer.log(self.processLog, 'Failed to read jobs data.')

    def read_profiles(self):
        self.profiles = pd.read_csv(self.profiles_file)
        self.profiles.drop(self.profiles.columns[self.profiles.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
        self.log_writer.log(self.processLog, 'Failed to read freelancers data.')

    def get_jobs(self):
        return self.jobs

    def get_profiles(self):
        return self.profiles

    def close_logs(self):
        self.processLog.close()
        self.errorLog.close()
    