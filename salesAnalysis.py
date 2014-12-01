# salesAnalysis.py

# This program takes a series of beginning, ending, sales, error, and add files,
# sums them together into sales files (using the methods of "createSales.py"),
# and generates useful analytic data (such as text files with data, or graphs)

# It is flexible enough to handle many queries. Break out of the program by
# typing 'END'

def main():
    import removeNames
    import createSales
    from graphics import *

    #removeNames.removeNames()
    #createSales.createSales()

    while True: # main loop
        print("This loop will continue until you stop it.")
        print("If you type 'END' (no quotes) into any entry, the program")
        print("will terminate.")
        print()
        print("Type 1 for analytical data (text files)")
        print("Type 2 for graphical data")
        choice1 = input()
        if choice1 == 'END':
            break
        print()

        print("What date range would you like your query to apply to?")
        print("Type dates in MM/DD/YYYY format")
        beginDate = input("BeginDate: ")
        if beginDate == 'END':
            break
        endDate = input("EndDate: ")
        if endDate == 'END':
            break
        print()

        print("What PLU Value would you like to use?")
        print("Type '0' (no quotes) for all PLUs")
        print("For graphical data, the results will be summed")
        print("Type 1 when you are done entering PLUs")
        pluList = []
        while True:
            currentPLU = input()
            #if currentPLU == 'END':
            #    break
            if int(currentPLU) == 1:
                break
            if int(currentPLU) == 0: # all PLUs
                # Add all PLUs to PLU List
                break
            else:
                pluList.append(currentPLU)
        startMonth = str(beginDate[0:2])
        startDay = str(beginDate[3:5])
        startYear = str(beginDate[6:10])
        endMonth = str(endDate[0:2])
        endDay = str(endDate[3:5])
        endYear = str(endDate[6:10])
        beginFile = "SALES "+startYear+","+startMonth+","+startDay+".txt"
        beginFile = str(beginFile)
        endFile = "SALES "+endYear+","+endMonth+","+endDay+".txt"
        endFile = str(endFile)
                
        if int(choice1) == 1: # Analytical
            if len(pluList) == 0: # All PLUs are desired




        if int(choice2) == 2 # Graphical
