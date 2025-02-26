import requests
from bs4 import BeautifulSoup

url = "https://lol.fandom.com/wiki/2025_First_Stand"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

# find participating teams
qualified_teams_table = soup.find("table", class_="wikitable")

# finding qualified regions
qualified_teams_table_rows = qualified_teams_table.find_all('tr')[2:]

qualified_teams_region = []
for row in qualified_teams_table_rows:
    qualified_teams_region.append(row.find_all('td')[0].find_all(text=True, recursive=False)[-1].get_text(strip=True))

#finding qualified teams
qualified_teams = []
for row in qualified_teams_table_rows:
    cells = row.find_all('td')
    team_cell = cells[1]  # The second <td> (team column)
    team_span = team_cell.find('span', class_="team")

    if team_span:
        teamname_span = team_span.find('span', class_="teamname")
        if teamname_span:
            team_link = teamname_span.find('a')
            if team_link:
                qualified_teams.append(team_link.get_text())
            else:
                qualified_teams.append("tbd")
        else:
            qualified_teams.append("tbd")
    else:
        qualified_teams.append("tbd")
    

#print(qualified_teams_table.prettify())
print(qualified_teams_region)
print(qualified_teams)
#print(qualified_teams_table_rows[1])