import sys
sys.path.append("../")

from bson import ObjectId
from typing import Tuple, List, Dict
from core import settings
from pymongo import MongoClient

class Connect:
    HOST = "localhost"
    PORT = 27017

    def __init__(
        self,
        host: str = None,
        port: int = None,
        database_name: str = None,
        isAuth: bool = None,
        database_auth_account: str = None,
        database_auth_password: str = None,
    ):
        """
        host                            主机名, 
        port                            端口号,
        database_name                   数据库的名字,
        isAuth                          数据库需不需要验证,
        database_auth_account           数据库验证的账号,
        database_auth_password          数据库验证的密码,
        """
        if host is None:
            host = self.HOST
        if port is None:
            port = self.PORT
        self.client = MongoClient(host, port)
        self.database = self.client[database_name]
        if isAuth:
            self.database.authenticate(
                database_auth_account, database_auth_password)
    

class DataSet:
    def __init__(
        self,
        database,
        set_name
    ):
        self.data_set = database[set_name]
    
    def insert(self, data: Tuple[Dict, List]):
        """
        增加一条或多条字段
        """
        if isinstance(data, dict):
            self.data_set.insert(data)
        elif isinstance(data, list):
            self.data_set.insert(data)
        else:
            raise Exception("BAD DATA TYPE")

    def delete_one(self, query: Dict) -> ObjectId:
        """
        删除指定条件的一条字段
        """
        object_id = self.data_set.find_one(query)["_id"]
        self.data_set.remove(object_id)
        return object_id

    def delete_many(self, query: Dict):
        """
        删除指定条件的多个字段
        """
        self.data_set.remove(query)

    def update_one(self, query: Dict, update_data: Dict):
        """
        修改更新一条数据
        """
        self.data_set.update_one(filter=query, update=update_data)

    def update_many(self, query: Dict, update_data: Dict):
        """
        修改更新多个数据
        """
        self.data_set.update_many(filter=query, update=update_data)

    def find_one(self, query: Dict) -> Dict:
        """
        查找一条数据
        """
        result = self.data_set.find_one(query)
        return result

    def find_many(self, query: Dict) -> List:
        """
        查找多条数据
        """
        result = []
        for i in self.data_set.find(query):
            result.append(i)
        return result


db = Connect(
    database_name="test",
    isAuth=True,
    database_auth_account="root",
    database_auth_password="123456"
)
data_set = DataSet(db.database, "test")
# client.insert({'test': 'test'})
# client.delete_one({'test': 'test'})
print(data_set.find_many({'test': 'test'}))
