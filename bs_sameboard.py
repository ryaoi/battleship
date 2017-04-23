from random import randint

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

board = []
end_flag = 0
retry = ""

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
	for row in board:
		print " ".join(row)

print "Let's play Battleship!"

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

"""
print ("---The answer---\nrow1:%d\ncol1:%d\n----------------") % (ship_row, ship_col)
"""
while (end_flag == 0):
    for turn in range(8):
        print bcolors.HEADER + ("Turn:%d Player:%d") % ((turn + 2) / 2, (turn) % 2 + 1) + bcolors.ENDC
        get_row = raw_input("Guess Row:")
        get_col = raw_input("Guess Col:")
	
        if(get_col == "" or get_row == ""):
            if (turn == 7):
                print  bcolors.FAIL + ("Game Over") + bcolors.ENDC
            else:
                print ("Missing input...")
            continue
        guess_row = int(get_row)
        guess_col = int(get_col)

        if guess_row == ship_row and guess_col == ship_col:
            print ("Congratulations! You sunk my battleship!")
            break
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print ("Oops, that's not even in the ocean.")
            elif(board[guess_row][guess_col] == "X"):
                print ("You guessed that one already.")
            else:
                print ("You missed my battleship!")
                if ((turn + 1) % 2 == 1):
                   board[guess_row][guess_col] = bcolors.OKBLUE + "X" + bcolors.ENDC
                else:
                   board[guess_row][guess_col] = bcolors.OKGREEN + "X" + bcolors.ENDC
                print_board(board)
            if (turn == 7):
                print bcolors.FAIL + ("Game Over") + bcolors.ENDC
                break
    if (end_flag == 0):
        retry = ""
        while (retry != "y" and retry != "n"):
            retry = raw_input("Retry?[y/n]")
            if (retry == ""):
                print ("Put something inside...")
            elif retry.lower() == "y":
                print ("Retry!!!")
            elif retry.lower() == "n":
                print ("No Retry")
                end_flag = 1
            else:
                print ("y or n?")
