from bs4 import BeautifulSoup
import requests

# Send a GET request to the webpage
url = "https://www.usnews.com/news/best-states/rankings/health-care"
response = requests.get(url)

# Create a BeautifulSoup object with the response text
soup = BeautifulSoup(response.text, "html.parser")

# Find the ordered list of states
ol = soup.find("ol", class_="item-list")
print(ol.text)
