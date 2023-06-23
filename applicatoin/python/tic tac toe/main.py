bourd = ["-", "-","-",
         "-", "-", "-",
         "-","-","-"]
current_player = "x"
winner = None
gamerunning = True

def printbourd(bourd):
    print(bourd[0]+ " | " + bourd[1] + " | " + bourd[2])
    print("----------")
    print(bourd[3]+ " | " + bourd[4] + " | " + bourd[5])
    print("----------")
    print(bourd[6]+ " | " + bourd[7] + " | " + bourd[8])

printbourd(bourd)

def playerInput(board):
    inp = int(input("Select a spot 1-9: "))
    if board[inp-1] == "-":
        board[inp-1] = current_player
    else:
        print("Oops player is already at that spot.")

def switchPlayer():
    global current_player
    if current_player == "x":
        current_player = "o"
    else:
        current_player = "x"


        
while gamerunning:
    printbourd(bourd)
    playerInput(bourd)
    switchPlayer()

