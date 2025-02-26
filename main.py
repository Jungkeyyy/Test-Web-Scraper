import requests
from bs4 import BeautifulSoup

url = "https://lol.fandom.com/wiki/2025_First_Stand"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

# find participating teams
qualified_teams_table = soup.find("table", class_="wikitable")

print(qualified_teams_table.prettify())
