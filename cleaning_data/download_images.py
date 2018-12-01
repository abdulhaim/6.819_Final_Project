import pandas as pd
import numpy as np
import urllib
import os
import pickle

# Combining csv's 

df_1 = pd.read_csv("our_labelled_data_271.csv")
df_1 = df_1.drop(['AutoApprovalDelayInSeconds','Expiration','NumberOfSimilarHITs','LifetimeInSeconds','WorkerId','AssignmentStatus','AcceptTime','SubmitTime','AutoApprovalTime','ApprovalTime','RejectionTime','RequesterFeedback','LifetimeApprovalRate','HITId','HITTypeId','Description','Reward', 'CreationTime','Last30DaysApprovalRate','MaxAssignments','Answer.Tag1','WorkTimeInSeconds','Title','Keywords','AssignmentDurationInSeconds','RequesterAnnotation','Last7DaysApprovalRate','Approve','Reject'], axis=1)

df_1.loc[df_1['Answer.Tag2'] == 4, 'Answer.Tag2'] = "extreme" 
df_1.loc[df_1['Answer.Tag2'] == 5, 'Answer.Tag2'] = "moderate" 
df_1.loc[df_1['Answer.Tag2'] == 6, 'Answer.Tag2'] = "minimal"
df_1.loc[df_1['Answer.Tag2'] == 7, 'Answer.Tag2'] =  "not applicable"

pickle_file = []
if not os.path.exists("images"):
        os.makedirs("images")

df_2 = pd.read_csv("three_3002.csv")
df_2 = df_2.drop(['AutoApprovalDelayInSeconds','Expiration','NumberOfSimilarHITs','LifetimeInSeconds','WorkerId','AssignmentStatus','AcceptTime','SubmitTime','AutoApprovalTime','ApprovalTime','RejectionTime','RequesterFeedback','LifetimeApprovalRate','HITId','HITTypeId','Description','Reward', 'CreationTime','Last30DaysApprovalRate','MaxAssignments','WorkTimeInSeconds','Title','Keywords','AssignmentDurationInSeconds','RequesterAnnotation','Last7DaysApprovalRate','Approve','Reject'], axis=1)
df_2.fillna("not applicable", inplace=True)

for index, row in df_1.iterrows():
    directory = "images/" + row["Answer.Tag2"] 
    if not os.path.exists(directory):
        os.makedirs(directory)
    url = row['Input.image_url']
    name = directory + '/' +  row["AssignmentId"] + '.jpg'
    pickle_file.append([name,row["Answer.Tag2"]])
    try:
        urllib.request.urlretrieve(url, name)
    except urllib.error.HTTPError:
        continue

for index, row in df_2.iterrows():
    directory = "images/" + row["Answer.Tag2"] 
    if not os.path.exists(directory):
        os.makedirs(directory)
    url = row['Input.image_url']
    name = directory + '/' +  row["AssignmentId"] + '.jpg'
    pickle_file.append([name,row["Answer.Tag2"]])
    try:
        urllib.request.urlretrieve(url, name)
    except urllib.error.HTTPError:
        continue

with open("pickle_file.pkl", 'wb') as handle:
        pickle.dump(pickle_file, handle, protocol=2)
    
