# main.py for PYBANK
# Python Script to analyze the financial records of my ficticious company.
#       budget_data is opened read record by record,
#       calculations are performed during this process.
#       After which a text file is created called PyBank_Analysis.txt,
#       and the results are written to it. 
import os
import csv

totalmonths=0
totalPnL=0
firstamount=0
change=0
# recordholder is a list structure to be a place holder so that
# Greatest Increase in Profits and Greatest Decrease in Profits gets calculated.
recordholder=["",0]
Greatest_Increase=["",0]
Greatest_Decrease=["",0]

inputpath=os.path.join("Resources","budget_data.csv")
with open(inputpath) as inputfile:
    inputrecord=csv.reader(inputfile,delimiter=",")
    inputheader=next(inputrecord)
    for record in csv.reader(inputfile):
        totalmonths+=1
# totalPnL get accumulated for as many records contained in the input file.
        totalPnL=totalPnL+float(record[1])
        if (totalmonths==1):
# firstamount gets set to first value in dataset which is triggered when totalmonths equals 1.
            firstamount=float(record[1])
# place holder gets set to current record
            recordholder=record
        else:
# change is calculated by subtracting previous P&L month from the current P&L month
            change=(float(record[1])-float(recordholder[1]))
            if (change>Greatest_Increase[1]):
# change is tested against Greatest Increase value saved from previous loop runs.
# if true date is set and change is saved into Greastest Increase list.                
                Greatest_Increase[0]=record[0]
                Greatest_Increase[1]=change
            if (change<Greatest_Decrease[1]):
# change is tested against Greatest Decrease value saved from previous loop runs.
# if true date is set and change is saved into Greastest Decrease list.                
                Greatest_Decrease[0]=record[0]
                Greatest_Decrease[1]=change
            recordholder=record

# below a text file is opened called PyBank_Analysis.txt and the results
# are written into it through .write.  When complete file is closed with .close()

outputpath=os.path.join("Analysis","PyBank_Analysis.txt")
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