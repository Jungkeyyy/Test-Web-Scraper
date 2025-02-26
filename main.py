import requests
from bs4 import BeautifulSoup

url = "https://lol.fandom.com/wiki/2025_First_Stand"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

# find participating teams
qualified_teams_table = soup.find("table", class_="wikitable")

# finding team names and region
qualified_teams_table_rows = qualified_teams_table.find_all('tr')[2:]

qualified_teams_region =[]
for row in qualified_teams_table_rows:
    qualified_teams_region.append(row.find_all('td')[0].get_text())

#print(qualified_teams_table.prettify())
print(qualified_teams_region)
#print(qualified_teams_table_rows[1])