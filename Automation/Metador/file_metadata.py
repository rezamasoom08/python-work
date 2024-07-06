import os
from datetime import datetime

def GetFileMetadata(FilePath):
    FileStatistics = os.stat(FilePath)
    FileSize = FileStatistics.st_size
    LastModificationDateTime = datetime.fromtimestamp(FileStatistics.st_mtime)

    print(f'The file size is: {FileSize} bytes.')
    print(f'The last modified date and time was: {LastModificationDateTime}')

GetFileMetadata('edms.pdf')