from selenium import webdriver
import time
from getpass import getpass

print('  ____ ___  ______   __  ____  ____   _    __  __   ____   ___ _____ ')
print(' / ___/ _ \|  _ \ \ / / / ___||  _ \ / \  |  \/  | | __ ) / _ \_   _|')
print('| |  | | | | | | \ V /  \___ \| |_) / _ \ | |\/| | |  _ \| | | || |  ')
print('| |__| |_| | |_| || |    ___) |  __/ ___ \| |  | | | |_) | |_| || |  ')
print(' \____\___/|____/ |_|   |____/|_| /_/   \_\_|  |_| |____/ \___/ |_|  ')
print('\n')

username = input("Enter in your username: ")
password = getpass("Enter your password: ")
inputString = input("Enter message to send: ")

mah = webdriver.Chrome("Your Webdriver Path") #Example ("E:\WebDrivers\chromedriver.exe")
mah.implicitly_wait(15)

mah.get("website you want to spam ")#Example:https://tamilhindichat.com
time.sleep(5)
enter = mah.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div[2]/button[1]")     
enter.click()
time.sleep(2)
username_textbox = mah.find_element_by_id("user_username")
username_textbox.send_keys(username)

password_textbox = mah.find_element_by_id("user_password")
password_textbox.send_keys(password)

login = mah.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[1]/div[2]/button")     
login.click()

see = mah.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/div[4]/div[2]/div/div[1]")
see.click()

time.sleep(10)

i=0
while i<= 1:
    sendmsg = mah.find_element_by_name("content")
    sendmsg.send_keys(inputString)
    submit = mah.find_element_by_id("submit_button")
    submit.click()      
    time.sleep(3)
