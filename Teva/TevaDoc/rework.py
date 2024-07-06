import configparser
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

def read_documentum_credentials(config_file):
    #print(config_file)
    config = configparser.ConfigParser()
    config.read(config_file)
    config.sections()

    if 'documentum' not in config:
        raise ValueError("Documentum section not found in the config file")

    username = config['documentum'].get('username')
    password = config['documentum'].get('password')
    docbase = config['documentum'].get('docbase')
    #server = config['documentum'].get('server')

    if not all([username, password, docbase]):
        raise ValueError("Incomplete credentials found in the config file")

    return username, password, docbase

# Function to authenticate to Documentum repository
def authenticate(username,password,docbase):
    
    client = jpype.JClass("com.documentum.fc.client.DfClient")
    idfclient = client.getLocalClient()
    
    loginInfo = DfLoginInfo()
    loginInfo.setUser(username)
    loginInfo.setPassword(password)
    mgr=idfclient.newSessionManager()
    
    mgr.setIdentity(docbase,loginInfo)
    session = mgr.newSession(docbase)
    return session

if __name__ == "__main__":
    config_file = "documentum.ini"
    try:
        username, password, docbase = read_documentum_credentials(config_file)
        session = authenticate(username, password, docbase)
        print(session.getLoginUserName())   # Print the logged-in user  
        # Use docbase_conn to perform operations on Documentum server
    except Exception as e:
        print(f"Error: {e}")

jpype.shutdownJVM()
