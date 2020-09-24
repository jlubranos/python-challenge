import os
import csv

Py_Poll = {}
Tvotes=0
Cname=""
inputpath=os.path.join("Resources","election_data.csv")
with open(inputpath) as inputfile:
    inputrecord=csv.reader(inputfile,delimiter=",")
    inputheader=next(inputrecord)
    for record in csv.reader(inputfile):
        Cname=record[2]
        if not Py_Poll.get(Cname):
            Py_Poll[Cname]=1
        else:
            Py_Poll[Cname]+=1
        Tvotes+=1
    Sorted_Py_Poll=sorted(Py_Poll.items(), reverse=True, key=lambda x : x[1])
outputpath=os.path.join("Analysis","PyPoll_Analysis.txt")
outputfile=open(outputpath,"w")
outputfile.write("Election Results\n")
outputfile.write("-------------------------\n")
ctvotes="{:,.0f}".format(float(Tvotes))
outputfile.write("Total Votes : " + ctvotes + "\n")
outputfile.write("-------------------------\n")
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
