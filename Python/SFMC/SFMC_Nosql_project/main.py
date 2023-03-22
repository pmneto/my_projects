from requests_SFMC import sfmc_Requests
from request_mc import auth_Mc
import pymongo
from libcheck import checkEnv

if __name__ == "__main__":
 
 env = checkEnv.createEnv()
 checkEnv.installPipReqs(env)
 checkEnv.activateVE(env)

 auth_flow = auth_Mc()
 credentials = auth_flow.auth_flow()
 my_deList = dict()
 

 credentials = auth_flow.refresh_token()
 credentials,rest_url, soap_url = credentials[0],credentials[1][0],credentials[1][-1]
 

 de_customerkey = 'Your_SFMC_DE_CUSTOMERKEY' #specifically this program was meant to request a data extension which holds customer keys from other data extensions
 request_de = sfmc_Requests(de_customerkey,rest_url,soap_url,credentials)
 json_formed = request_de.formDEContent()
 
 my_deList[json_formed['items'][0]['values'].get('data_extension')] = json_formed['items'][0]['values'].get('customerkey')
 
 
 for k,v in my_deList.items():
  
  request_de = sfmc_Requests(v,rest_url,soap_url,credentials)
  json_formed = request_de.formDEContent()
  if json_formed:
   myclient = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
   mydb = myclient["Marketing_Cloud"]
   mycol = mydb[k]
   myColInserted = mycol.insert_one(json_formed)
   