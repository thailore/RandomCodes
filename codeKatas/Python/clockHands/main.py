#!/usr/bin/env python

def getClockhands(time):
        degreesBetweenHours = 30

        numbers = time.split(":")
        hour = int(numbers[0])
        minutes = int(numbers[1])


        hourAngleFrom12 = (hour * degreesBetweenHours) + ((minutes/60) * degreesBetweenHours)   
        # 360 + 15 = 

        minutesAngleFrom12 = minutes * 6 
        #180

        smallestTimeAngle = abs(hourAngleFrom12 - minutesAngleFrom12)
        if smallestTimeAngle > 180:
            smallestTimeAngle = 360 - smallestTimeAngle
        return smallestTimeAngle

if __name__ == "__main__":
    time = input("Enter time of day: ")
    print(getClockhands(time))