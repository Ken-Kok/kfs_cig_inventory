# createSales.py

# This program uses only begin shift files to generate sales files,
# one for each day. This will aid further processing in order to see
# longitudinal sales figures universally, or by pack.

def createSales():
    import glob
    from datetime import date
    import pyFunctions01

    #print("This program assumes that it is dealing with any range of files with arbitrary names.")
    #print("It will then take only files with the word 'begin', and create sales files based on date.")
    #print()
    print("Available Sales Files:",end='\n')
    functionBeginAdd = '????,??,?? ??,??,?? [AB][ED][GD]??*.txt'
    beginAddFiles = glob.glob(functionBeginAdd)

##    for fileName in beginAddFiles:
##        currentFile = open(fileName,'r')
##        if currentFile.find('BEGIN') == -1: # The file is an add file
##            # Then subtract the add file from the sales file

    beginFile = glob.glob('*BEGIN*.txt')
    addFile = glob.glob('*ADD*.txt')

##    # For every day, create a new sales file
##    firstBegin = beginFile[0]
##    lastBegin = beginFile[-1]
##    d0 = date(int(firstBegin[0:4]),int(firstBegin[5:7]),int(firstBegin[8:10]))
##    d1 = date(int(lastBegin[0:4]),int(lastBegin[5:7]),int(lastBegin[8:10]))
##    delta = d1-d0
##    daysBetween = delta.days # Doesn't include the last day

    # Remove all begin files except the first one for every day
    newBeginFile = []
    newBeginFile.append(beginFile[0]) # Adds the first date
    for i in range(len(beginFile)-1):
        currentFile = beginFile[i]
        nextFile = beginFile[i+1]
        if currentFile[0:10] == nextFile[0:10]: # The files are of the same date
            continue
        else: # the files don't have the same date, therefore the next file is good
            newBeginFile.append(nextFile)
        #print(newBeginFile)

    # Combine add files which occured on the same day into the first one
    addFileTemp = []
    for i in range(len(addFile)-1):
        currentFile = addFile[i]
        nextFile = addFile[i+1]
        if currentFile[0:10] == nextFile[0:10]: # The files have the same date
            addFileTemp.append(currentFile) # build a list of files w/ same date
        else: # The files don't have the same date (we moved on)
            addFileTemp.append(currentFile) # but we missed this one
            # Now put them into one file
            pluList = []
            quantityList = []
            for fileName in addFileTemp:
                currentFile = open(fileName,'r')
                fullList = currentFile.readlines()
                currentFile.close()
#                quantityInfo = fullList.pop()
                totalList = []
                for i in range(len(fullList)):
                    newSplit = fullList[i].split()
                    currentPLU = newSplit[0]
                    if len(newSplit) == 2:
                        currentQuantity = newSplit[-1]
                    else:
                        currentQuantity = newSplit[-2]
                    pluList.append(currentPLU)
                    quantityList.append(currentQuantity)
            # Combine those lists together
            pluList,quantityList = pyFunctions01.combineList(pluList,quantityList,1)
            # Write the combined list to the first add in the temp file
            writeFile = open(addFileTemp[0],'w')
            totalList = []
            for i in range(len(pluList)):
                currentTotal = str(pluList[i])+" "+str(quantityList[i])+str("\n")
                totalList.append(currentTotal)
            totalStr = ''
            for i in range(len(totalList)):
                totalStr = totalStr + str(totalList[i])
            writeFile.write(totalStr)
            writeFile.close()
            addFileTemp = []
#            totalList = []
#            totalStr = ''
            fullList = []

    # Combine the add files together, much like the begin files (such that only the first)
    # is listed
    newAddFile = []
    newAddFile.append(addFile[0]) # Adds the first date
    for i in range(len(addFile)-1):
        currentFile = addFile[i]
        nextFile = addFile[i+1]
        if currentFile[0:10] == nextFile[0:10]: # The files are of the same date
            continue
        else: # the files don't have the same date, therefore the next file is good
            newAddFile.append(nextFile)    
                                          
##    for i in range(daysBetween):
##        dayNumber = i+1
    #print(newBeginFile)
    # Subtract each beginning file from the next, use that to estimate sales
    salesPLUList = []
    salesQuantityList= []
    for i in range(len(newBeginFile)-1):
        todayFileName2 = newBeginFile[i]
        #print(todayFileName)
        tomorrowFileName = newBeginFile[i+1]
        todayDate = todayFileName2[0:10]
        todayFileName = str("SALES")+" "+str(todayDate)+str('.txt')
        # Combine today and tomorrow file, today first
        f1 = open(todayFileName2,'r')
        todayFile = f1.readlines()
        todayFile.pop()
        f1.close()
        todayPLUList = []
        todayQuantityList = []
        for i in range(len(todayFile)):
            newSplit = todayFile[i].split()
            currentPLU = newSplit[0]
            if len(newSplit) == 2:
                currentQuantity = newSplit[-1]
            else:
                currentQuantity = newSplit[-2]
            todayPLUList.append(currentPLU)
            todayQuantityList.append(currentQuantity)
