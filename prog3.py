# This code was written by Braxton Eidem

import sys
import copy
# Python3 code here creating class
class Node:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start 
        self.end = end 
        self.edges = []
        self.endNode = 1

    def printEdges(self):
        print(self.name, "edge count: ", len(self.edges), "end node: ", self.endNode)

        for edge in self.edges:
            print(f"  edge {edge.name:10}")

              
def printO(number):
      i = 0
      while i < number:
         print('O|', end ="")
         i = i+1

def printX(number):
      i = 0
      while i < number:
         print('x|', end ="")
         i = i+1

def printInfo(rides):
    print("\t\t\t\t\t|0|1|2|3|4|5|6|7|8|")
    print("\t\t\t\t\t-------------------")

    for obj in rides:
        print(f"{obj.name:10}  ==> {obj.start:2d}:00 - {obj.end:2d}:00", end ="\t\t|") 
        printX((obj.start))
        printO((obj.end - obj.start))
        printX((9-obj.end))
        print()
    print()

#main driver of the program. reads through the args list to get all files 
#example: python3 prog2_algo.py test1.txt

# creating list
rides = []

with open(sys.argv[1]) as f:
    line = f.readline()
    cur_line = line.strip()
    ride_values = cur_line.split(' ')

    for i in ride_values:
        name = "-1"
        start = -1
        end = -1

        #get name
        ride_name = i.split(':')
        name = ride_name[0]

        #get first start
        vertex = ride_name[1]
        vertexTrim = vertex[1:4] 
        vertexTrim = vertexTrim.split(',')
        start = int(vertexTrim[0])
        end = int(vertexTrim[1])

        # appending instances to list
        rides.append(Node(name, start, end))


# make the graph connections  
for mainNode in rides:
    mainNodeStart = mainNode.start
    mainNodeEnd = mainNode.end

    #find main node start and end 
    for node in rides:
        nodeStart = node.start
        nodeEnd = node.end

        if(mainNodeEnd <= nodeStart):
            # print("  :", mainNode.name)
            # print(f"    {node.name:10}: {nodeStart:2d}:00 - {nodeEnd:2d}:00") 
            mainNode.edges.append(node)
            mainNode.endNode = 0
            #print(mainNode.name, " is now connected to: ", len(mainNode.edges), " other nodes")


#printable statistics 
printInfo(rides)
# for mainNode in rides:
#     mainNode.printEdges()

# BREATH FIRST SEARCH

stack = []
maxSumTime = -1
bestPath = []

# breath first search
for rootNode in rides:
    path = []
    path.append(rootNode)
    stack.append(path)


while(len(stack) != 0):
    tom = stack.pop()
    height = len(tom)

    #check to see if last in *list* is an end node
    if tom[height-1].endNode == 1: 
        # sum up ride time
        sumTime = 0
        for child in tom:
            sumTime = sumTime + (child.end - child.start)
        # Check to see if this path has the best time
        if(sumTime > maxSumTime):
            bestPath = tom
            maxSumTime = sumTime
    else:
        # check to see if this is the end of the list
        for child in tom[height-1].edges: 
            tim = copy.deepcopy(tom)
            tim.append(child)
            stack.append(tim)

print("best time: ", maxSumTime)
print("best path: ", end = "")
for obj in bestPath:
    print(obj.name, end =", ")