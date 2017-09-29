from Task4_AssPrac import ArrayBasedList


class TextEditor:
    def __init__(self):
        self.newArray = ArrayBasedList(10)

    def insertNum(self,num, item):
        '''
        This function inserts a new item at the position before the index selected
        complexity: bests and worst case O(1)
        :param num: the index that is chosen to insert the item
        :param item: item to be inserted to the position before index selected
        :return: an updated list that is grown in size after inserting more items
        '''
        num = int(num)
        if num >= 1 and num <= len(command.newArray):
            self.newArray.insert(num,item)
            print(self.newArray)

    def readFile(self,filename):
        '''
        This function is to read in a file
        complexity: best case and worst case: O(n)
        :param filename:The file name of the file that is used to read in
        :return: the content in the file
        '''
        infile = open(filename, 'r')
        content = infile.readlines()
        infile.close()
        for i in range(len(content)):
            row = str(content[i].rstrip('\n'))
            self.newArray.append(row)
        print(self.newArray)
        return self.newArray

    def writeFile(self,filename):
        '''
        This function is to write in a file
        complexity:
        :param filename:The file name of the file that is used to write in
        :return: contents will be overwrited
        '''
        outfile = open(filename, 'w')
        for i in range(1, (len(self.newArray) + 1)):
            outfile.write(self.newArray[i] + '\n')
        outfile.close()
        return self.newArray

    def print(self,num):
        '''
        This function is to print the contents given the index. Function is supposed to print out whole list if no index given
        :param num: the index of item that is chosen to be printed
        :return: printed item or printed list
        '''
        num = int(num)
        if num > len(self.newArray):
            raise IndexError
        print(self.newArray[num])

    def deleteNum(self,num):
        '''
        This function is to delete the contents given the index. Function is supposed to delete whole list if no index given
        complexity: best case worst case: O(N)
        :param num: the index of item that is chosen
        :return: either empty list or list without the deleted items
        '''
        num = int(num)
        if num > len(self.newArray):
            raise IndexError
        self.newArray.delete(num)
        #print(self.newArray)

    def quit(self):
        print("bye bye")
        raise SystemExit

    def frequency(self):
        '''
        This function is to check for the amount of time the same item appeared in the list
        :return: the item and the amount of time it appeared
        '''
        tempList = []
        for i in range(1, len(command.newArray) + 1):
            target = command.newArray[i]
            target = target.split(" ")
            print(target)
            for j in range(len(target)):
                tempList.append(target[j])
        print(tempList)

        for i in range(len(tempList)):
            newtarget = tempList[i]
            count = 0
            for j in range(i+1, len(tempList)):
                if newtarget == tempList[j]:
                    count += 1
            #print(newtarget + str(count))


            #for j in range(i+1, len(command.newArray)):
                #if target == command.newArray[j]:
                    #count += 1
            #print(target + "count")


if __name__ == '__main__':
    print("1. insert // type insert* (space) *index*")
    print("2. read // type *read* (space) *filename.txt*")
    print("3. write // type *write* (space) *filename.txt*")
    print("4. print // type *print* (space) *index or nothing*")
    print("5. delete // type *delete* (space) *index or nothing*")
    print("6. quit")
    print("7. frequency")

    command = TextEditor()
    while True:
        try:
            option = input()
            option = option.split(" ")
            # print(len(option))
            if len(option) < 3:
                if option[0] == "read":
                    filename = option[1]
                    command.readFile(filename)
                    # print(len(command.newArray))

                if option[0] == "insert":
                    num = int(option[1])
                    if num >= 1 and num <= len(command.newArray):
                        item = input("Enter:")
                        num = int(num)
                        # print('hi')
                        command.insertNum(num, item)
                        # print('hi')
                    else:
                        print("?")

                if option[0] == "write":
                    file_name = option[1]
                    command.writeFile(file_name)
                    # print(hi)
                    # print(command.newArray)

                if option[0] == "print":
                    if len(option) == 1:
                        print(str(command.newArray))
                    else:
                        command.print(option[1])

                if option[0] == "delete":
                    if len(option) == 1:
                        print(range(1, len(command.newArray)))
                        for item in range(len(command.newArray), 0, -1):
                            print(command.newArray[item])
                            command.deleteNum(item)
                    else:
                        index = int(option[1])
                        command.deleteNum(index)

                if option[0] == "quit":
                    command.quit()

                if option[0] == "frequency":
                    command.frequency()

            else:
                print("?")


        except Exception:
            print("?")
