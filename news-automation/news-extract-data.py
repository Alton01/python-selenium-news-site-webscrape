from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://www.thesun.co.uk/sport/football/")


# for getting multiple elements with same xpath class
containers = driver.find_elements(By.XPATH, value='//div[@class="teaser__copy-container"]')


titles = []
subtitles = []
links = []

# itterating to get title, subtitle and link individually
for container in containers:
    title = container.find_element(By.XPATH, value='//div[@class="teaser__copy-container"]/a/span').text
    subtitle = container.find_element(By.XPATH, value='//div[@class="teaser__copy-container"]/a/h3').text
    link = container.find_element(By.XPATH, value='//div[@class="teaser__copy-container"]/a').get_attribute("href")
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)


my_dict = {'title': titles, 'subtitle': subtitles, 'link': links }

df_headlines = pd.DataFrame(my_dict)

# export dataframe in csv format
df_headlines.to_csv('headline.csv')

driver.quit()
