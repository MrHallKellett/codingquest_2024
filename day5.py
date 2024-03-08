from collections import defaultdict

with open("day5.txt") as f:
    ACTUAL_DATA = f.read().splitlines()


TEST_DATA = '''        base    ta00    cx22    xj84
base       0   55457   63529   61302
ta00   55457       0  111890   35768
cx22   63529  111890       0   98977
xj84   61302   35768   98977       0

Rover 1 route: base -> cx22 -> ta00 -> base -> xj84 -> base'''.splitlines()

EXPECTED = 353480



def solve(data):

    headers = data[0].split()
    print(headers)

    dists = {}

    matrix = True

    rovers = {}

    for line in data[1:]:
        print(line)

        if len(line.strip()) == 0:
            matrix = False
            continue

        if matrix:

            place = line.split()[0]
            dists[place] = list(map(float, line.split()[1:]))

        else:
            rover, route = line.split(":")
            rovers[rover] = route.split(" -> ")

    tot = 0
    for rover, stops in rovers.items():
        last = "base"

        for s in stops:
            s = s.strip()

            i = headers.index(s)

            tot += dists[last][i]

            last = s

        
    result = tot
        

        

        

        



        
        

   

    print("Result obtained:", result)
    return result




if __name__ == "__main__":

    assert solve(TEST_DATA) == EXPECTED
    print("TEST PASSED!!!")

    
    print(solve(ACTUAL_DATA))


