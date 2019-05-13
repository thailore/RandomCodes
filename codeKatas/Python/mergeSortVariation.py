from collections import deque

"""Program should take 2 arrays consisting of k elements, and sort them into
one big array without using the sorted() built in function"""


def mergeSort(firstArray, secondArray):
    newArray = []

    while firstArray and secondArray:
        if firstArray[0] < secondArray[0]:
            newArray.append(firstArray.popleft())
        else:
            newArray.append(secondArray.popleft())
    newArray.extend(firstArray)
    newArray.extend(secondArray)

    return (newArray)




if __name__ == '__main__':

    f, s = deque(), deque()
    fA = input("Enter first array separated by commas: ")
    fA = fA.split(",")
    for i in range(len(fA)):
        fA[i] = int(fA[i])

    sA = input("Enter second array separated by commas: ")
    sA = sA.split(",")
    for i in range(len(sA)):
        sA[i] = int(sA[i])
    sA = sorted(sA)
    fA = sorted(fA)
        
    for i in range(len(fA)):
        f.append(fA[i])

    for i in range(len(sA)):
        s.append(sA[i])
    
    print(mergeSort(f,s))
