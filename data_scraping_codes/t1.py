import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create a new instance of the Chrome driver
driver_path = 'C:/Users/Asus/Downloads/chromedriver'
driver = webdriver.Chrome(driver_path)

# Navigate to the US News website
driver.get("https://www.usnews.com/news/best-states/rankings/health-care")

# Find the table of rankings
table = driver.find_element_by_xpath("//table[@class='table table-striped table-hover table-sm']")

# Get all of the rows in the table
rows = table.find_elements_by_xpath(".//tr")

# For each row, get the state name, ranking, and score
for row in rows:
    # Get the state name
    state_name = row.find_element_by_xpath(".//td[1]").text
    # Get the ranking
    ranking = row.find_element_by_xpath(".//td[2]").text
    # Get the score
    score = row.find_element_by_xpath(".//td[3]").text
    # Print the state name, ranking, and score
    print(f"{state_name}: {ranking} ({score})")

# Quit the browser and WebDriver instance
driver.quit()
