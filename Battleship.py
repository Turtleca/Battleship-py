## A battleship "port" By Turtle.ca 

# 1/4/2023 
#start the board functions and possibly the visuals?

#create an empty list of specified dimentions
#int, int
def createEmptyBoard(columns,rows):
    emptyList = [" "]
    for i in range(rows):
        emptyList.append([" "])
        for j in range(columns):
            emptyList[i].append([" "])
    return(emptyList)
#list

#places ships in specified locations on a board
#int, string, list
def ShipCreation(shipClass,position,board): #position string in format "e40" "row, column, direction". shipClass either int or ship name
    if shipClass == 0:
        shipLetter = "P"

#edited list

#Main function
#n/a
def main():
    pass
#n/a

main()