def smartAssigning(information):
    """for i in range(len(information)):
        if information[i][1] != "0":
            avail = i
            tasks = information[i][3]
            break
                
    for i in range(len(information)):
        if information[i][1] == "0":
            next
        else:
            if information[i][3] == "0":
                return information[i][0]
            if information[i][3] < tasks:
                tasks = information[i][3]
                avail = i
            if information[i][3] == tasks:
                if information[i][2] < information[avail][2]:
                    tasks = information[i][3]
                    avail = i
    return information[avail][0]"""
    total = sorted(information, key=lambda x: x[3])
    avail = total[0][0]
    for i in range(len(total)-1):
        if total[i][1] == "0":
            avail = total[i+1][0]
        if total[i][3] == total[i+1][3]:
            if total[i][2] < total[i+1][2]:
                avail = total[i][0]
            else:
                avail = total[i+1][0]
    print(total)
    return avail
            

def tasksTypes(deadline, day):
    labels = [0,0,0]
    for i in range(len(deadline)):
        if deadline[i]<= day:
            labels[0]+=1 
        elif deadline[i] in range(day+1, day+8):
            labels[1]+=1
        else:
            labels[2]+=1
    return labels

