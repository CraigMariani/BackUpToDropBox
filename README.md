# BackUpToDropBox
Automation script that backs up files to your Drop Box account


My first attempt was with using selenium to automate the login process and upload a file that the user is creating. 
I had issues with the upload feature. To get by this I tried using the DropBox API to upload a file to the 
BackUp folder in the dropbox account. There was an issue with uploading the file however, the error stated
"BadInputError" "Error in call API function (file/upload): The given OAuth 2 accesss token is malformed"
