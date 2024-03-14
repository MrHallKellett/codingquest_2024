from collections import defaultdict
from math import inf as INF
from copy import copy
with open("day9.txt") as f:
    ACTUAL_DATA = f.read()


TEST_DATA = '''
#####################
S...............#...#
###########.###.#.#.#
#...#.......#.#...#.#
#.#.#.#######.#####.#
#.#..$#.#.$....$....#
#.#####.#.#######.###
#.#.......#.....#.#.#
#.#########.###.#.#.#
#.#...........#.#...#
#.#.#$####$.###$###.#
#...#.....#.#...#...#
#.###.###.###.#.#.###
#...#.#.....#.#.#...#
#####################
#.#.#$..#.$...#$..#.#
#.#.###.###.#.#.###.#
#...#...#...#.....#.#
#.###.###.#.#####.#.#
#...#.....#.........G
#####################
xxx
#####################
#.........#.........#
#.###.###.#########.#
#.......#...........#
#######.###########.#
#....$#...$....$....#
#.###.#####.#######.#
#.#.........#.......#
#.#####.#.#.#.#####.#
#...#...#.#.#.#...#.#
###.#$###.$.#.#$#.#.#
#...#.#.#.#...#.#.#.#
#.#.#.#.#.###.#.#.#.#
#.#.....#.........#.#
#.#####.###.#####.#.#
#....$#...$.#..$..#.#
#.###.#.###.#.#####.#
#...#...#.....#.....#
###.#####.#####.#####
#.......#...........#
#####################'''.strip()

EXPECTED = 53

def detect_junction(y, x, w, h, floor):
    
    count = 0
    for y2, x2 in ((-1, 0), (0, -1), (1, 0), (0, 1)):

        nx = x + x2
        ny = y + y2

        if nx < 0 or nx >= w or ny < 0 or ny >= h:
            continue

        if floor[ny][nx] == ".":
            count += 1

    return count

        
graph = {}

class Node:
    def __init__(self, x, y, z, symbol):
        self.symbol = symbol
        self.value = (x, y, z)
        self.connections = {}

    def add_connection(self, neighbour, weight):
        if neighbour == self:
            raise Exception("canny connect to mself")
        self.connections[neighbour] = weight

    def __repr__(self):
        return f"{self.value}"

        
        

def get_or_make_node(x, y, z, symbol):
    value = (x, y, z)
    node = graph.get(value)

    if node is None:
        node = Node(*value, symbol)
        graph[value] = node

    return node

def find_connections(vertex, floors):
    w = len(floors[0][0])
    h = len(floors[0])
    q = [(vertex.value, 0, set())]

    if vertex.symbol == "$":
        neighbour = list(vertex.value)
        neighbour[-1] = int( not bool(neighbour[-1]))
        neighbour_vertex = graph.get(tuple(neighbour))
        vertex.add_connection(neighbour_vertex, 0)
        print(f"Connected lift vertex {vertex} to neighbouring level vertex {neighbour_vertex}")
        

    
    while q:
        
        current, steps, path = q.pop(-1)

        path.add(current)
        
        x, y, z = current

        
        dead_end = True
        for y2, x2 in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                nx = x+x2
                ny = y+y2
                neighbour = (nx, ny, z)

                if (nx, ny, z) in path:                    
                    continue

                
        
                neighbour_vertex = graph.get(neighbour)
                if neighbour_vertex != vertex and neighbour_vertex is not None:
                    
                    vertex.add_connection(neighbour_vertex, steps+1)
                    #print(f"Discovered neighbour for {vertex} - the vertex at {neighbour_vertex} is {steps+1} steps away")
                    #display(path, floors, highlight=vertex)
                    
                else:

                    if nx < 0 or nx >= w or ny < 0 or ny >= h:
                        continue
                    
                    if floors[z][ny][nx] in ".$GE":
                        dead_end = False
                        
                        q.append((neighbour, steps+1, copy(path)))
        if dead_end:
            steps -= 1
            path.remove(current)
                    
    print("dfs over")


