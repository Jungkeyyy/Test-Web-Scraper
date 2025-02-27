import requests
from bs4 import BeautifulSoup

url = "https://www.espn.com.au/nba/schedule"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
    
# schedule
schedule = soup.find(id="matchlist-content-wrapper")

days = schedule.find_all('th')