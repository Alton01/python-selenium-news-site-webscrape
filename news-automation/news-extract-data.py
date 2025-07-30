from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

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

# export dataframe in csv format
df_headlines.to_csv('headline-headless.csv')

driver.quit()
