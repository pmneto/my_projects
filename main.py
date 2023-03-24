from requests_SFMC import sfmc_Requests
from request_mc import auth_Mc
from config import sfmcInfo
from libcheck import checkEnv
from CRUDMongoDb import CRUDMongoDb
import sys
import json


if __name__ == "__main__":
 

 stats = sfmcInfo.stats.stats
 database = 'Marketing_Cloud'
 de_customerkey = sfmcInfo.environmentVariables.data_extension
 my_deList = dict()
 
 sys.stdout.write(f'My status:  {stats}\n')

 env = checkEnv.createEnv()
 checkEnv.installPipReqs(env)
 checkEnv.activateVE(env)

 auth_flow = auth_Mc()
 credentials = auth_flow.auth_flow()
 mongoLib = CRUDMongoDb()

 
 credentials,rest_url, soap_url = credentials[0],credentials[1][0],credentials[1][-1]
 

 
 request_de = sfmc_Requests(de_customerkey,rest_url,soap_url,credentials)
 json_formed = request_de.formDEContent()
 
 
 for i in json_formed['items']:
    
    my_deList[i['values'].get('data_extension')] = i['values'].get('customerkey')
    

 if stats != 'prod':
   print(mongoLib.dropDB(database))



 for k,v in my_deList.items():
  
        request_de = sfmc_Requests(v,rest_url,soap_url,credentials)
        json_formed = request_de.formDEContent(k)
        count = json_formed['count']
        print(f'My json: {count}')
        print(f'DE REQUESTED: {k}')
        mongoLib.writeDB("Marketing_Cloud", json_formed,k)