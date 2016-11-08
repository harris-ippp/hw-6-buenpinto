import requests

# I getting, then saving the .csv files on one big loop_
for line in open("ELECTION_ID"):#Open the ELECTION_ID file
    year=line.split()[0] # Get the year
    id=line.split()[1] # Get the ID
    # Create a generic URL that depends on the election ID as:
    addr="http://historical.elections.virginia.gov/elections/download/"
    addr+=id
    addr+="/precincts_include:0/"
    # Use requests.get() to download the .csv file
    resp = requests.get(addr)
    result = year +".csv" # This is the name of the output file (indexed to the year)
    # Save the .csv file to disk, with the given name
    with open(result, "w") as out:
        out.write(resp.text)
