#Uber test 1
def perfectCity(departure, destination):
    total = 0
    up, down, left, right = 0,0,0,0
    if type(departure[0]) == int: #x is int
        total += abs(departure[0]-destination[0])
        test = list(str(destination[1]))
        test2 = list(str(departure[1]))
        if test[0] != test2[0]: 
            total += abs(departure[1]-destination[1])
        else:
            up = abs(math.ceil(departure[1])-departure[1])+abs(math.ceil(destination[1]) - destination[1])
            down = abs(departure[1] - math.floor(departure[1]))+ destination[1]
        if up>down:
            total+= down
        else:
            total+= up
        
        
    else: #y is int
        total += abs(departure[1]-destination[1])
        test = list(str(destination[0]))
        test2 = list(str(departure[0]))
        if test[0] != test2[0]: 
            total += abs(departure[0]-destination[0])
        else:
            left = abs(departure[0] - math.floor(departure[0])) + destination[1]
            right =abs(math.ceil(departure[0]) - departure[0]) + abs(math.ceil(destination[0]) - destination[0])
        if left > right:
            total+= right
        else:
            total+= left
        
        
    return total