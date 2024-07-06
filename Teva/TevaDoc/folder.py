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
            dfId=dx.getId(col.getString("r_object_id"))
            sysobj=session.getObject(dfId)
            fn="C:/Users/Mreza/Documents/Matthew/Tevadoc/"+str(sysobj.getString("object_name"))+".pdf"
            print(fn)
            getFile(sysobj, session, fn)
        return col
    
    except:
        print("Error executing query:", e)
        if col is not None:
            col.close()
        return None

def getFile(sysobj,session,fn):
  print("---->getFile")
  try:
    #sysobj.getFile(sysobj.getString("object_name"))
    sysobj.getFileEx2(fn,"pdf",0,"",JBoolean(False))
  except Exception as ex:
    print("Caught python exception during DFC getfile :", str(ex))


session = authenticate("fdqmprd","fdmadmp","f0rever9")
print(session.getLoginUserName())

#query = "select r_object_id, object_name from dm_document(all) where folder('/TPT/TPT/Form/Patient Technologies', descend)"

with open('folder_list.txt') as f:
    lines = f.readlines()
    for line in lines:
        path = line.strip()
        #print(path)
        query = f"select r_object_id, object_name from dm_document where folder('{path}', descend)"
        #print(query)
        exec_query(JObject(query),session)

#exec_query(JObject(query),session)

jpype.shutdownJVM()