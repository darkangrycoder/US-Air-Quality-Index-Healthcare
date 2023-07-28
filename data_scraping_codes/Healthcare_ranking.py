from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
url = 'https://www.moneygeek.com/insurance/health/analysis/2022-top-states-health-care/'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
tables = soup.find_all('table')
desired_table = tables[-1]
headers = []
for th in desired_table.find_all('th'):
    headers.append(th.text.strip())
time.sleep(5)
data = []
for rows in desired_table.find_all('tr'):
    row_data = []
    for td in rows.find_all('td'):
        row_data.append(td.text.strip())
    if row_data:
        data.append(row_data)
df = pd.DataFrame(data, columns=headers)
df.to_csv('Healthcare_ranking.csv', index=False)
