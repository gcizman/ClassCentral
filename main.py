from googletrans import Translator
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pandas as pd
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument("window-size=1920,1080")
driver = webdriver.Chrome(options=chrome_options)
url = "https://www.classcentral.com/collection/top-free-online-courses"
driver.get(url)

translator = Translator()

try:
    while True:
        # wait until button is clickable
        WebDriverWait(driver, 1).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//button[@data-name='LOAD_MORE']"))
        ).click()
        time.sleep(0.5)
except Exception as e:
    pass

all_courses = driver.find_element(by=By.CLASS_NAME, value='catalog-grid__results')
courses = all_courses.find_elements(by=By.CSS_SELECTOR, value='[class="color-charcoal course-name"]')

df = pd.DataFrame([[course.text, course.get_attribute('href')] for course in courses],
                  columns=['Title (eng)', 'Link'])

df['Title (hin)'] = df['Title (eng)'].apply(lambda x: translator.translate(x, dest='hi').text)

print(df)
