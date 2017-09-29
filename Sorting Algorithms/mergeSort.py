def mergekSort(list):
    #split the list until its has one item
    print('Splitting', list)
    if len(list) > 1:
        mid = len(list)//2
        leftList = list[:mid]
        rightList = list[mid:]
        mergekSort(leftList)
        mergekSort(rightList)

    #merge back the list, only start executing when the list has only one item
        i,j,k, = 0, 0, 0
        while i < len(leftList) and j < len(rightList): #this loop compares the items in the 2 list and place them to the new list
            if leftList[i] < rightList[j]:
                list[k] = leftList[i]
                i += 1
            else:
                list[k] = rightList[j]
                j += 1
            k += 1

        while i < len(leftList): #this loop settles the remaining items that have no been place into the new list for the left list
            list[k] = leftList[i]
            i += 1
            k += 1

        while j < len(rightList): #this loop settles the remaining items that have no been place into the new list for the right list
            list[k] = rightList[j]
            j += 1
            k += 1

    print('Merging', list)



if __name__ == "__main__":
    testList = [54,26,93,17,77,31,44,55,20]
    testList2 = [54,26,93,17]
    mergekSort(testList2)
    print(testList2)

#mergesort will split the list until it has only one item, then it will begin to combine back the list
#complexity? Base, worst, average is O(N log N). breaks the list log N time, and N time to merge back the list