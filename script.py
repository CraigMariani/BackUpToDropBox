from selenium import webdriver

login_info = []

def get_login_info():
    file = open('../DropboxInfo/DropBoxAccountInformation.txt', 'r')
    
    for line in file:
        login_info.append(line)
    login_info[0] = login_info[0].rstrip('\n')
    
    return login_info



    return 0

login_info = get_login_info()
usrName = login_info[0]
passWord = login_info[1]


# intiial launch of dropbox
driver = webdriver.Chrome() # get the Chrome Driver
driver.get("https://www.dropbox.com/home/BackUpFiles") #Navigate to URL 

# input login information and submit button
driver.find_element_by_name('login_email').send_keys(usrName)
driver.find_element_by_name('login_password').send_keys(passWord)
driver.find_element_by_class_name('login-button.signin-button.button-primary').click()

# 


