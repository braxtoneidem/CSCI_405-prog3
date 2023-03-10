# This code was written by Braxton Eidem

import sys


# Python3 code here creating class
class geeks:
	def __init__(self, name, roll):
		self.name = name
		self.roll = roll

class Node:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start 
        self.end = end 

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


        print(ride_name[1])
        #get first start
        vertex = ride_name[1]
        vertexTrim = vertex[1:4] 
        vertexTrim = vertexTrim.split(',')
        start = int(vertexTrim[0])
        end = int(vertexTrim[1])


        # appending instances to list
        rides.append(Node(name, start, end))

print("\t\t\t\t\t|0|1|2|3|4|5|6|7|8|")
print("\t\t\t\t\t-------------------")
for obj in rides:
    print(f"{obj.name:10}  ==> {obj.start:2d}:00 - {obj.end:2d}:00", end ="\t\t|") 
    printX((obj.start))
    printO((obj.end - obj.start))
    printX((9-obj.end))

    print()
    



   




# # Accessing object value using a for loop
# for obj in list:
# 	print(obj.name, obj.roll, sep=' ')

print("")
# # Accessing individual elements
# print(list[0].name)
# print(list[1].name)
# print(list[2].name)
# print(list[3].name)
