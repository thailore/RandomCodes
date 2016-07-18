def parkingSpot(carDimensions, parkingLot, luckySpot):
    #check first if luckyspot available
    upperLeft = parkingLot[luckySpot[0]][luckySpot[1]]
    bottomRight = parkingLot[luckySpot[2]][luckySpot[3]]
    if bottomRight == 1 or upperLeft == 1:
        print(1)
        return False
    
    if luckySpot[2]-luckySpot[0]+1 == carDimensions[0] and luckySpot[3] - luckySpot[1]+1 == carDimensions[1]: #coming from y axis
        #check if can enter from left or right
        works = True
        for i in range(luckySpot[1] +1 ):
            if parkingLot[i][luckySpot[2]] == 1:
                print(2)
                works = False
                break
        if works == True:
            return works
        for i in range(carDimensions[1],len(parkingLot[luckySpot[]])):
            if parkingLot[i][luckySpot[2]] == 1:
                print(3)
                return False
        works = True
        return works
            
            
    else: #coming from x axis
        #check if can enter from top or bottom
        works = True
        for i in range(luckySpot[3] +1 ):
            if parkingLot[luckySpot[1]][i] == 1:
                print(4)
                works = False
                break
        if works == True:
            return works
        for i in range(carDimensions[1],len(parkingLot[luckySpot[2]])):
            if parkingLot[luckySpot[2]][i] == 1:
                print(5)
                return False
        works = True
        return works
    