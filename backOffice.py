##    backOffice.py
##
##    This script will run once per day at a predefined time on the pcDuino in
##    each store. It takes all of the newly created text files in Downloads
##    and moves them to a temporary folder. In the temp folder, it compares
##    each beginning file to the next, and generates a fake sales file for
##    every shift. This sales file is not the same as the file generated during
##    the shift report, but it will essentially add the error report into
##    the sales report.
##
##    After processing, it will make a list of each cashier and their sales.
##    These lists will be emailed to a list defined in 'emailList.txt', in addition
##    to the total beginning file for each cashier.

def main():
    dumpDirectory = '' # Where cashier files are dumped (generally /Downloads)
    tempDirectory = '' # Where processing can occur
    permDirectory = '' # Where files should be stored en-masse

    # Import statements
    import os
    import shutil
    import glob
    import pyFunctions01
    import smtplib
    import time
    import send_mail

    # Move files to temporary home
    tempSource = os.listdir(dumpDirectory)
    tempDestination = tempDirectory
    for files in tempSource:
        if files[0:3].isdigit(): # The first letters in a desired file are the year
            shutil.move(files,tempDestination)
    # Change directory to where the files currently are
    os.chdir(tempDirectory)

    # Make a list of beginFiles
    beginFileList = glob.glob('*BEGIN*.txt')
    fullFileList = glob.glob('*[AB][ED][GD]*.txt') # Selects add files
    if len(beginFileList) != len(fullFileList): # There are add files
        # Walk through the files, find the add file. Add the total of that to the total of the previous beginFile
        for i in range(len(fullFileList)):
            if fullFileList[i][20:23] != 'ADD':
                continue # i was not an add file
            else:
                addedBegin = fullFileList[i-1]
                addToAdd = fullFileList[i]
                myFile = open(addedBegin,'r')
                beginList = myFile.readlines()
                myFile.close()
                beginQuantity = beginList.pop()
                beginQuantity = beginQuantity.split()
                beginQuantity = float(beginQuantity[0])

                myFile = open(addToAdd,'r')
                addList = myFile.readlines()
                myFile.close()
                addQuantity = addList.pop()
                addQuantity = addQuantity.split()
                addQuantity = float(addQuantity[0])

                newBeginQuantity = beginQuantity + addQuantity

                myFile = open(addedBegin,'w')
                myFile.write(beginList)
                myFile.write(str("\n"))
                myFile.write(str(newBeginQuantity))
                myFile.close()
    
    # Compare those beginFiles to eachother
    currentSalesList = []
    currentNameList = []
    currentBeginList = []
    for i in range(len(beginFileList)-1):
        currentFile = beginFileList[i]
        nextFile = beginFileList[i+1]

        # Read the first file
        myFile = open(currentFile,'r')
        currentList = myFile.readlines()
        myFile.close()
        currentQuantity = currentList.pop()
        currentQuantity = currentQuantity.split()
        currentQuantity = currentQuantity[0] # Gets the total

        # Read the second file
        myFile = open(nextFile,'r')
        nextList = myFile.readlines()
        myFile.close()
        nextQuantity = nextList.pop()
        nextQuantity = nextQuantity.split()
        nextQuantity = nextQuantity[0]

        # Compare the first list to the second

        currentSales = float(currentQuantity) - float(nextQuantity)
        currentName = str(currentFile[26:])

        currentSalesList.append(str(currentSales))
        currentNameList.append(str(currentName))
        currentBeginList.append(str(currentQuantity))

    # Combine the two lists together into one list to email
    emailList = ''
    for i in range(len(currentNameList)):
        emailValue = str(currentNameList[i]) + ',' + str(currentSalesList[i]) + ',' + str(currentBeginList[i]) + str("\n")
        emailList = emailList + emailValue

    # Move files to permanent home
    # Save last beginFile, because it isn't closed yet
    lastBegin = beginFileList[-1]
    lastBegin = dumpDirectory + '/' + lastBegin
    shutil.move(lastBegin,dumpDirectory)
    # Move the processed files from temp to perm
    permSource = os.listdir(tempDirectory)
    permDestination = permDirectory
    for files in permSource:
        if files[0:3].isdigit(): # the first letters in the desired file are the year
            shutil.move(files,permDestination)

    send_mail.send_mail(FROM, TO, SUBJECT, TEXT, FILE)
            
##    # send eMail
##    SERVER = "localhost"
##
##    FROM = "jonestown_cig@kfs.com"
##
##    # read list of emails, put in list named "emailNameList"
##
##    TO = emailNameList
##    date = time.strftime("Y,%m,%d")
##    SUBJECT = "Cig Inventory" + str(date)
##
##    TEXT = emailList
##    
##    message = """\
##    From: %s
##    To: %s
##    Subject: %s
##
##    %s
##    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
##
##    server = smtplib.SMTP(SERVER)
##    server.sendmail(FROM, TO, message)
##    server.quit()

main()













    
