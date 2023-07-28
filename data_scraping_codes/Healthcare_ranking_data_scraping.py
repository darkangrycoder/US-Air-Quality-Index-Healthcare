from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

'''Site that I have been scraping'''
url = 'https://www.hospitalsafetygrade.org/state-rankings'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
table = soup.find('table')
headers = []

'''Scrapping Table Headers'''
for th in table.find_all("th"):
    headers.append(th.text.strip())
time.sleep(5)

'''Cleaning & Filtering Headers'''
filtered_headers = [x.replace('\xa0', ' ').replace(
    '\r', '').replace('\n', '').replace('\t', '').replace('% A', '').replace('Â', '') for x in headers]
data = []

'''Scrapping Table Rows'''
for row in table.find_all("tr"):
    row_data = []
    for td in row.find_all("td"):
        row_data.append(td.text.strip())
    if row_data:
        data.append(row_data)
df = pd.DataFrame(data, columns=headers)
df.to_csv('Overall_Healthcare_ranking.csv', index=False)
print(f"Successfully data extracted to 'Overall_Healthcare_ranking.csv' file.")
