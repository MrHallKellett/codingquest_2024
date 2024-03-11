from collections import defaultdict
from string import ascii_lowercase
with open("day6.txt") as f:
    ACTUAL_DATA = f.read()



TEST_DATA = """Cipher key: helloworld

Message: wp nehslv ewgw"""

EXPECTED = "et phonex home"

def solve(data):

    data = data.replace("Cipher key: ", "").replace("Message: ", "")

    key, msg = data.split("\n\n")

    msg = msg.replace(" ", "")

    msg = msg.replace("j", "i")

    msg = msg.split()
    result = ""

    new_msg = ""
    for w in msg:
        if len(w) % 2 == 1:
            w += "x" if w[0] != "x" else "q"
        new_msg += " " + w

        '''rmqfgs yegv em qnpu pdml dc atuy olzy anpu'''
        
        print(new_msg)


    new_msg = new_msg.replace(" ", "")

    
    letters = key + ascii_lowercase

    letters = letters.replace("j", "i")
    used = set()
    i = 0

    grid = [[]]
    for char in letters:

        if char in used:
            continue

        used.add(char)

        i += 1
        
        grid[-1].append(char)
        if i % 5 == 0 and i < 25:
            grid.append([])

    
    for row in grid:
        print(row)

    for i in range(0, len(new_msg), 2):

        pair = new_msg[i:i+2]


        

        locs = []
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell in pair:
                    locs.append((y, x))

                    

        if locs[0][0] == locs[1][0]:
            print("same row")
            for loc in locs:
                y, x = loc
                result += grid[y][x-1]

        elif locs[0][1] == locs[1][1]:
            print("same col")
            for loc in locs:
                y, x = loc
                result += grid[y-1][x]

        else:
            print("diff")
            y1, x1 = locs[0]
            y2, x2 = locs[1]
            result += grid[y1][x2]
            result += grid[y2][x1]
            

        print(pair)
        print(result)
        input()
                      
                    

    print("Result obtained:", result)
    return result




if __name__ == "__main__":

    #assert solve(TEST_DATA) == EXPECTED
    print("TEST PASSED!!!")

    
    print(solve(ACTUAL_DATA))


