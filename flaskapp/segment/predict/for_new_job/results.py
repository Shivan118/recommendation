import numpy as np
import joblib, os, sys

fileDir = os.path.dirname(__file__)
#fileDir = os.path.join(fileDir,'..')
modelsPath = os.path.abspath(os.path.join(fileDir, 'models'))
#logPath = os.path.abspath(os.path.join(fileDir, 'logs'))
sys.path.insert(0, modelsPath)
#sys.path.insert(0,logPath)

scaler_file = os.path.join(modelsPath, 'jobsMinMaxScaler.pkl')
predictor_file = os.path.join(modelsPath, 'kmeans.pickle')


def predictSegment(minBudget, category):
    minBudget = float(minBudget)
    if category == 'Administrative & Secretarial':
        entry = np.array([minBudget, 0, 0, 0, 0, 0, 0, 0, 0, 0]).reshape(1, -1)
    elif category == 'Business & Finance':
        entry = np.array([minBudget, 1, 0, 0, 0, 0, 0, 0, 0, 0]).reshape(1, -1)
    elif category == 'Design & Art':
        entry = np.array([minBudget, 0, 1, 0, 0, 0, 0, 0, 0, 0]).reshape(1, -1)
    elif category == 'Education & Training':
        entry = np.array([minBudget, 0, 0, 1, 0, 0, 0, 0, 0, 0]).reshape(1, -1)
    elif category == 'Engineering & Architecture':
        entry = np.array([minBudget, 0, 0, 0, 1, 0, 0, 0, 0, 0]).reshape(1, -1)
    elif category == 'Legal':
        entry = np.array([minBudget, 0, 0, 0, 0, 1, 0, 0, 0, 0]).reshape(1, -1)
    elif category == 'Others':
        entry = np.array([minBudget, 0, 0, 0, 0, 0, 1, 0, 0, 0]).reshape(1, -1)
    elif category == 'Programming & Development':
        entry = np.array([minBudget, 0, 0, 0, 0, 0, 0, 1, 0, 0]).reshape(1, -1)
    elif category == 'Sales & Marketing':
        entry = np.array([minBudget, 0, 0, 0, 0, 0, 0, 0, 1, 0]).reshape(1, -1)
    elif category == 'Writing & Translation':
        entry = np.array([minBudget, 0, 0, 0, 0, 0, 0, 0, 0, 1]).reshape(1, -1)

    scaler = joblib.load(scaler_file)

    entry_scaled = scaler.transform(entry)

    predictor = joblib.load(predictor_file)

    job_cluster_id = (predictor.predict(entry_scaled))[0]

    return int(job_cluster_id)


    