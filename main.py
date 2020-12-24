# Make a game of tictactoe using a 2 dimensional Array

array = ["."] * 3
for i in range(0, 3):
    array[i] = ["."] * 3


def display(array):
    print("  1", "2", "3")
    print("1", " ".join(array[0]))
    print("2", " ".join(array[1]))
    print("3", " ".join(array[2]))

def p1turn(array):
    while True:
        print("Player 1's Turn")
        x = int(input("Input column"))
        y = int(input("Input row"))
        if array[y - 1][x - 1] == ".":
            array[y - 1][x - 1] = "O"
            break
        else:
            print("That position is taken")

def p2turn(array):
    while True:
        print("Player 2's Turn")
        x = int(input("Input column"))
        y = int(input("Input row"))
        if array[y - 1][x - 1] == ".":
            array[y - 1][x - 1] = "X"
            break
        else:
            print("That position is taken")

def checkwin(array):
    for i in range(0, 3): # horizontal check
        if array[i][0] == array[i][1] == array[i][2] and "." not in array[i]:
            if array[i][i] == "O":
                return 0
            elif array[i][i] == "X":
                return 1
    for e in range(0, 3): # vertical check
        if array[0][e] == array[1][e] == array[2][e] and "." not in array[e][e]:
            if array[e][e] == "O":
                return 0
            elif array[e][e] == "X":
                return 1
    if array[0][0] == array[1][1] == array[2][2] and "." not in array[0][0]:
        if array[0][0] == "O":
            return 0
        elif array[0][0] == "X":
            return 1
    if array[0][2] == array[1][1] == array[2][0] and "." not in array[0][2]:
        if array[0][2] == "O":
            return 0
        elif array[0][2] == "X":
            return 1


display(array)
while True:
    p1turn(array)
    display(array)
    if checkwin(array) == 0:
        print("Player 1 is the winner!")
        break
    p2turn(array)
    display(array)
    if checkwin(array) == 1:
        print("Player 2 is the winner!")
        break
