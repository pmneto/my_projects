import json
import requests
import sys
from datetime import datetime as dt
from collections import ChainMap

class sfmc_Requests:
 
 """Incomplete, should make API Calls to request data from SFMC"""

 def __init__(self,de_customerkey,rest_url,soap_url,credentials):
  self.de_customerkey, self.rest_url, self.soap_url, self.credentials = de_customerkey, rest_url, soap_url, credentials
  self.page = 1
  
  self.header =  {
    'Content-type': 'application/json',
    'Authorization': 'Bearer ' + self.credentials[0]
    }
  
  

 def get_DE(self, page=1):
  
  self.url_requested = self.rest_url + 'data/v1/customobjectdata/key/DE_EXTERNAL_KEY/rowset'.replace('DE_EXTERNAL_KEY', self.de_customerkey)
 
  if (self.credentials[-1] > dt.today().strftime('%Y-%m-%d %H:%M:%S')) == True:
   request = requests.get(self.url_requested + f'?page={page}', headers = self.header)
   return request.json()
  else:
   return 'Token Expired'
    
 def formDEContent(self, de_requested = None):
  
  self.construct = sfmc_Requests(self.de_customerkey, self.rest_url, self.soap_url, self.credentials)
  self.requestDe = self.construct.get_DE()
  self.json_file = self.requestDe
  
  if self.requestDe['count'] >= 2500:
  
   self.pages = self.requestDe['count']/2500
  
   while(self.page<=self.pages):
    sys.stdout.write(f'Im requestin page :  {self.page}\n')
    self.requestDe = self.construct.get_DE(self.page)
    self.json_file =  ChainMap(self.json_file,self.requestDe)
    print(len(self.json_file))
    #sys.stdout.write(f'My response:  {self.requestDe}\n')
    self.page +=1
  
   return self.json_file
  
  else:
  
   return self.json_file