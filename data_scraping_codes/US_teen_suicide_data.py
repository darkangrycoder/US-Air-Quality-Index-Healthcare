from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd

'''Configure the web driver'''
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(
    "C:/Users/Asus/Downloads/chromedriver"), options=options)

'''Navigate to the website'''
driver.get("https://www.americashealthrankings.org/explore/measures/teen_suicide")
time.sleep(5)

'''Access to the main data page'''
main_page = driver.find_element(
    By.XPATH, '//*[@id="measure-page"]/div[4]/div/div[2]/div[2]')

'''click to access main data table'''
access_to_main_data = main_page.find_element(
    By.XPATH, '//*[@id="measure-page"]/div[4]/div/div[2]/div[2]/div[2]')
access_to_main_data.click()
time.sleep(5)

'''locate main data table'''
main_data_table = driver.find_element(
    By.XPATH, '//*[@id="measure-page"]/div[4]/div/div[2]/div[2]/div[3]/div')

'''filter & extract the titles'''
title_element = main_data_table.find_element(
    By.XPATH, '//*[@id="measure-page"]/div[4]/div/div[2]/div[2]/div[3]/div/div/div[2]/div[1]')
title = title_element.text.split("\n")
filtered_title = [t for t in title if t != "Rank"]

'''access to the ranking data'''
main_data_text = main_data_table.find_element(
    By.XPATH, '//*[@id="measure-page"]/div[4]/div/div[2]/div[2]/div[3]/div/div/div[2]/div[2]')
desired_data = []
all_dataset = main_data_text.find_elements(By.TAG_NAME, 'div')
for data in all_dataset:
    desired_data.append(data.text)

'''extracting & standard formatting'''
filtered_list = list(set(desired_data))
filtered_list_final = [item for item in filtered_list if '\n•\n' in item]
formatted_list = [item.split('\n•\n') for item in filtered_list]

'''converting to csv file'''
df = pd.DataFrame(formatted_list, columns=filtered_title)
df.to_csv('Suicide_data_US.csv', index=False)
print("Succeed!!!You can take rest for a while")
