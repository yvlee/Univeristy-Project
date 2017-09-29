def quickSort(alist):
   recursive_quick(alist,0,len(alist)-1)
   return alist

def recursive_quick(alist,first,last):
   if first<last:
       mid = partition(alist,first,last)
       recursive_quick(alist,first,mid-1)
       recursive_quick(alist,mid+1,last)

def partition(alist,first,last):
   pivot = alist[first]     #pivot value
   left = first+1           #left index
   right = last             #right index
   check = False
   while not check:
       while left <= right and alist[left] <= pivot:    #while left index <= right index and alist[left index] <= pivot value
           left = left + 1                              #left index + 1, move index one position to the right

       while alist[right] >= pivot and right >= left:   #while alist[right index] >= pivot value and right index >= left index
           right = right -1                             # right index move one position to the left

       if right < left:                             #means sorted list
           check = True
       else:
           temp = alist[left]
           alist[left] = alist[right]
           alist[right] = temp

   temp = alist[first]
   alist[first] = alist[right]
   alist[right] = temp
   return right


if __name__ == '__main__':
   #Below are examples of inputs to try with the quicksort algorithm.
    unsortedList = [54,26,93,17,77,31,44,55,20]
    unsortedTable = [("acdb",4), ("abdc",3), ("adcb",5), ("abcd",2), ("aaaa",1)]
    unsortedList = ["acdb", "abdc","adcb","abcd","aaaa"]
    print(quickSort(unsortedTable))
