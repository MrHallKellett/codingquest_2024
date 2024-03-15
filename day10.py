from collections import defaultdict

with open("day10.txt") as f:
    ACTUAL_DATA = f.read().splitlines()



TEST_DATA = '''e3 c2 b1 c1 b4 a1 b2 a2'''.splitlines()

EXPECTED = 6

debug = True

def d_print(*s, sep=" ", end="\n"):
    if debug:
        
        print(sep.join(str(i) for i in s))
        print(end)


def flip(board, captures, player):

    for y, x in captures:
        try:
            board[y][x] = str(player) + "<"
        except:
            print(y, x, "fail")
            input()
    return recurse_capture(captures, board, player)

def recurse_capture(captures, board, player):
    for y, x in captures:
        board = capture(board, y, x, player)
    return board

def other(player):

    return str(int(not bool(int(player)-1)) + 1)

def capture(board, y, x, player):
    captured = []
    # downwards then upwards

    board = [[cell[0] for cell in row] for row in board]
    print("vertical check from", y, x)
    for r in [range(y+1, size), range(y-1, -1, -1)]:
        captured = []
        for a in r:
            if a < 0 or a >= size:
                break
            if board[a][x] == player:
                d_print("Hit player so enacted flip")
                board = flip(board, captured, player)
                
                break
            elif board[a][x] == other(player):
                d_print("Captured", a, x)
                captured.append((a, x))
            elif board[a][x] == ".":
                d_print("Capture unsuccessful")
                break
        else:
            d_print("Capture unsuccessful")

    # rightwards then leftwards
    
    print("horiz check from", y, x)
    for r in [range(x+1, size), range(x-1, -1, -1)]:
        captured = []
        
        for b in r:
            check = board[y][b]
            d_print("checking", y, b, "which is", check)
            print(board)
            if b < 0 or b >= size:
                break
            if board[y][b] == player:
                d_print(f"Hit player so enacted capture of {captured}")
                board = flip(board, captured, player)
                break
            elif board[y][b] == other(player):
                captured.append((y, b))
            elif board[y][b] == ".":
                d_print(f"Capture of {captured} unsuccessful")
                break
        else:
            d_print(f"Capture of {captured} unsuccessful")
            
    print("SE NW diag check from", y, x)
    for r in [range(1, size), range(-1, -size, -1)]:
        captured = []
        for d in r:
            nx, ny = x+d, y+d
            
            if nx >= size or ny >= size or nx < 0 or ny < 0:
                break
            check = board[ny][nx]
            
            if check == player:
                board = flip(board, captured, player)
                d_print(f"Hit player so enacted capture of {captured}")
            elif check == other(player):
                captured.append((ny, nx))
            elif check == ".":
                d_print(f"Capture of {captured} unsuccessful")
                break
        else:
            d_print(f"Capture of {captured} unsuccessful")

    
    print("NE diag check from", y, x)
    
    for d in range(1, size):
            nx, ny = x+d, y-d                
            if nx >= size or ny >= size or nx < 0 or ny < 0:
                break
            check = board[ny][nx]
            if check == player:
                board = flip(board, captured, player)
                d_print(f"Hit player so enacted capture of {captured}")
            elif check == other(player):
                captured.append((ny, nx))
            elif check == ".":
                d_print(f"Capture of {captured} unsuccessful")
                break
    else:
        d_print(f"Capture of {captured} unsuccessful")

    print("SW diag check from", y, x)
    for d in range(1, size):
            nx, ny = x-d, y+d                
            if nx >= size or ny >= size or nx < 0 or ny < 0:
                break
            check = board[ny][nx]
            if check == player:
                board = flip(board, captured, player)
                d_print(f"Hit player so enacted capture of {captured}")
            elif check == other(player):
                captured.append((ny, nx))
            elif check == ".":
                d_print(f"Capture of {captured} unsuccessful")
                break
    else:
        d_print(f"Capture of {captured} unsuccessful")

    display(None, board)
    return board

def display(move, board):

    s = "      "

    for i in range(1, size+1):

        s += hex(i)[2:] + " "
    s += "\n"
    for y, row in enumerate(board):
        s += str(chr(y+97)).ljust(5)

        for x, cell in enumerate(row):
            
            s += str(cell).ljust(2)

        s += "\n"

    print(s)
    print()
    
    


def validate(board, y, x, player):

    for y2 in range(-1, 2):
        for x2 in range(-1, 2):
            if y2 == 0 == x2:   continue
            
            
            nx = x2 + x
            ny = y2 + y

            if nx < 0 or ny < 0 or nx >= size or ny >= size:
                continue
            
            if board[ny][nx] == other(player):
                return True
    return False

def solve(data):

    totals = {'1':0, '2':0}

    board = [["." for _ in range(size)] for _ in range(size)]

    

    print("default board")

    for game_no, game in enumerate(data):

        mid = size//2
        board = [["." for _ in range(size)] for _ in range(size)]
        board[mid-1][mid-1] = '1'
        board[mid][mid-1] = '2'
        board[mid][mid] = '1'
        board[mid-1][mid] = '2'

        i = 0
        for move in game.split():

            

            print(move, "is the move")

            player = str(int(bool(i % 2))+1)

            y = ord(move[0]) - 97
            x = int(move[1:]) - 1
            print(y, x)


            board[y][x] = player

            board = capture(board, y, x, player)

            
            i += 1

            game = {'1':0, '2':0}
            for row in board:
                for cell in row:
                    if cell in totals.keys():
                        game[cell] += 1

            

        print(f"Game {game_no} over... results: ", game)
        input()
        totals['2'] += game['2']
        totals['1'] += game['1']
        
    result = totals['1']

    print("Result obtained:", result)
    return result


def tests():
    tests = {}

    with open("day10tests.txt") as f:
        data = f.read().splitlines()

    take = ""
    for line in data:
        if "test" in line:
            tests[line] = {'in':[], 'out':[]}
            this_test = line
        elif "," in line:
            tests[this_test]["move"] = tuple(map(int, line.split(",")))
        elif line == "in":
            take = "in"
        elif line == "out":
            take = "out"
        else:            
            tests[this_test][take].append(list(line))


    for name, test in tests.items():
        print(name)

        board = test['in']

        y, x = test['move']

        
        print("input...")
        display(None, board)
        board[y][x] = "2"
        print(board)
        board = capture(board, y, x, "2")
        print("output...")
        display(None, board)

        assert board == test['out']

        

if __name__ == "__main__":
    size = 6

    tests()

    size = 6

    assert solve(TEST_DATA) == EXPECTED
    size = 20
    print("TEST PASSED!!!")

    
    print(solve(ACTUAL_DATA))


