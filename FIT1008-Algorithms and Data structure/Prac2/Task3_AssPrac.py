class ArrayBasedList:
    def __init__(self, size=100):
        self.size = size
        self.maximum = 100
        assert size >= 0
        assert size <= self.maximum, "Maximum size is 100"
        if size:
            self.myArray = [None]*size
            self.items = 0
        else:
            raise ValueError("List size should be positive integer")


    def __str__(self):
        '''
                This function is to print out the list line by line as a string.
                precondition: Must input items
                postcondition: Returns a list printed line by line
                complexity: Best and worst case = O(N)
                :return: prints list line by line
                '''
        output = ""
        for i in range(self.items):
            output += str(self.myArray[i]) + "\n"
        return output

    def __len__(self):
        '''
        This function is used to determine the length of list.
        complexity: best case and worst case: O(1)
        :return: length of the list
        '''
        return self.items

    def append(self, item):
        '''
        This function is to append items into empty array.
        precondition: list is not full
        postcondition: list will be updated with the appended items
        complexity: best case & worst case: O(N)
        :param item: item that will be appended
        :return: updated list with the items appended in
        '''
        noSpace = self.isFull()
        if noSpace:
            self.increaseSize()
            self.myArray[self.items] = item
            self.items += 1
            return self.myArray

        else:
            self.myArray[self.items] = item
            self.items += 1
        return self.myArray

    def increaseSize(self):
        '''
        This function is increase the size of the list once it's full
        precondition: list is full
        postcondition: list size will grow 10 times
        complexity: best case & worst case: O(N)
        :return: an increased list size
        '''
        self.maximum *= 10
        tempArray = [None] * self.maximum
        for i in range(self.items):
            tempArray[i] = self.myArray[i]
        self.myArray = tempArray
        return self.myArray

    def isFull(self):
        '''
        This function is to check whether the list is full.
        precondition: length of my list is bigger than or equal to size of the array.
        complexity: best and worst case: O(1)
        :return: True if list if full, or False if list is not full
        '''
        return self.items >= len(self.myArray)

    def __contains__(self,item):
        '''
        This function is to check whether an item is in the list.
        precondition: Must be a valid item
        complexity: best and worst case: O(N)
        :param item: The item that is chosen to be searched in the list
        :return: True if the item is in the list, or False if the item is not in the list
        '''
        for i in range(self.items):
            if self.myArray[i] == item:
                return True
        return False

    def __getitem__(self, index):
        '''
        This function is to get items from the list from the indexes
        precondition: must be a valid index
        complexity: best case: O(1) and worst case: O(N)
        :param index: The index that is chosen to get the item from
        :return: item chose from the index
        '''
        if index > 0 and index <= self.items:
            return self.myArray[index-1]
        else:
            raise IndexError

    def __setitem__(self, index, value):
        '''
         This function is to set a new item and append it at the index selected
         precondition: Must have a valid index
         complexity: Best case: O(1)and worst case: O(N)
         :param index: The index that is chosen to get the item from
         :param value: value that will be set at the chosen index
         :return: an updated list of new items appended
         '''
        validIndex = index >= 0 and index <= self.items
        if validIndex:
            self.myArray[index - 1] = value
            return self.myArray
        else:
            raise IndexError

    def __eq__(self, other):
        '''
        This function checks whether the list is the same as another list
        precondition: the length of the other list must be same as the original list
        complexity: Best case: O(1) and worst case: O(N)
        :param other: a new list
        :return: True if equals, False if not equals
        '''

        if len(other) == self.items:
            for i in range(self.items):
                if self.myArray[i] != other[i]:
                    return False
                return True

    def insert(self,index,item):
        '''
         This function inserts a new item at the position before the index selected
         preconditon: if the list is not full
         complexity: best case: O(1) worst case: O(N)
         :param index: The index that is chosen to insert the item
         :param item: item to be inserted to the position before index selected
         :return: an updated list that is grown in size after inserting more items
         '''
        validIndex = index >= 0 and index < self.items
        noSpace = self.isFull()
        if not noSpace and validIndex:
            self.items += 1
            for i in range (self.items-1,index - 1,-1):
                self.myArray[i] =  self.myArray[i-1]    #moving items
            self.myArray[index - 1] = item
            print(self.myArray)
        elif noSpace:
            #rint("isfull, resize")
            self.increaseSize()

        else:
            raise IndexError

    def delete(self,index):
        '''
        This function is to delete items in the list from the index selected
        precondition: index must be valid and there are items in the list to be
        complexity: best case: O(1) worst case: O(N)
        :param index: the index chosen to delete the item from
        :return: An updated list that no longer contains the item selected to delete
        '''
        validIndex = index >= 0 and index <= self.items
        if validIndex:
            for i in range (index-1, self.items-1):
                self.myArray[i] = self.myArray[i + 1]
            self.items -= 1
            return validIndex
        else:
            raise IndexError

    def remove(self,item):
        '''
               This function removes item directly from the list
               precondition: valid item to be removed
               complexity: best case and wosrt case:O(N)
               :param item: the item to be removed from list
               :return: An updated list that no longer contains the item selected to be removed
               '''
        for i in range (self.items):
            if item == self.myArray[i]:
                self.items -= 1
                while i < self.items:
                    self.myArray[i] = self.myArray[i+1]
                    i += 1
                return
            else:
                raise ValueError


theArray = ArrayBasedList(20)
theArray.append(6)
theArray.append(2)
theArray.append(3)
theArray.append(4)
theArray.append(5)
theArray.append(6)
theArray.append(7)
theArray.append(8)
print(theArray)
print(theArray.__getitem__(2))
theArray.insert(1,"pie")