def display(vertices, floors, highlight=None):
    
    for z, floor in enumerate(floors):
        print("floor", z)
        s =""
        for y, row in enumerate(floor):
            s += str(y).ljust(5)
            for x, cell in enumerate(row):
                if highlight and highlight.value == (x, y, z):
                    s += "X"
                elif (x, y, z) in vertices:
                    s += "◘"
                else:
                    s += cell
            s += "\n"
        print(s)
    input()


def find_shortest_path(graph, origin, destination, floors):
    origin = graph[(0, 1, 0)]


    # set up table
    table = {n:{"node":str(n), "cost":INF if n is not origin else 0, "prev":"", "calc":""} for n in graph.values()}                        



    unvisited = list(graph.values())

    visited = []

    print(len(unvisited), "left to visit")

    while len(unvisited):

            smallest = INF
            current_node = None

            ## find the unvisited vertex with smallest known distance from the origin
            for node, data in table.items():
                    if node not in unvisited:        continue
                    if data["cost"] <= smallest:
                            smallest = data["cost"]
                            current_node = node
            print("The current vertex is", current_node)

            ## find each unvisited neighbour of the current vertex

            for neighbour, distance in current_node.connections.items():
                    print(f"{current_node} is connected to {neighbour} {type(neighbour)}")
                    if neighbour not in unvisited:
                            print("Already visited")
                    else:
                            
                            ## calculate total distance from origin node
                            tot = distance

                            calc = str(tot)
                            # until we've got back to the start

                            
##                            print(f"We need to make it back from {current_node} to {origin}")
                            pitstop = table[current_node]["cost"]
##                            print(f"Came via {current_node} and that cost {pitstop}")
                            tot += pitstop
                            calc += " + " + str(pitstop)
##                            print(f"so the total is now {tot}")


                            if tot <= table[neighbour]["cost"]:
                                    table[neighbour]["prev"] = current_node                                                        
                                    table[neighbour]["cost"] = tot                                                                                                              
                                    table[neighbour]["calc"] = calc
                                   
##                                    for node, data in table.items():
##                                            print(
##                                                    f'{str(node)} \t\t {data["cost"]} \t\t {data["prev"]} \t\t {data["calc"]}')
##
##                                    print()
##                            else:
##                                    print(f"{tot} was not shorter. table not updated")
            unvisited.remove(current_node)


    for node, data in table.items():
            print(
                    f'{str(node)} \t\t {data["cost"]} \t\t {data["prev"]} \t\t {data["calc"]}')

    print()

    node = destination

    
    path = [str(destination)]

    cost = table[node]["cost"]

    while node is not origin:
            print(table[node])
            
            node = table[node]["prev"]
            
            
            path.append(node.value)


    

    display(path, floors)
    

    return cost + off_by
            

def solve(data):
    

    floors = [f.strip().splitlines() for f in data.split("xxx")]

    VERTEX_MARKERS = "SG$"

    # mark vertices
    for z, floor in enumerate(floors):
        w = len(floor[0])
        h = len(floor)
        print("floor", z)
        for y, row in enumerate(floor):
            for x, cell in enumerate(row):
                
                if cell in VERTEX_MARKERS or (cell == "." and detect_junction(y, x, w, h, floor) > 2):
                    node = get_or_make_node(x, y, z, cell)
                    if cell == "S":
                        origin = node
                    elif cell == "G":
                        destination = node
                    print(f"Found a vertex at floor {z} row {y} col {x}")


    # display


    display(graph.keys(), floors)
    

    
    # dfs from every vertex to find every other vertex

    for vertex in graph.values():
        find_connections(vertex, floors)

        print(vertex, "connected to:")
        for conn, weight in vertex.connections.items():
            print(conn, "in", weight, "steps")
        #display([v.value for v in vertex.connections.keys()], floors, highlight=vertex)
        


    


    # find shortest path

    
                
                

            

            

    result = find_shortest_path(graph, origin, destination, floors)

   

    print("Result obtained:", result)
    input()
    return result




if __name__ == "__main__":
    #goddamnit
    off_by = 1

    assert solve(TEST_DATA) == EXPECTED
    print("TEST PASSED!!!")

    off_by = 2

    
    print(solve(ACTUAL_DATA))


    input()
