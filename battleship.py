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

board1 = []
board2 = []

for x in range(5):
    board1.append(["O"] * 5)
    board2.append(["O"] * 5)

def print_board(board):
	for row in board:
		print " ".join(row)

print "Let's play Battleship!"

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row1 = random_row(board1)
ship_col1 = random_col(board1)
ship_row2 = random_row(board2)
ship_col2 = random_col(board2)

"""
print ("---The answer---\nrow1:%d\ncol1:%d\n----------------") % (ship_row1, ship_col1)
print ("---The answer---\nrow2:%d\ncol2:%d\n----------------") % (ship_row2, ship_col2)

"""
for turn in range(8):
    print bcolors.HEADER + ("Turn:%d Player:%d") % ((turn + 1) / 2, (turn) % 2 + 1) + bcolors.ENDC
    if ((turn + 1) % 2 == 1):
        board = board1
        ship_row = ship_row1
        ship_col = ship_col1
    else:
        board = board2
        ship_row = ship_row2
        ship_col = ship_col2
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
            board[guess_row][guess_col] = "X"
            if ((turn + 1) % 2 == 1):
                print bcolors.OKBLUE
            else:
                print bcolors.OKGREEN
            print_board(board)
            print bcolors.ENDC
        if (turn == 7):
            print bcolors.FAIL + ("Game Over for both of you") + bcolors.ENDC
