import json
import requests
import datetime
from datetime import datetime as dt
from config import sfmcInfo

class auth_Mc:

"""Incomplete, shoud request and auth sfmc server-to-server integration"""
    
 def __init__(self):
     self.credentials = list()
     self.rest_url: str
     self.soap_url: str
     self.client_id = sfmcInfo.environmentVariables.client_id
     self.client_secret = sfmcInfo.environmentVariables.client_secret

 def auth_flow(self):
    self.response_list = list()
    self.payload = {
         "grant_type": 'client_credentials',
         "client_id": self.client_id,
         "client_secret": self.client_secret
    }


    self.auth_url = 'https://mch1y-pr7jgwjl1ypz3wtsswlq7q.auth.marketingcloudapis.com' + '/v2/token'
    self.header = {
            "Content-Type": "application/json"
        }
     
   
    self.request = requests.post(self.auth_url, headers=self.header, json=self.payload)
    self.response = self.request.json()

    if self.request.status_code == 200:
     
     self.expiration, self.rest_url, self.soap_url = (dt.today() + datetime.timedelta(seconds = self.response['expires_in'])).strftime('%Y-%m-%d %H:%M:%S'), self.response['rest_instance_url'] , self.response['soap_instance_url']

     self.credentials.extend([self.response['access_token'], self.expiration])
     self.response_list.extend([self.credentials,[self.rest_url,self.soap_url]])
     
    return self.response_list
        
 def refresh_token(self):
   if self.credentials[0][-1] <= dt.today().strftime('%Y-%m-%d %H:%M:%S'):
    
    self.construct = auth_Mc()
    self.refresh = self.construct.auth_flow()

    return self.refresh
   
   else:
    print('Token is valid!')
   return self.response_list
 
if __name__ == "__main__":
 auth_flow = auth_Mc()
 credentials = auth_flow.auth_flow()
 [print(i) for i in credentials]
 credentials = auth_flow.refresh_token()
 