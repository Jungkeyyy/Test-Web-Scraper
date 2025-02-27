import requests
from bs4 import BeautifulSoup

url = "https://www.nba.com/schedule"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
    
# schedule
schedule = soup.find_all("div")

print(soup)