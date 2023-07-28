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
driver.get("https://www.americashealthrankings.org/explore/measures/Obesity")
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
# Extracting & standard formatting
filtered_list = list(set(desired_data))
filtered_list_final = [item for item in filtered_list if '\n' in item]
formatted_list = [item.split('\n') for item in filtered_list_final]

# Remove empty sublists and rows with missing values
formatted_list = [item for item in formatted_list if item]
formatted_list = [item for item in formatted_list if len(item) == len(title)]

# Convert to DataFrame
df = pd.DataFrame(formatted_list, columns=title)
df.to_csv('obesity_data_us.csv', index=False)
print("Success! The data has been saved to 'obesity_data_us.csv'.")
