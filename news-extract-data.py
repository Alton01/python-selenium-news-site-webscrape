from selenium import webdriver
from selenium.webdriver.chrome.service import Service 

driver = webdriver.Chrome()
driver.get("https://www.thesun.co.uk/sport/football/")


# for getting multiple elements with same xpath class
# getting both title and subtitle
containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

# getting title, subtitle and link individually
for container in containers:
    title = container.find_element(by="xpath", value='./a/span').text
    subtitle = container.find_element(by="xpath", value='./a/h3').text
    link = container.find_element(by="xpath", value='./a').get_attribute("href")