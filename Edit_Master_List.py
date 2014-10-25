

def main():

    while True:

        # 1.) Receive PLU Code
        # 2.) Find PLU within a text file 'Master PLU List'
        # 3a.) If PLU is not found, add a new entry (name, price)
        # 3b.) If PLU is found, edit name and price

        print("Type 'END' into any entry to end the program")

        pluName = input("What PLU would you like to be used? ")
        if pluName == 'END':
            break
        
        nameName = input("What is the new/revised name of the PLU? ")
        if nameName == 'END':
            break
        print("What is the price of the PLU?")
        price = input("If the PLU has an equiv PLU, enter the price of the equiv PLU (such as pack price if the PLU is a carton): ")
        if price == 'END':
            break
        print("Does the PLU have an equiv. PLU (such as a carton - pack relationship)? ")
        equivPLU = input("If yes, enter the equiv PLU. If no, enter 0: ")
        equivPLU = str(equivPLU)
        if equivPLU != '0':
            equivQuantity = input("Please enter the quantity equiv (for instance, if the PLU is a carton of cigs, this value is 10): ")
            price = float(price) * int(equivQuantity)
            price = round(price,2)
        else:
            equivQuantity = 1
        
                      
        
        
        print()

        inFile = open('Master PLU List.txt', "r")
        data = inFile.readlines()
        inFile.close()

        counter = 0
        for i in range(len(data)):
            
            if data[i].find(pluName)==0:
                # If true, found PLU in list already
                data[i] = str(pluName)+" "+str(nameName)+" "+str(price)+" "+str(equivPLU)+" "+str(equivQuantity)+str("\n")
                break
                # If false, PLU is not in the list
            counter = counter + 1
        if counter == len(data):
            data.append(str(pluName)+" "+str(nameName)+" "+str(price)+" "+str(equivPLU)+" "+str(equivQuantity)+str("\n"))
##            if equivPLU == '0':
##                data2.append(str(pluName)+" "+str(nameName)+" "+'0'+" "+str(price)+str("\n"))
##        data2.append(priceSum)
        
    # Find inventory file, make two lists of PLUs and Quantities

        inventoryFile = open('Master Inventory.txt', 'r')
        inventory = inventoryFile.readlines()
        inventoryFile.close()

        inventoryPLUList = []
        inventoryQuantityList = []

        try:
            inventoryTest = inventory[-1].split()
            if len(inventoryTest) < 3:
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
        except IndexError:
            pass

        try:
            inventoryLocation = inventoryPLUList.index(pluName)
        except ValueError:
            if equivPLU == '0':
                inventory.append(str(pluName)+" "+str(nameName)+" "+'0'+" "+str(price)+str("\n"))
                
            
            
        
        print()
        inFile = open('Master PLU List.txt', "w")
        for i in range(len(data)):
            inFile.write(data[i])
        inFile.close()
        print("The Master List has been updated.")
        inFile = open('Master Inventory.txt',"w")
        for i in range(len(inventory)):
            inFile.write(inventory[i])
        inFile.close()
        print("The Inventory List has been updated.")
        print()
    input("Press 'Enter' to close")
        

main()





















