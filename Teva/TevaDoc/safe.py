import jpype
import jpype.imports
from jpype.types import *
import sys

from jpype import JClass, JString

jpype.startJVM(classpath=["C:/Users/Mreza/Documents/Matthew/Softwares/Jars/*","C:/Users/Mreza/Documents/VS Code/Python/Teva/TevaDoc"])

import java.lang

from com.documentum.fc.common import DfId
from com.documentum.fc.common import DfLoginInfo
from com.documentum.fc.client import IDfClient
from com.documentum.com import DfClientX 
from com.documentum.fc.client import IDfSession
from com.documentum.fc.client import IDfSessionManager
from com.documentum.fc.client import IDfQuery
from com.documentum.fc.client import IDfCollection
from com.documentum.fc.common import DfException

def authenticate(repository,user,password):
    
    client = jpype.JClass("com.documentum.fc.client.DfClient")
    idfclient = client.getLocalClient()
    
    loginInfo = DfLoginInfo()
    loginInfo.setUser(user)
    loginInfo.setPassword(password)
    mgr=idfclient.newSessionManager()
    
    mgr.setIdentity(repository,loginInfo)
    session = mgr.newSession(repository)
    return session

def exec_query(query_string, session):
    try:
        col = None  # Collection for the result
        dx = DfClientX()
        query = dx.getQuery()  # Create query object
        query.setDQL(query_string)  # Give it the query
        
        col = query.execute(session, IDfQuery.DF_READ_QUERY)
        print("Query Executed")

        while col.next():
            print("r_object_id:", col.getString("r_object_id"), "object_name:", col.getString("object_name"))
            
        return col
    
    except:
        print("Error executing query:", e)
        if col is not None:
            col.close()
        return None

session = authenticate("fdqmprd","fdmadmp","f0rever9")
print(session.getLoginUserName())

query = "select r_object_id, object_name from dm_document(all) where folder('/TPT/TPT/Form/Patient Technologies', descend)"

exec_query(JObject(query),session)
jpype.shutdownJVM()