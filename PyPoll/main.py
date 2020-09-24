# main.py 
# PyPoll Vote counting program
#   Opens cvs file PyPoll_Analysis.txt
#   Py_Poll a list of dictionaries is created and intialized.
#       Py_Poll key=candidate name : vote counter for that candidate

import os
import csv

Py_Poll = {}
# Tvotes is the counter for total overall votes.
Tvotes=0
# Cname is candidate name which is used to as the key in the dictionary
Cname=""
inputpath=os.path.join("Resources","election_data.csv")
with open(inputpath) as inputfile:
    inputrecord=csv.reader(inputfile,delimiter=",")
    inputheader=next(inputrecord)
    for record in csv.reader(inputfile):
        Cname=record[2]
# Search the list of dictionaries for the candidate name using .get
        if not Py_Poll.get(Cname):
# If candidate does not exist then create a dictionary and update his vote count to 1.
            Py_Poll[Cname]=1
        else:
# If candidate name is found then update his vote count by adding 1.
            Py_Poll[Cname]+=1
# Update overall vote count by 1 as well
        Tvotes+=1

# After processing is complete sort the list of dictionary using the candidate vote count as the value
# to sort on from largest to smallest so that the winner will be the first dictionary in the list.
    Sorted_Py_Poll=sorted(Py_Poll.items(), reverse=True, key=lambda x : x[1])

# Create PyPoll_Analysis.txt and write the results into the file.

outputpath=os.path.join("Analysis","PyPoll_Analysis.txt")
outputfile=open(outputpath,"w")
outputfile.write("Election Results\n")
outputfile.write("-------------------------\n")
ctvotes="{:,.0f}".format(float(Tvotes))
outputfile.write("Total Votes : " + ctvotes + "\n")
outputfile.write("-------------------------\n")

# Loop to wriite out all the names of the candidates which were created in the list.
for name,votes in Sorted_Py_Poll:
    pvotes="{:.3%}".format(float(votes/Tvotes))
    ctvotes="{:,.0f}".format(float(votes))
    outputfile.write(name + ": " + pvotes + " (" + ctvotes + ")\n")
outputfile.write("-------------------------\n")
outputfile.write("Winner: " + Sorted_Py_Poll[0][0] + "\n")
outputfile.write("-------------------------\n")
outputfile.close()
print("PyPoll Analysis Complete.......")
print("Results written to PyPoll_Analysis.txt file.")
