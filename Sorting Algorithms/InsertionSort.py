def insertionSort(aList):
    for i in range(1, len(aList)): #invariant 1: alist[:i] is sorted
        currentValue = aList[i]
        position = i
        while position > 0 and aList[position-1] > currentValue: #invariant 2: key > alist[position:]
            aList[position] = aList[position-1]
            position -= 1
        aList[position] = currentValue
    return aList

if __name__ == '__main__':
    mylist = [2,42,23,44,1,0]
    print(insertionSort(mylist))
