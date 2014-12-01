# add_inventory.py

##def combinePLUs(pluList,quantityList):
##    # This file checks to see if there are any copy PLUs in the list, and if there are,
##    # it adds the quantities together.
##    # This allows, for instance, a cashier to scan packs twice, when they mean to scan cartons the second time.
##    quantity = 0
##    newPLUList = []
##    newQuantityList = []
##    for i in pluList:
##        while pluList.count(i) > 1:
##            location = pluList.index(i)
##            try:
##                currentQuantity = quantityList.pop(location)
##            except IndexError:
##                break
##            quantity = quantity + int(currentQuantity)
##        newPLUList.append(i)
##        newQuantityList.append(quantity)
##        for i in newPLUList:
##            if newPLUList.count(i) > 1:
##                location = newPLUList.index(i)
##                newPLUList.pop(location)
##                newQuantityList.pop(location)
##              
##    return newPLUList,newQuantityList

def playBuzzer(wavFile):

    import wave, sys, pyaudio
    sound = wave.open(wavFile)
    p = pyaudio.PyAudio()
    chunk = 1024
    stream = p.open(format =
                    p.get_format_from_width(sound.getsampwidth()),
                    channels = sound.getnchannels(),
                    rate = sound.getframerate(),
                    output = True)
    data = sound.readframes(chunk)
    while data != '':
        stream.write(data)
        data = sound.readframes(chunk)
        
def checkPLU(currentPLU,masterPLUList):
    # This file checks to make sure that the PLU currently in the process of scanning is in the database.
    # If it is not in the database (such as not entered yet, or the scanner misfired), it rings a bell, and returns
    # A 0 for False to main(). If the PLU is available in the database, then it returns a 1 for True to main()

    
    existsTrue = masterPLUList.count(currentPLU)
    if existsTrue == 0: # The PLU is not in the list
        print("The PLU scanned is not in the list")
        print('\a')
        trufla = 0
        pluIndex = 1000000
    if existsTrue > 0:
        pluIndex = masterPLUList.index(currentPLU)

    if existsTrue == 1: # The PLU is a primary, that is to say it is a carton in the case of cigs
                        # Or, the PLU carton has not been scanned, and thus only a pack is in the database
        #print("You scanned a carton.")
        #print("If this is a pack, the carton-pack relationship has not been established")
        trufla = 1
    if existsTrue == 2: # The PLU is a secondary, that is to say it is a pack
        #print("You scanned a pack")
        trufla = 1
    if existsTrue > 2: # The PLU must not be entered into the system correctly.
        #print("You scanned a pack that is in the system at least two times.")
        trufla = 1

    return trufla, pluIndex
    
def createFile(pluList, nameList, quantityList, priceList, fileName):
    fullList = ''

    sumSales = 0
    sumQuantity = 0
    newNameList = []
    newNameStr = ''
    for i in range(len(nameList)):
        for j in range(len(nameList[i])):
            newNameStr = newNameStr + " " + nameList[i][j]
        newNameList.append(newNameStr)
        newNameStr = ''
    for i in range(len(pluList)):
        if pluList[i][0] != '0':
            fullList = fullList + str(pluList[i][0])+" "+str(newNameList[i])+" "+str(quantityList[i][0])+" "+str(priceList[i])+str("\n") #nameList is messed up
        else:
            fullList = fullList + str(pluList[i])+" "+str(newNameList[i])+" "+str(quantityList[i])+" "+str(priceList[i])+str("\n") #nameList is messed up
            sumSales = sumSales + float(priceList[i])*float(quantityList[i])
            sumQuantity = sumQuantity + float(quantityList[i])
    fullList = fullList + str(sumQuantity)+" "+str(sumSales)
    file = open(fileName, 'w')
    file.write(fullList)
    file.close()

def main():
    """

    :rtype : object
    """
    import pyFunctions01
    masterPLU = open('Master PLU List.txt', 'r')
    pluNameList = masterPLU.readlines()
    masterPLU.close()

    masterPLU = []
    masterName = []
    masterPrice = []
    masterEquivPLU = []
    masterEquivQnt = []
    for i in range(len(pluNameList)):
        masterList = pluNameList[i].split()
        masterPLU.append(masterList[0])
        masterName.append(masterList[1:-3])
        masterPrice.append(masterList[-3])
        masterEquivPLU.append(masterList[-2])
        masterEquivQnt.append(masterList[-1])

    
    import time
    name = input("What is your Name (First Last): ")
    #date = input("What is the date (YYYYMMDD)?: ")
    date = time.strftime("%Y,%m,%d %H,%M,%S")

    # Create file name

