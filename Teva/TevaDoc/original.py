import jpype
import jpype.imports
from jpype.types import *
import sys
import os
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


# Function to authenticate to Documentum repository
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

# Function to execute a DQL query
def exec_query(query_string, folder, session):
    try:
        col = None  # Collection for the result
        dx = DfClientX()
        query = dx.getQuery()  # Create query object
        query.setDQL(query_string)  # Give it the query
        
        col = query.execute(session, IDfQuery.DF_READ_QUERY)   # Execute the query
        print("Query Executed")

        # Iterate over the result set
        while col.next():
            print("r_object_id:", col.getString("r_object_id"), "object_name:", col.getString("object_name"))   # Print object id and name
            dfId=dx.getId(col.getString("r_object_id"))
            sysobj=session.getObject(dfId)            
            fn=f"{str(folder)}"+str(sysobj.getString("object_name"))+".pdf"
            print(fn)
            #getFile(sysobj, session, fn)   # Get file
        return col
    
    except Exception as e:    # Catch any exceptions
        print("Error executing query:", e)
        if col is not None:
            col.close()   # Close the collection
        return None

# Function to create folder structure
def create_folder_structure(base_dir, path):
    try:
        # Create the base directory if it doesn't exist
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        folder_path = os.path.join(base_dir, path)   # Join base directory and path
        os.makedirs(folder_path, exist_ok=True)   # Create folder
        print(f"Folder '{path}' created successfully at '{base_dir}'")
        return(folder_path)    # Return the folder path

    except OSError as error:
        print(f"Failed to create folder structure: {error}")

# Function to get a file from Documentum
def getFile(sysobj,session,fn):
  print("---->getFile")
  try:
    sysobj.getFileEx2(fn,"pdf",0,"",JBoolean(False))   # Get file
  except Exception as ex:
    print("Caught python exception during DFC getfile :", str(ex))


# Authenticate to Documentum repository
session = authenticate("fdqmprd","fdmadmp","f0rever9")
print(session.getLoginUserName())   # Print the logged-in user

# Read folder paths from file
with open('folder_list.txt') as f:
    base_dir = "C:/Users/Mreza/Documents/Matthew/Tevadoc"
    lines = f.readlines()
    # Iterate over each line
    for line in lines:
        path = line.strip()   # Remove leading/trailing whitespace
        query = f"select r_object_id, object_name from dm_document where folder('{path}', descend)"    # Construct query
        modify = path[1:]   # Remove the first character
        modify += "/"   # Append "/"
        folder = create_folder_structure(base_dir, modify)   # Call create_folder_structure function
        exec_query(JObject(query),folder,session)    # call exec_query function

# Shutdown the JVM
jpype.shutdownJVM()