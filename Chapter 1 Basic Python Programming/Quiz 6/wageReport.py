# 6 wageReport.py
'''
A program to print the  wage paid to the employees for the given period
by geting a file name from the user
'''
def printRow(*col):
    string = "%9s %11.2f %12.1f" % col
    print(string)

# make a sample report
def makeReport():
    reportFile = open('report', 'w')
    print("Jim\t10.0\t8", file=reportFile)
    print("Tim\t12.0\t6", file=reportFile)
    print("Marry\t11.0\t7", file=reportFile)
    print("David\t18.0\t12", file=reportFile)
    print("Tom\t10.0\t8", file=reportFile)

def main():
    # makeReport()
    try:
        filename = input("Please input a filename: ")
        reportFile = open(filename, 'r')
        # print the title
        print("last_name", "hourly_wage", "hours_worked")
        for line in reportFile:
            line = line.strip()
            last_name, hourly_wage, hours_worked = line.split('\t')
            printRow(last_name, float(hourly_wage), float(hours_worked))
        reportFile.close()

    except FileNotFoundError:
        print("File not found, please retry.")

if __name__ == "__main__":
    main()
'''
sample:
Please input a filename: report

last_name hourly_wage hours_worked
      Jim       10.00          8.0
      Tim       12.00          6.0
    Marry       11.00          7.0
    David       18.00         12.0
      Tom       10.00          8.0
'''      
