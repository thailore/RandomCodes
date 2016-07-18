from collections import OrderedDict
def multiSelection(dimensions, tasks, mouseCoordinates):
    total = OrderedDict()
    offset = 0
    total[tasks[0]]=[[0,0],[dimensions[0],dimensions[1]]]
    for i in range(1,len(tasks)):
        key = tasks[i]
        offset += dimensions[2]
        left_h = (dimensions[1] * i)+offset
        total[tasks[i]]= [[0,left_h],[dimensions[0],left_h+dimensions[1]]]
    msx = sorted(mouseCoordinates)
    print(msx)
    msy = sorted(mouseCoordinates, key=lambda t: t[1])
    answer = []
    
    print(msy)
    print(total)
    for key, value in total.items():

        for k in range(value[0][1],value[1][1]+1):
            if k in range(msy[0][1],msy[1][1]+1):
                #for y in range(value[0][0],value[0][1]):
                 #   if y in range(msx[0][1],msx[1][1]+1):
                print(key)
                if key not in answer:
                    answer.append(key)
    return answer





def tasksScheduling(workingHours, tasks):
    days = 0
    done = False
    a = tasks
    for num in tasks:
        if num > workingHours:
            return -1
        
    while not done:
        b = list(sorted(a)[::-1])
        day = workingHours
        days+=1
        for i in range(len(b)):
            if day - b[i] >= 0:
                a.remove(b[i])
                day -= b[i]
        if len(a)==0:
            done = True
    return days