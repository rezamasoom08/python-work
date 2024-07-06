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
from com.documentum.fc.client import IDfSession
from com.documentum.fc.client import IDfSessionManager
from com.documentum.fc.client import IDfQuery
from com.documentum.fc.client import IDfCollection
from com.documentum.fc.common import DfException
from com.documentum.com import DfClientX 

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

def getfile(sysobj,session,fn):
    print("---->getfile")
    try:
        sysobj.getFileEx2(fn, "pdf",0,"",JBoolena(False))
    except:
        print("Caught python exception during DFC getfile :", str(ex))

def exec_query(query_string, session):
    col = None  # Collection for the result
    dx = DfClientX()
    query = dx.getQuery()  # Create query object
    query.setDQL(query_string)  # Give it the query
    
    col = query.execute(session, IDfQuery.DF_READ_QUERY)
    while col.next():
        print(col.getString("recnum")+col.getString("comp_name")+col.getString("content_type"))

    
def pdfWriter(file,to,session,properties):
    print("---->pdfwriter")

    from datetime import datetime
    from pypdf import pdfWriter, pdfReader

    reader = pdfReader(file)
    writer = pdfWriter()

    #add all pages to the writer
    for page in reader.pages:
        writer.add_page(page)
    
    #for old metadata
    metadata = reader.metadata
    writer.add_metadata(metadata)

    # format the current date and time
    utc_time = "-05'00"
    time = datetime.now().strftime(f"D\072%Y%m%d%H%M%S(utc_time)")

    metadata = {}
    from com.documentum.fc.common import IDfAttr
    ac = to.getAttrCount()
    i = 0
    bFirst = 0

    ac = to.getAttrCount()
    i = 0
    value = ""
    while (i<ac):
        attr = to.getAttr(i)
        if attr.getName() == "title":
            metadata["/Title"] = str(getAttrValue(to,attr))
        else:
            metadata["/"+str(attr.getName())] = str(getAttrValue(to,attr))
        i = i + 1
    
    metadata["/audit_trail_file"] = to.getString("object_name")+"_audit.html"
    writer.add_metadata(metadata)

# save the new pdf to a file

with open(False+"1.pdf", "wb") as f:
    writer.write(f)

session = authenticate("fdqmprd","fdmadmp","f0rever9")
print(session.getLoginUserName())

query = "select * from dm_cabinet"

print(query)

exec_query(JObject(query),session)
jpype.shutdownJVM()