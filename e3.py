import pandas as pd
from matplotlib import pyplot as plt


#This is the loop that generates the list of dataframes:
# pre-define a list
list_elections = []
for line in open("ELECTION_ID"): #Loop for every line of ELECTION_ID
    year=line.split()[0] #get the year
    file= year +".csv" # file is the name of the .csv we want to open
    header = pd.read_csv(file, nrows = 1).dropna(axis = 1) # Read only the first row of the .csv
    d = header.iloc[0].to_dict() #Store the wanted columns on 'd'
    df = pd.read_csv(file, index_col = 0,
                  thousands = ",", skiprows = [1]) # Now we read the whole thing
    df.rename(inplace = True, columns = d) # Rename columns to d =democrat/republican etc.
    df.dropna(inplace = True, axis = 1) # Drop empty columns
    df=df[["Democratic", "Republican", "Total Votes Cast"]] #Keep the relevant columns only
    df["Year"] = year #Add a year column
    df["Republican_share"]=round(df["Republican"]/df["Total Votes Cast"],2) #Add a "Republican Share" column as well
    list_elections.append(df) #append this df to the list and start the loop again


#Now we can concatenate all the dataframes in a cumulative fashion:
df=list_elections[0] #The first dataframe of the list is our initial value
for i in range(1, len(list_elections)):
   df=pd.concat([df,list_elections[i]], axis=1) # df is its previous value concatenated with the following element of the list

# Up to now, we have generated a single DataFrame that contains elections results
# for all the given years.

#For the following steps (plot), we will only need the "Year" and "Republican_share" columns
df2=df[["Year","Republican_share"]]

# Get only the info for the given county (Accomack, on the first row)
l = list(df2.iloc[0]) #This gets the first row only, in the form of a list.(i.e. all Republican Shares and Years for Accomack county )

# Now, I'll aim to organize the values from the Accomack county list, that is,
# put the into two separate, well ordered lists for year and Rep_share.

#initialize some lists
Year = []
Rep_share = []
n=0
#I append in reverse order (i.e. insert(o,element)):
for r in l:
    if (n < len(l)/2):
        Year.insert(0,r)
    else: Rep_share.insert(0,r)
    n +=1

#We put both of them in a single series now
series =pd.Series(Rep_share, Year)

#Finally, the plot:

#Store the plot on "figure"
figure = series.plot(x="Year", y="Rep_share", color='r') #red line for republican share :)
#Axis labels
plt.xlabel("Year")
plt.ylabel("Republican Share (%)")
#Plot title
plt.title("Figure 1: Republican Share as a Fraction of Total Votes, Accomack County", y=1.04)

# add a grid for a better look
plt.grid(True)
#explort the plot on a .png format
figure.get_figure().savefig('accomack.png')

#shows the plot on the screen
plt.show()

# --> we see a an increasing trend in the republican share for this county!
