from google.cloud import bigquery
from google.oauth2 import service_account
# from flask import Flask, render_template, request, redirect

import string

import random

# def biggquery():
#     credentials = service_account.Credentials.from_service_account_file(
#         'JSONKEY.json')
#     project_id = 'instant-binder-251011'
#     client = bigquery.Client(credentials=credentials, project=project_id)
#     query_job = client.query(
#         """SELECT * FROM QUICK_LEARN.User_info_from_app LIMIT 1000""")
#     results = query_job.result()
#     return results


# def signed():
#     global user_id
#     results = biggquery()
#     for row in results:
#         user_id1 = int(row['User_id'])
#         # if ((row['Email'] == email1) and (row['VERIFIED'] == 'YES')):
#         if ((row['Email'] == "raymanjungle4@gmail.com")):
#             user_id = int(row['User_id'])
#             print(user_id1)
#             exit()
#     user_id = user_id1 + 1
#     credentials = service_account.Credentials.from_service_account_file(
#             'JSONKEY.json')
#     project_id = 'instant-binder-251011'
#     client = bigquery.Client(credentials=credentials, project=project_id)
#     query_job = client.query(
#         """INSERT INTO QUICK_LEARN.User_info_from_app(User_id, Email, Password)
#         VALUES ({},'templark4@gmail.com','Templark4')""".format(user_id))
#     print(user_id)


# signed()

# credentials = service_account.Credentials.from_service_account_file(
#     'JSONKEY.json')
# project_id = 'instant-binder-251011'
# client = bigquery.Client(credentials=credentials, project=project_id)
# for i in range(21,22):    
#     d = random.randint(1, 10)
#     query_job = client.query(
#         """UPDATE QUICK_LEARN.User_Information SET Assessment_score = {} WHERE user_id = {} """.format(d , i))

credentials = service_account.Credentials.from_service_account_file(
    'JSONKEY.json')
project_id = 'instant-binder-251011'
client = bigquery.Client(credentials=credentials, project=project_id)
for i in range(1,22):
    query_job = client.query(
        """UPDATE QUICK_LEARN.User_Information SET Assessment_score = {} WHERE user_id = {} """.format(d , i))