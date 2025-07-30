from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
from datetime import datetime
import os
import sys

# code for converting py file to executable from the terminal - pyinstaller --onefile news-extract-data.py

# pyinstaller converts .py files to executables(exe)
# get and set the path of executable to be created
application_path = os.path.dirname(sys.executable)

now = datetime.now()

month_day_year = now.strftime("%m%d%Y")

#Headless Mode
options = Options()
options.add_argument("--headless=new")
#options.headless = True

driver = webdriver.Chrome(options=options)
driver.get("https://www.thesun.co.uk/sport/football/")

# for getting multiple elements with same xpath class
containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')


titles = []
subtitles = []
links = []

# itterating to get title, subtitle and link individually
for container in containers:
    title = container.find_element(by="xpath", value='//div[@class="teaser__copy-container"]/a/span').text
    subtitle = container.find_element(by="xpath", value='//div[@class="teaser__copy-container"]/a/h3').text
    link = container.find_element(by="xpath", value='//div[@class="teaser__copy-container"]/a').get_attribute("href")
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)


my_dict = {'title': titles, 'subtitle': subtitles, 'link': links }

df_headlines = pd.DataFrame(my_dict)

#File name creation
file_name = f'headline-{month_day_year}.csv'
final_path = os.path.join(application_path, file_name)

# export dataframe in csv format
df_headlines.to_csv(final_path)

driver.quit()
