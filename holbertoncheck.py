#!/usr/bin/python3
import time
import requests
from getpass import getpass
import sys

"""
Getting your informations
"""
email = input("Enter your Holberton email: ")
print("-----------------------")
password = getpass("Enter your Holberton Password: ")
print("-----------------------")
api = input("Enter your Holberton api: ")
print("-----------------------")

"""
Getting the authentification token
"""
url = 'https://intranet.hbtn.io/users/auth_token.json'
myobj = {"api_key": api, "email": email, "password": password, "scope": "checker"}
x = requests.post(url, data=myobj)
xj = x.json()
try:
    xau = xj['auth_token']  #authentification key
    print("Authentification success!")
    print("-----------------------")
except:
    print("Make sure your email or password are correct")
    exit()



"""
Getting your project and the task informations
"""
pid = input("Enter the project ID: ")
print("-----------------------")
tnumber = input("Enter the number of the task you want to check: ")
print("-----------------------")


"""
Getting the Task Id 
"""
proj = requests.get('https://intranet.hbtn.io/projects/{}.json?auth_token={}'.format(pid, xau))
projj = proj.json()
tid = projj['tasks'][int(tnumber)]['id']    #task ID





"""
requesting a correction for The task
""" 
id = requests.post('https://intranet.hbtn.io/tasks/{}/start_correction.json?auth_token={}'.format(tid, xau))
corrid = id.json()
cid = corrid['id'] #Correction Id



"""
Waiting to load our correction
"""
l = "#"
p = 0
print("Correcting: {}".format(projj['name']))
print("-----------------------")
print("Task: {}".format(projj['tasks'][int(tnumber)]['title']))
print("-----------------------")
for i in range (10):
    l = l + "#"
    p = p + 10
    sys.stdout.write("\r" + '     | Loading {}'.format(l))
    sys.stdout.write("\r" + '{}%'.format(p))
    time.sleep(1.0)
print()



"""
Requestion our correction
"""
corr = requests.get('https://intranet.hbtn.io/correction_requests/{}.json?auth_token={}'.format(cid, xau))
c = corr.json()




"""
printing The result
"""
i = 0
checking = True
answer = ""
print("***********************")
try:
    while c['result_display']['checks'][i]:
        for key, value in (c['result_display']['checks'][i]).items():
            if key == 'passed':
                if value == True:
                    answer = "Success"
                else:
                    answer = "Fail"
                print("[{}] > {}".format(c['result_display']['checks'][i]['title'], answer))
                if value == False:
                    checking = False
        i = i + 1
except IndexError:
    pass
print("***********************")

if checking == True:
    print("[Congrats! You've done it!]") 
else:
    print('[Something is wrong... But never lose HOPE]')
    
