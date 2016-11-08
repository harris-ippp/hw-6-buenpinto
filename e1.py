
import requests
from bs4 import BeautifulSoup

# This is the URL I'll be using to get the IDs and Years
elec_add="http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2015/office_id:1/stage:General"

#Make the request.get and use BeautifulSoup to parse it
resp = requests.get(elec_add)
soup = BeautifulSoup(resp.content , "html.parser")

#Define 2 empty lists
id=[]
year=[]
# This is the loop through the soup's find_all result:
for tr in soup.find_all('tr', 'election_item'):
    id.append(tr.get('id').split("-")[2]) # Get the ID and append it to the ID list
    year.append(tr.find("td").string) # Get the year and append it to the year list

# Now I can create the ELECTION_ID list, with both IDs and Years
ELECTION_ID = [year,id]

# Print the resultant list (the for loop makes it so the output is clearer)
for i in range(0,len(year)):
    print(ELECTION_ID[0][i], ELECTION_ID[1][i])

# This output is then saved from the Bash command line by doing
# python e1.py > ELECTION_ID
