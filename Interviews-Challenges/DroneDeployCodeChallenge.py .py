"""
Drone Airspace Coding Challenge:
Given a square airspace, 128km x 128km, and N=10,000 Drones occupying the
airspace, our challenge is to effeciently compute how many drones are flying
too close to one another for safety.

Drone positions will be provided as an Nx2 array of [x,y] coordinates (in meters).

Drones must maintain a horizontal separation of radius 0.5km from other 
drones. If a drone is within 0.5km of another drone, both are "in conflict".

Have check_for_conflicts return the total number of drones who are in a conflicted
state (not the total number of conflicts).

DO all your work and testing in coderpad (no copy/pasting).

Coding style, readability, scalability, and documentation all matter!
Consider the computational complexity of your solution. The N^2 answer can 
be coded up in 5 minutes and 10 lines; we'd like to see something better!
"""


import random
import math
import itertools
random.seed(1)  # Setting random number generator seed for repeatability


NUM_DRONES = 10000
AIRSPACE_SIZE = 128000  # Meters.
CONFLICT_RADIUS = 500  # Meters.


def check_for_conflicts(drones, conflict_radius):
    num_drones_in_conflict = []
    total=0
    
    #combinations as to not compare ones already compared
    for drone1, drone2 in itertools.combinations(drones, 2): 
        print(drone1, drone2)
        
        #if either x or y coordinate difference are in radius
        if abs(drone1[0]-drone2[0]) <= conflict_radius or abs(drone1[1]-drone2[1]) <= conflict_radius:
            #append difference of coordinates 
            num_drones_in_conflict.append(drone1[0]*2-drone1[1])
            num_drones_in_conflict.append(drone2[0]*2-drone2[1])
            #no two drones should have same combination of x*2-y

    return len(set(num_drones_in_conflict))
    

def gen_coord():
    return int(random.random() * AIRSPACE_SIZE)


if __name__ == '__main__':
    drone_positions = [[gen_coord(), gen_coord()] for i in range(NUM_DRONES)]

    conflicts = check_for_conflicts(drone_positions, CONFLICT_RADIUS)

    print ("Drones in conflict: {}".format(conflicts))