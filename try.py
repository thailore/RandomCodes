def tasksScheduling(workingHours, tasks):
    days = 0
    done = False
    a = tasks
    for num in tasks:
        print("yo")
        if num > workingHours:
            return -1
        
    while not done:
        b = list(a)
        day = workingHours
        days+=1
        for i in range(len(b)):

            if day - b[i] >= 0:
                a.remove(b[i])
                day -= b[i]
        if len(a)==0:
            done = True
    return days
            
