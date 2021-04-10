# Cody-spambot
Python based Bot with Selenium

Works perfectly fine in Windows 10...other OS no idea...

Python 3 should be installed to the run the bot...


## Webdrivers can be downloaded from here : Check your browser version and download accordingly..
1. Chrome----> https://chromedriver.chromium.org/ ..
2. Edge------> https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ ..
3. Firefox----> https://github.com/mozilla/geckodriver/releases ..


## To check browser version go to : ..

1. **Chrome**----> chrome://settings/help ..
2. **Edge**------> edge://help ..
3. **Firefox**----> Click the menu button ≡ Menu , click Help and select About Firefox

## Add the Path of your webdriver to
- > mah = webdriver.Chrome("`PASTE YOUR WEBDRIVER PATH HERE`") #Example ("E:\WebDrivers\chromedriver.exe")

## Add the site name you want to spam to
- > mah.get("website you want to spam ")#Example:https://tamilhindichat.com

## Remove these lines If there is no Lobby
- >see = mah.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/div[4]/div[2]/div/div[1]")
- >see.click()

## Change this line if ur browser is not chrome...
1. **for Edge**---- > mah = webdriver.Edge("`PASTE YOUR WEBDRIVER PATH HERE`") #Example ("E:\WebDrivers\chromedriver.exe")
2. **for Firefox**--- > mah = webdriver.Firefox("`PASTE YOUR WEBDRIVER PATH HERE`") #Example ("E:\WebDrivers\chromedriver.exe")

## Website link to add
- > mah.get('`http://`') #Paste the cody website you want to spam

## Install

 - Clone the repository `git clone https://github.com/mah-hacker/Cody-Spambot`
 - Install requirements.txt `pip install -r requirements.txt`
 
 ## Run the bot

 - Run the bot `python Cody-Spambot.py`
1. Enter your username
2. Enter your password
3. Spam message you want to send.

..........................................THATS IT THE BOT DOES THE SPAM...........................................

###### BOT OR PUBLISHER IS NOT RESONSIBLE IF ANY BAN/SUSPEND OF ACCOUNT THIS IS ONLY FOR EDUCATIONAL PURPOSE ONLY..SO USE IT WISELY 
