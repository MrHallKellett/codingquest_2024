from collections import defaultdict

with open("day2.txt") as f:
    ACTUAL_DATA = f.read().splitlines()


TEST_DATA = '''45000377000000008306f39f0A000bc1d7253441
4500007f0000000005065de1c0a800b833c555ee
450002e50000000008061ef5c0a8796698721661
4500017e00000000b206e54e88c7fd4f0A00244c
45000164000000009d06d73c0A0000b7e0b143b8'''.splitlines()

EXPECTED = "868/1625"

INTERNAL = (192, 168)
PASSENGER = (10, 0)

def get_byte(data, start, amt):
    byte = data[start:start+(amt*2)]
    

    return int(byte, 16)
    

def solve(data):

    passenger = 0
    internal = 0
    
    for line in data:
        
        packet_length = get_byte(line, 4, 2)

        source = (get_byte(line, 24, 1), get_byte(line, 26, 1))
        dest = (get_byte(line, 32, 1), get_byte(line, 34, 1))
        
        
        if source == INTERNAL or dest == INTERNAL :
            internal += packet_length
        if source == PASSENGER or dest == PASSENGER :
            passenger += packet_length
            
        
        

    result = f"{internal}/{passenger}"

    print("Result obtained:", result)
    return result




if __name__ == "__main__":

    assert solve(TEST_DATA) == EXPECTED
    print("TEST PASSED!!!")

    
    print(solve(ACTUAL_DATA))