##    year = date[0:4]
##    month = date[4:6]
##    day = date[6:8]

    nameList = name.split(" ")
    lastName = nameList[-1]
    firstName = nameList[0]

    addFileName = date+" "+"ADD"+" "+lastName+" "+firstName+".txt"

    # Gather PLU Information (plu, amt)

    counter1 = 0
    pluList = []
    quantityList = []
    newList = []

    while True:
        pluName = input("Type of scan the PLU (or 'END' to exit): ")
        if pluName == 'END':
            break
        else:
            pluExists, pluIndex = checkPLU(pluName,masterPLU)
            if pluExists == 0:
                playBuzzer('Buzzer.wav')
                continue
            print(masterName[pluIndex])
        quantity = input("Type the quantity: ")
        isDigit = pyFunctions01.checkDigit(str(quantity))
        if isDigit == 0: # The value is not a digit
            playBuzzer('Buzzer.wav')
            print("There was a non-numerical character in your quantity string")
            continue
        if len(str(quantity)) > 4:
            print("The quantity is too large, please scan that pack again.")
            print("If you meant to enter more than 4 digits, please split")
            print("the quantity by scanning the PLU twice.")
            playBuzzer('Buzzer.wav')
            continue
        elif str(quantity) == '':
            print("You entered nothing for quantity.")
            print("Please enter the PLU again.")
            playBuzzer('Buzzer.wav')
            continue
        with open('pluListTemp.txt','a') as pluFile:
            pluFile.write(str(pluName))
            pluFile.write('\n')
        with open('quantityListTemp.txt','a') as quantityFile:
            quantityFile.write(str(quantity))
            quantityFile.write('\n')
        #quantityFile = open('quantityListTemp.txt','a')
        #pluList.append(pluName)
        #quantityList.append(quantity)
        counter1=counter1+1
    # Update the pluList and quantityList, adding all PLUs together.
    # This file takes time, pops both lists and recreates.
    newPluFile = open('pluListTemp.txt','r')
    pluList = newPluFile.read()
    pluList = pluList.split()
    newQuantityFile = open('quantityListTemp.txt','r')
    quantityList = newQuantityFile.read()
    quantityList = quantityList.split()
    newPluFile.close()
    newQuantityFile.close()
    newPluFile = open('pluListTemp.txt','w')
    #newPluFile.write()
    newPluFile.close()
    newQuantityFile = open('quantityListTemp.txt','w')
    #newQuantityFile.write()
    newQuantityFile.close()
    pluList,quantityList = pyFunctions01.combineList(pluList,quantityList,1)
    #pluList,quantityList = combinePLUs(pluList,quantityList)

    # Find inventory file, make two lists of PLUs and Quantities

    inventoryFile = open('Master Inventory.txt', 'r')
    inventory = inventoryFile.readlines()
    inventoryFile.close()

    inventoryPLUList = []
    inventoryQuantityList = []

    inventoryTest = inventory[-1].split()
    if 3 > len(inventoryTest):
        for i in range(len(inventory)-1):
            inventorySplit = inventory[i].split()
            inventoryPLU = inventorySplit[0]
            inventoryQuantity = inventorySplit[-2]
            inventoryPLUList.append(inventoryPLU)
            inventoryQuantityList.append(inventoryQuantity)
    else:
        for i in range(len(inventory)):
            inventorySplit = inventory[i].split()
            inventoryPLU = inventorySplit[0]
            inventoryQuantity = inventorySplit[-2]
            inventoryPLUList.append(inventoryPLU)
            inventoryQuantityList.append(inventoryQuantity)
            
    # Fix the file to include equiv PLUs

    for i in range(len(pluList)-1,-1,-1):
        currentPLU = pluList[i]
        masterListLocation = masterPLU.index(currentPLU)
        if masterEquivPLU[masterListLocation] != '0': # If there is an equiv, PLU isn't 0
            multQuantity = float(quantityList[i])*float(masterEquivQnt[masterListLocation]) # Makes the actual quantity
            newEquivPLU = masterEquivPLU[masterListLocation] # name of equiv PLU (now real PLU)
            try:
                pluListLocation = pluList.index(newEquivPLU) # finds location of PLU in presented list
                oldQnt = quantityList[pluListLocation] # pulls quantity from this memory location
                quantityList[pluListLocation] = float(multQuantity)+float(oldQnt) # adds the two quantities together into memory location               
            except ValueError:
                pluList.append(masterEquivPLU[masterListLocation])
                quantityList.append(multQuantity)
            pluList.pop(i) # destroys original PLU
            quantityList.pop(i) # destroys original Quantity
            

    # Add names and prices to new inventory

    nameList = []
    priceList = []
    for i in range(len(pluList)):
        currentPLU = pluList[i]
        masterListLocation = masterPLU.index(currentPLU)
        nameList.append(masterName[masterListLocation])
        priceList.append(masterPrice[masterListLocation])

    inventoryNameList = []
    inventoryPriceList = []


    for i in range(len(inventoryPLUList)):
        currentPLU = inventoryPLUList[i]
        try:
            beginListLocation = pluList.index(str(currentPLU))
            addedQuantity = float(quantityList[beginListLocation])
        except ValueError:
            addedQuantity = 0
        masterListLocation = masterPLU.index(currentPLU)
        currentQuantity = float(inventoryQuantityList[i])
        newQuantity = currentQuantity+addedQuantity
        inventoryQuantityList[i] = str(newQuantity)
        inventoryNameList.append(masterName[masterListLocation])
        inventoryPriceList.append(masterPrice[masterListLocation])

               
    createFile(pluList, nameList, quantityList, priceList, addFileName)
    print("An add inventory file has been created.")

    createFile(inventoryPLUList, inventoryNameList, inventoryQuantityList, inventoryPriceList, 'Master Inventory.txt')
    print("The inventory file has been updated.")
    input("Press 'Enter' to close")

main()

