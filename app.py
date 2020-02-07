#Read CVS into panda.
#sort randonly
# Dependencies
import requests
import json
from config import bootcampApiUser
from config import bootcampApiPassword

baseurlApiImport = 'https://bootcampspot.com/api/instructor/v1/'
postData ={'email': bootcampApiUser, 'password':bootcampApiPassword }

#df.sample(frac=1)
#df = df.sample(frac=1).reset_index(drop=True), in line sort.
#count pairs, number pairs.

#could Scrape this
#https://bootcampspot.com/students
#2233
#url = 'https://bootcampspot.com/api/instructor/v1/api/instructor/v1/'

def bootcampDF():
    r = requests.post(url = baseurlApiImport, data = postData)
    print(r.content)
    #https://bootcampspot.com/api/instructor/v1/api/instructor/v1/attendance
    #df=pd.read_json('https://api.coinmarketcap.com/v1/ticker/?limit=10')
    #df.head()


bootcampDF()
