from bs4 import BeautifulSoup
import requests
import pandas as pd

'''Site that I am scraping about'''
url = 'https://www.moneygeek.com/insurance/health/analysis/2022-top-states-health-care/'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
tables = soup.find_all('table')

'''Get the last table'''
last_table = tables[-1]

'''Extracting desired data'''
data = []
rows = last_table.find_all('tr')
header = [cell.get_text(strip=True) for cell in rows[0].find_all('th')]

for row in rows[1:]:
    data.append([cell.get_text(strip=True) for cell in row.find_all('td')])

'''creating file'''
df = pd.DataFrame(data, columns=header)
df.to_csv("state_overall_healthcare_ranking.csv", index=False)
print(f"Successfully data extracted to 'state_overall_healthcare_ranking.csv' file.")
