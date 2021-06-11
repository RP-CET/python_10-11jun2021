#pip install selenium==4.0.0.b4
#download https://msedgedriver.azureedge.net/91.0.864.41/edgedriver_win64.zip
#put msedgedriver.exe in the same path as this Python Script

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge("msedgedriver.exe")  # Optional argument, if not specified will search path.


driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 120)
  
# Replace 'Friend's Name' with the name of your friend 
# or the name of a group 
target = '"+65 1177 1111"'
  
# Replace the below string with your own message
string = "Message sent using Python, test 2!!!"
  
x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
group_title.click()
inp_xpath = '//div[@class="_2_1wd copyable-text selectable-text"][@dir="ltr"][@data-tab="6"]'
input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))

#WhatsApp for App is ready
input_box.send_keys(string + Keys.ENTER)

#this is just make sure that the Edge browser to stay in view
input()