# This code was written by Braxton Eidem

import sys

class Ride:
    def __init__(self, name, age):
    self.name = name
    self.start = start 
    self.end = end 


def new_File(fileName):
    rides = []
    with open(fileName) as f:
        line = f.readline()
        cur_line = line.strip()
        castle_values = cur_line.split(' ')
        for i in castle_values:


            
            ride = Ride(name, start, end)
            rides.append(i)

    return rides








#main driver of the program. reads through the args list to get all files 
#example: python3 prog2_algo.py test1.txt

rides = []
rides = new_File(sys.argv[1])
print('rides: ', rides)