#        todayFileFull = ''
#        for i in range(len(todayPLUList)):
#            todayFileFull = todayFileFull + str(todayPLUList[i])+" "+str(todayQuantityList[i])+str("\n")
        f1 = open(tomorrowFileName,'r')
        tomorrowFile = f1.readlines()
        tomorrowFile.pop()
        f1.close()
        tomorrowPLUList = []
        tomorrowQuantityList = []
        for i in range(len(tomorrowFile)):
            newSplit = tomorrowFile[i].split()
            currentPLU = newSplit[0]
            if len(newSplit) == 2:
                currentQuantity = newSplit[-1]
            else:
                currentQuantity = newSplit[-2]
            tomorrowPLUList.append(currentPLU)
            tomorrowQuantityList.append(currentQuantity)
#        tomorrowFileFull = ''
#        for i in range(len(tomorrowPLUList)):
#            tomorrowFileFull = tomorrowFileFull + str(tomorrowPLUList[i]) +" "+str(tomorrowQuantityList[i])+str("\n")
#        with open(todayFileName,'a') as myfile:
#            myfile.write(tomorrowFileFull)
            #print(tomorrowFile)
##        f2 = open(todayFileName,'a')
##        f2.write(tomorrowFile)
##        f2.close()
        # Now today is today followed by tomorrow, subtract to get to sales
#        fullList = []
#        f3 = open(todayFileName,'r')
#        bigSales = f3.readlines()
#        f3.close()
        salesPLUList = []
        salesQuantityList = []
        for i in range(len(todayPLUList)):
            salesPLUList.append(todayPLUList[i])
            salesQuantityList.append(todayQuantityList[i])
        for i in range(len(tomorrowPLUList)):
            salesPLUList.append(tomorrowPLUList[i])
            salesQuantityList.append(tomorrowQuantityList[i])
        
#        salesPLUList = []
#        salesQuantityList = []
#        for i in range(len(bigSales)):
#            newSplit = bigSales[i].split()
            #print(newSplit)
#            currentPLU = newSplit[0]
#            if len(newSplit) == 2:
#                currentQuantity = newSplit[-1]
#            else:
#                currentQuantity = newSplit[-2]
#            salesPLUList.append(currentPLU)
#            salesQuantityList.append(currentQuantity)
        # Once we make the sales quantity and PLU list, send that to the subtraction method of
        # pyFunctions01
        #print(salesPLUList)
        #print(salesQuantityList)
        salesPLUList,salesQuantityList = pyFunctions01.combineList(salesPLUList,salesQuantityList,3)
        # Add back in any add file associated to this day
        # Build my list of add files
        for fileName in newAddFile:
            #print(fileName)
            if fileName.find(todayDate) == -1: # This add file doesn't have the correct date
                addPLUList = []
                addQuantityList = []
                continue
##                try:
##                    len(addPLUList)
##                    continue
##                except NameError:
##                    addPLUList = []
##                    continue
            else: # This add file does have the correct date
                #print(fileName)
                f4 = open(fileName,'r')
                currentAddFile = f4.readlines()
                f4.close()
                currentAddFile.pop()
                
                addPLUList = []
                addQuantityList = []
                for i in range(len(currentAddFile)):
                    newSplit = currentAddFile[i].split()
                    addPLU = newSplit[0]
                    if len(newSplit) == 2:
                        addQuantity = newSplit[-1]
                    else:
                        addQuantity = newSplit[-2]
                    addPLUList.append(addPLU)
                    addQuantityList.append(addQuantity)
        # Now that we have an add list, we can combine that list with the PLU List
        #print(addQuantityList)
        for i in range(len(addPLUList)):
            salesPLUList.append(addPLUList[i])
            salesQuantityList.append(addQuantityList[i])
        #print(salesQuantityList)
        salesPLUList,salesQuantityList = pyFunctions01.combineList(salesPLUList,salesQuantityList,1)
        #print(salesQuantityList)

        # Create the file using these two lists
        totalStr = ''
        for i in range(len(salesPLUList)):
            totalStr = totalStr + str(salesPLUList[i])+" "+str(salesQuantityList[i])+str("\n")
            #print(totalStr)
        # Once the total string exists, simply create a new file w/ the proper name
#        print(totalStr)
        file = open(todayFileName,'w')
        file.write(totalStr)
        file.close()
        print(todayFileName)
    
