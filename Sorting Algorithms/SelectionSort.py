def selectionSort(aList):
    for i in range(len(aList)-1, 0, -1):
        positionMax = 0
        for j in range(1, i+1):
            #print(i, j)
            if aList[j] > aList[positionMax]:
                positionMax = j
        tmp = aList[i]
        aList[i] = aList[positionMax]
        aList[positionMax] = tmp
    return aList

if __name__ == '__main__':
    list = [54,26,93,17,77,31,44,55,20]
    print(selectionSort(list))