#Author:Gcobani Mkontwana
#date:27/02/2023
#Script transalate text into Hindi using google translate API

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium
# Give Language code in which you want to translate the text:=>
lang_code = 'hi '

# Provide text that you want to translate:=>
input1 = " Find your next course.Class Central aggregates courses from many providers to help you find the best courses on almost any subject, wherever they exist"

# launch browser with selenium:=>
browser = webdriver.Chrome() #browser = webdriver.Chrome('path of chromedriver.exe file') if the chromedriver.exe is in different folder

# copy google Translator link here:=>
browser.get("https://translate.google.co.in/?sl=auto&tl="+lang_code+"&text="+input1+"&op=translate")

# just wait for some time for translating input text:=>
time.sleep(6)

# Given below x path contains the translated output that we are storing in output variable:=>
output1 = browser.find_element(By.CLASS_NAME,'HwtZe').text

# Display the output:=>
print("Translated Paragraph:=> " + output1)