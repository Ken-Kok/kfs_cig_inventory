## This program is a small program which provides supporting files in order to
## aid in the development of other programs, especially in the realm of data
## processing.
##
## Read the directions under each file for more information.

def combineList(list1,list2,operation):
    # This program performs the requested operation on elements of list2 assuming that
    # their respective list1 elements match. For instance, if the operation was 0, for
    # addition, list1 = [1,2,3,1] and list2 = [1,2,3,5], the return lists would be
    # list1 = [1,2,3] and list2 = [6,2,3]. This is useful in any type of data processing
    # when combining like indexes is desired, such as database related work.

    # for addition, operation = 1
    # for multiplication, operation = 2
    # for subtraction (subtract all later indexes from first), operation = 3
    # for division (divide the addition of all but the direct index by the
    # first), operation = 4
    

    # Creates a list of non-repeated inputs
    newList1 = []
    newListLocation = []
    for i in list1:
        try: # if this statement isn't a value error, newList already contains list1
            newList1.index(i)
            # contained already, pass over this value
            continue
        except ValueError: # the element must not be contained in the newList already.
            newList1.append(i)
            # Grab the location of the added item
            # This is a list of the first locations of added elements
            newListLocation.append(list1.index(i))
    listOccurances = []
    for i in newList1:
        # Counts the number of occurances there are of each index in the list
        # Also keeps these values in order according to first occuring index
        # For list1 = [1,2,1,3,2], listOccurances = [2,2,1]
        listOccurances.append(list1.count(i))

    firstQuantityList= []
    for i in newListLocation:
        # Keeps track of the first index of each value in list2
        # For list1 = [1,2,1,3,2] and list2 = [5,3,6,8,8],
        # fistQuantityList = [5,3,8]
        firstQuantityList.append(list2[i])

    list2Reorder = []
    for currentIndex in newList1:
        # Reorders list2 such that it is the order of newList1
        for i in (i for i,x in enumerate(list1) if x == currentIndex):
            list2Reorder.append(list2[i])
    if int(operation) == 1:
        list2Added = []
        # Add together the elements of list2Reorder based on listOccurances
        counter = 0
        added = 0
        for n in listOccurances:
            added = 0
            for i in range(n):
                added = added + float(list2Reorder[counter])
                counter = counter + 1
            list2Added.append(added)
            
        return newList1, list2Added
    
    elif int(operation) == 2:
        list2Mult = []
        # Multiple together the elements of list2Reorder based on listOccurances
        counter = 0
        mult = 1
        for n in listOccurances:
            mult = 0
            for i in range(n):
                mult = mult + float(list2Reorder[counter])
                counter = counter + 1
            list2Mult.append(mult)

        return newList1,list2Mult

    elif int(operation) == 3:
        list2Sub = []
        # Subtract the elements of list2Reorder based on listOccurances
        counter = 0
        sub = 0
        for n in listOccurances:
            sub = 0
            for i in range(n):
                sub = sub - float(list2Reorder[counter])
                counter = counter + 1
            list2Sub.append(sub)
        newList2Sub = []
        for i in range(len(list2Sub)):
            # Add back the starting element
            newValue = float(list2Sub[i]) + (2*float(firstQuantityList[i]))
            newList2Sub.append(float(newValue))

        return newList1, newList2Sub

    elif int(operation) == 4:
        list2Div = []
        # Adds the elements of list2Reorder based on listOccurances
        counter = 0
        div = 0
        for n in listOccurances:
            added = 0
            for i in range(n):
                div = div + float(list2Reorder[counter])
                counter = counter + 1
            list2Div.append(div)
        divList2Div = []
        for i in range(len(list2Div)):
            # Remove the first element
            newValue = list2Div - firstQuantityList[i]
            divList2Div.append(newValue)
        newList2Div = []
        for i in range(len(divList2Div)):
            # Divide by the starting element)
            newValue = firstQuantityList[i]/divList2Div[i]
            newValue.append(newList2Div)

        return newList1, newList2Div

        

def playWav(wavFile):
    # This program plays a desired .wav file, into the computer's default
    # audio port

    import wave,sys,pyaudio
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





























    



