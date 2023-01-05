## A battleship "port" By Turtle.ca 

# 1/4/2023 
#start the board functions and possibly the visuals?

def createEmptyBoard(columns,rows):
    emptyList = []
    for i in range(columns):
        emptyList.append([])
        for j in range(rows):
            emptyList[i].append([])
    return(emptyList)

def start():
    print(createEmptyBoard(10,10))

start()