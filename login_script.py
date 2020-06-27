# this script allows the user to login automatically and can access files


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC

import time
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

# select local files to upload
# driver.find_element_by_class_name("ue-effect-container uee-AppActionsView-SecondaryActionMenu-text-upload-file")
# driver.find_element_by_xpath('.//div[@class= "ue-effect-container uee-AppActionsView-SecondaryActionMenu-text-upload-file"]').click()

# driver.switch_to.window(driver.window_handles[-1])
# driver.find_element_by_link_text("Upload Files").click()
# element = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.LINK_TEXT,"Upload Files")))
# element.click

# upload_element = driver.find_element_by_xpath("/html/body/div[6]/div/div/div[3]/div[2]/div[2]/div/div/div[3]/div/ul/li[1]/button/span/span[2]/div")[0]
# upload_element.click()

# driver.find_element_by_class_xpath("//span[@class='']")
time.sleep(5)
driver.quit()
