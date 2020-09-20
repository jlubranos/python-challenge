# main.py for PYBANK
import os
import csv

totalmonths=0
totalPnL=0
firstamount=0
change=0
recordholder=["",0]
Greatest_Increase=["",0]
Greatest_Decrease=["",0]

inputpath=os.path.join("Resources","budget_data.csv")
with open(inputpath) as inputfile:
    inputrecord=csv.reader(inputfile,delimiter=",")
    inputheader=next(inputrecord)
    for record in csv.reader(inputfile):
        totalmonths+=1
        totalPnL=totalPnL+float(record[1])
        if (totalmonths==1):
            firstamount=float(record[1])
            recordholder=record
        else:
            change=(float(recordholder[1])-float(record[1]))*-1   
            if (change>Greatest_Increase[1]):
                Greatest_Increase[0]=record[0]
                Greatest_Increase[1]=change
            if (change<Greatest_Decrease[1]):
                Greatest_Decrease[0]=record[0]
                Greatest_Decrease[1]=change
            recordholder=record
outputpath=os.path.join("Analysis","PyBank_Analysis.csv")
outputfile=open(outputpath,"w")
outputfile.write("Financial Analysis\n")
outputfile.write("----------------------------\n")
outputfile.write("Total Months: ")
outputfile.write(str(totalmonths))
outputfile.write("\n")
outputfile.write("Total: $")
outputfile.write(str(round(totalPnL)))
outputfile.write("\n")
outputfile.write("Average Change: $")
outputfile.write(str(round((float(record[1])-firstamount )/(totalmonths-1),2)))
outputfile.write("\n")
outputfile.write("Greatest Increase in Profits: ")
outputfile.write(str(Greatest_Increase[0]))
outputfile.write("  ($")
outputfile.write(str(round(Greatest_Increase[1])))
outputfile.write(")")
outputfile.write("\n")
outputfile.write("Greatest Decrease in Profits: ")
outputfile.write(str(Greatest_Decrease[0]))
outputfile.write("  ($")
outputfile.write(str(round(Greatest_Decrease[1])))
outputfile.write(")")
outputfile.write("\n")
outputfile.close()
print("Analysis Complete.....")