import pymongo


class CRUDMongoDb:

    """ Incomplete, performs CRUD ON MONGO DB Local database"""

    def __init__(self):
     self.myclient : object
     self.mydb: str
     self.mycol: str
     self.myColInserted: str
     self.data: str
     self.database: str
     self.myclient = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
    
    def writeDB(self, database, data, collection_name):
      print('Collection: ',collection_name, '  ', 'Length of payload ', len(data) )
      self.data, self.database = data, database

      if data:
       
       self.mydb = self.myclient[f"{database}"]
       self.mycol = self.mydb[collection_name]
      
       
       for i in data['items']:
        
        self.myColInserted = self.mycol.insert_one(i)
    

    def dropDB(self, unwanted_database):
      self.myclient.drop_database(f'{unwanted_database}')
      return f'{unwanted_database} DB DROPED.'