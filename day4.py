from collections import defaultdict
from math import inf, sqrt
from re import findall

with open("day4.txt") as f:
    ACTUAL_DATA = f.read().splitlines()


TEST_DATA = '''System                                  Dist         X         Y         Z
Proxima Centauri                       4.247     2.945    -3.056    -0.143
Barnard's star                         5.963     4.958     2.980     1.449
Luhman 16 A                            6.503     1.697    -6.249     0.600
WISE J085510.83-071442.5               7.532    -3.967    -5.664     2.985
Wolf 359                               7.856    -1.916    -3.938     6.522'''.splitlines()

EXPECTED = 3.508


def solve(data):


    stars = {}
    for line in data:

        star = True
        

        s = ""

        for c in line.split():



            try:
                assert "." in c
                x = float(c)

                if s in stars:
                    stars[s].append(x)
                else:
                    stars[s] = [x]

                
                

            except:

                s += c

                
                
            

            
            

    

    lowest = inf

   
    for star in stars.values():
        
        
        _, x1, y1, z1 = map(float, star)

        
        for other in stars.values():
            if star == other:
                continue
            _, x2, y2, z2 = map(float, other)
        
            dist = sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
            if dist < lowest:
                lowest = dist
                print("new lowest", lowest)
    print("lowest", lowest)
    return round(lowest, 3)



if __name__ == "__main__":

    assert solve(TEST_DATA) == EXPECTED
    print("TEST PASSED!!!")

    
    print(solve(ACTUAL_DATA))


