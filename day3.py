from collections import defaultdict

with open("day3.txt") as f:
    ACTUAL_DATA = f.read().splitlines()[0]


TEST_DATA = '''12 6 4 1 9 5 5 1 9 1 7'''

EXPECTED = "F"


def solve(data):
    global line_length
    j = 0
    for i, thing in enumerate(data.split()):
        thing = int(thing)

        
        if i % 2 == 0:
            char = "."
        else:
            char = "#"
        for i in range(thing):
            print(char, end="")
            j += 1
            if j == line_length:
                print()
                j = 0

   





if __name__ == "__main__":
    line_length = 10
    solve(TEST_DATA) == EXPECTED
    print("TEST PASSED!!!")
    line_length = 100
    print()

    
    print(solve(ACTUAL_DATA))


