import pandas as pd
import numpy as np
import urllib
import os
import pickle

df = pd.read_csv("Batch_214780_batch_results-1.csv")

df = df.drop(['AutoApprovalDelayInSeconds','Expiration','NumberOfSimilarHITs','LifetimeInSeconds','WorkerId','AssignmentStatus','AcceptTime','SubmitTime','AutoApprovalTime','ApprovalTime','RejectionTime','RequesterFeedback','LifetimeApprovalRate','HITId','HITTypeId','Description','Reward',
            'CreationTime','Last30DaysApprovalRate','MaxAssignments','Answer.Tag1','WorkTimeInSeconds','Title','Keywords','AssignmentDurationInSeconds','RequesterAnnotation','Last7DaysApprovalRate',
            'Approve','Reject'], axis=1)

df.loc[df['Answer.Tag2'] == 4, 'Answer.Tag2'] = "extreme" 
df.loc[df['Answer.Tag2'] == 5, 'Answer.Tag2'] = "moderate" 
df.loc[df['Answer.Tag2'] == 6, 'Answer.Tag2'] = "minimal/none"
df.loc[df['Answer.Tag2'] == 7, 'Answer.Tag2'] =  "n/a"

pickle_file = []
if not os.path.exists("images"):
        os.makedirs("images")
for index, row in df.iterrows():
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

with open("pickle_file", 'wb') as handle:
        pickle.dump(pickle_file, handle, protocol=2)
    
