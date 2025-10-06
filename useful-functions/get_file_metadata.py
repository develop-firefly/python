from pwd import getpwuid
from time import ctime
import os

def get_file_metadata(self):
    ''' Function to get the file metadata like
    File name, File owner username, File owner full name,
    Created time, Accessed time, Modified time
    Input: Filename
    '''
    file_metadata = {'File_Name': self.my_filename,
                 'File_Owner_username': getpwuid(os.stat(self.my_filename).st_uid).pw_name,
                 'File_Owner_name': getpwuid(os.stat(self.my_filename).st_uid).pw_gecos,
                 'Created': ctime(os.stat(self.my_filename).st_ctime),
                 'Accessed': ctime(os.stat(self.my_filename).st_atime),
                 'Modified': ctime(os.stat(self.my_filename).st_mtime)
                 }
    return file_metadata