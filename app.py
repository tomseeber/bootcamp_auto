#Read CVS into panda.
#sort randonly
# Dependencies
import requests
import json
from config import bootcampApiUser
from config import bootcampApiPassword
#from config import authCode
#from config import courseID
#from config import baseurl

postData ={'Content-Type':'json','email': bootcampApiUser, 'password':bootcampApiPassword}
loginRoute = 'login/'
atttendanceRoute = 'attendance/'


#df.sample(frac=1)
#df = df.sample(frac=1).reset_index(drop=True), in line sort.
#count pairs, number pairs.

#could Scrape this
#https://bootcampspot.com/students
#2233
baseurl = 'https://bootcampspot.com/api/instructor/v1/api/instructor/v1/'

def bootcampDF():
    loginurl = baseurl + loginRoute
    #print(loginurl)
    headers = {'Content-Type':'application/json'}
    r = requests.post(url = loginurl, data = postData, headers=headers)
    
    print(r.request.headers['Content-Type'])
    
    #headers = {'Content-Type': 'application/json', 'authToken':authCode}
    #attendancePostData = {'courseId': courseID}
    #attendanceUrl = baseurl + atttendanceRoute
    #r2 = requests.post(url = attendanceUrl, data = attendancePostData, headers = headers)
    #https://bootcampspot.com/api/instructor/v1/api/instructor/v1/attendance
    #df=pd.read_json('https://api.coinmarketcap.com/v1/ticker/?limit=10')
    #df.head()

    #print(r2.request.headers['Content-Type'])
    #print(r2.content)
    #bootcampDF = requests.get()

def randomizeDF(df):
    df = df.sample(frac=1).reset_index(drop=True)
    #for person in df


bootcampDF()
