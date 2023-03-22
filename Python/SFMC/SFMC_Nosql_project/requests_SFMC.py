import json
import requests
from datetime import datetime as dt


class sfmc_Requests:

 def __init__(self,de_customerkey,rest_url,soap_url,credentials):
  self.rest_url, self.soap_url, self.credentials = rest_url, soap_url, credentials
  self.header =  {
    'Content-type': 'application/json',
    'Authorization': 'Bearer ' + self.credentials[0]}
  self.de_customerkey = de_customerkey
  self.page = 1

 def get_DE(self):
 
  self.url_requested = self.rest_url + 'data/v1/customobjectdata/key/DE_EXTERNAL_KEY/rowset'.replace('DE_EXTERNAL_KEY', self.de_customerkey)
 
  if (self.credentials[-1] > dt.today().strftime('%Y-%m-%d %H:%M:%S')) == True:
   request = requests.get(self.url_requested + f'?page={self.page}', headers = self.header)
   return request.json()
  else:
   return 'Token Expired'
    
 def formDEContent(self):
  self.construct = sfmc_Requests(self.de_customerkey, self.rest_url, self.soap_url, self.credentials)
  self.requestDe = self.construct.get_DE()
  self.json_file = self.requestDe
  
  if self.requestDe['count'] >= 2500:
  
   self.pages = self.requestDe['count']/2500
  
   while(self.page<=self.pages):
    self.requestDe = self.construct.get_DE()
    self.json_file += self.requestDe
    self.page+=1
  
   return self.json_file
  
  else:
  
   return self.json_file