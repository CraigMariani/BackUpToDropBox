# lets you upload a file using dropbox api

# import libraries
import os
import dropbox

# file paths
dropbox_path = '/BackUpFiles/FileExample.txt' 
file_path = '../FolderExample/FileExample.txt'

# read in file to upload and get file size
f = open(file_path, 'r')
file_size = os.path.getsize(file_path)
# print(f)
# print(file_size)
f.close()

# get the access key
f = open('../DropboxInfo/AccessKey.txt', 'r')
access_key = f.readline()
dbx = dropbox.Dropbox(access_key)
# f.close()

with open(file_path, 'rb') as f:
    print(f.read())
    print(type(f.read()))
    print()
    dbx.files_upload(f.read(), dropbox_path)

# dbx.files_upload(open(file_path, "rb").read(), dropbox_path)
