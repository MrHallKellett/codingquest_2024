from collections import defaultdict

with open("day1.txt") as f:
    ACTUAL_DATA = f.read().splitlines()


TEST_DATA = '''AAA: Seat 9997
BBB: Discount 2886
DDD: Luggage 3500
AAA: Tax 156
CCC: Fee 9468
BBB: Fee 9378
AAA: Discount 3103
DDD: Rebate 967'''.splitlines()

EXPECTED = 2533


def solve(data):

    costs = defaultdict(int)

    for line in data:

        key, thing, amt = line.split()

        amt  = int(amt)

            
        if "Discount" in line or "Rebate" in line:
            costs[key] -= amt
        elif any(i in line for i in "Meal,Seat,Luggage,Tax,Fee".split(",")):
            costs[key] += amt
        


    result = min(costs.values())

    print("Result obtained:", result)
    return result




if __name__ == "__main__":

    assert solve(TEST_DATA) == EXPECTED
    print("TEST PASSED!!!")

    
    print(solve(ACTUAL_DATA))


