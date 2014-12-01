# Strip the names from an arbitrary file

def removeNames():
    import glob
    
    print("This program strips the Cigarette names from files with an arbitrary name.")
    print("Please put the files into the designated folder, then run this program.")
    print("To delete the names from all SALES files, for instance, type 'SALES' into")
    print("the prompt. To delete the names from all text files in the directory,")
    print("Press 0.")

    print()

    function = input("Please specify which file you would like to delete: ")
    
    if str(function) == '0':
        for fileName in glob.glob('*.txt'):
            print(fileName)
            currentFile = open(fileName,'r')
            fullList = currentFile.readlines()
            currentFile.close()
            quantityInfo = fullList.pop() # Deletes the last line, which contains total info
            totalList = []
            for i in range(len(fullList)):
                newSplit = fullList[i].split()
                currentPLU = newSplit[0]
                if len(newSplit) == 2:
                    currentQuantity = newSplit[-1]
                else:
                    currentQuantity = newSplit[-2]
                currentTotal = str(currentPLU)+" "+str(currentQuantity)+str("\n")
                totalList.append(currentTotal)
            totalStr = ''
            for i in range(len(totalList)):
                totalStr = totalStr + str(totalList[i])
            totalStr = totalStr + quantityInfo
            currentFile = open(fileName,'w')
            currentFile.write(totalStr)
            currentFile.close()
    else:
        beginning = str('*')
        ending = str('*.txt')
        newFunction = beginning + str(function) + ending
        for fileName in glob.glob(newFunction):
            currentFile = open(fileName,'r')
            fullList = currentFile.readlines()
            currentFile.close()
            quantityInfo = fullList.pop() # Deletes the last line, which contains total info
            totalList = []
            for i in range(len(fullList)):
                newSplit = fullList[i].split()
                currentPLU = newSplit[0]
                if len(newSplit) == 2:
                    currentQuantity = newSplit[-1]
                else:
                    currentQuantity = newSplit[-2]
                currentTotal = str(currentPLU)+" "+str(currentQuantity)+str("\n")
                totalList.append(currentTotal)
            totalStr = ''
            for i in range(len(totalList)):
                totalStr = totalStr + str(totalList[i])
            totalStr = totalStr + quantityInfo
            currentFile = open(fileName,'w')
            currentFile.write(totalStr)
            currentFile.close()

    #input("Press 'Enter' to End")
            
            
