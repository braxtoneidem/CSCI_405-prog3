# This code was written by Braxton Eidem

import sys

# Python3 code here creating class
class Node:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start 
        self.end = end 
        self.edges = []

    def printEdges(self):
        print(self.name)
        for edge in self.edges:
            print("  edge: ", edge.name)

              
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
list = []
rides = []

# g = Graph()

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

printInfo(rides)

# make the graph connections  
for mainNode in rides:
    mainNodeStart = mainNode.start
    mainNodeEnd = mainNode.end
    print(f"{mainNode.name:10}  ==> {mainNodeStart:2d}:00 - {mainNodeEnd:2d}:00") 

    #find main node start and end 
    for node in rides:
        nodeStart = node.start
        nodeEnd = node.end

        if(mainNodeEnd <= nodeStart):
            # print("  :", mainNode.name)
            # print(f"    {node.name:10}: {nodeStart:2d}:00 - {nodeEnd:2d}:00") 
            mainNode.edges.append(node)
            #print("Connecting: ", node.name, " to: ", mainNode.name)
            #print(mainNode.name, " is now connected to: ", len(mainNode.edges), " other nodes")

for mainNode in rides:
    mainNode.printEdges()