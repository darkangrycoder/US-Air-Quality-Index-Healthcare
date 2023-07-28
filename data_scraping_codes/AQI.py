from bs4 import BeautifulSoup
import requests 
import time
import pandas as pd
url = 'https://wisevoter.com/state-rankings/air-quality-by-state/'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text,'lxml')
table = soup.find('table')
headers = []
for th in table.find_all('th'):
    headers.append(th.text.strip())
time.sleep(5)
data = []
for row in table.find_all('tr')[1:]:
    row_data=[]
    for td in row.find_all('td'):
        row_data.append(td.text.strip())
    if row_data:
        data.append(row_data)
df = pd.DataFrame(data, columns=headers)
df.to_csv('air_quality_data.csv', index=False)
