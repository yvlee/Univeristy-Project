def getCombinations(m, n):
    '''
    This function is to get all possible combinations
    :param m: is the first m letters
    :param n: the size of the string
    :return: all combinations in binary
    '''
    perm = m**n
    allComb = []
    for i in range(perm):
        pointer = -1
        vertex = [0] * n
        quotient = i//m
        remainder = i % m
        status = False
        vertex[pointer] += remainder

        while status is False:
            if quotient != 0:
                remainder = quotient % m
                pointer -= 1
                vertex[pointer] += remainder

                quotient = quotient // m
                if quotient == 0:
                    allComb.append(vertex)
                    break

            else:
                status = True
                allComb.append(vertex)

    return allComb

def adjList(nlist,n):
    '''
    This function creates the graph which is represented by adjacency list form
    :param nlist: the combination list
    :param n: the size of string
    :return: the adjacency list
    '''
    adjlist = []
    for i in range(len(nlist)):
        templist = []
        item = nlist[i]
        for j in range(len(nlist)):
            item2 = nlist[j]
            front = item2[:n-1]
            back = item[1:]
            #print(back,front)
            if back == front:
                templist.append(j)
        adjlist.append(templist)

    return adjlist

class Stack:
    def __init__(self,size):
        assert size > 0, "size should be positive"
        self.theArray = size * [None]
        self.count = 0
        self.top = -1

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count >= len(self.theArray)

    def reset(self):
        self.count = 0
        self.top = -1

    def push(self, newItem):
        assert not self.isFull(), "The stack is full."
        self.top += 1
        self.theArray[self.top] = newItem
        self.count += 1

    def pop(self):
        assert not self.isEmpty(), "The stack is empty"
        item = self.theArray[self.top]
        self.top -= 1
        self.count -= 1
        return item

    def peek(self):
        assert not self.isEmpty(), "The stack is empty"
        item = self.theArray[self.top]
        return item

def getCircuit(adjlist,m):
    '''
    This function is to find the eulerian circuit
    :param adjlist: the adjacency list
    :param m: number of letters
    :return: the circuit
    '''
    myStack = Stack((len(adjlist) * m) + 1)
    circuit = Stack((len(adjlist) * m) + 1)
    myStack.push(0) # start from vertex 0
    degree = []
    edgecount = len(adjlist) * m

    for i in range(len(adjlist)):
        degree.append(len(adjlist[i]))

    #print(edgeCount[currentVertex])
    while not myStack.isEmpty():
        currentVertex = myStack.peek()
        #print(currentVertex)

        if (degree[currentVertex] == 0):
            checkedVertex = myStack.pop()
            circuit.push(checkedVertex)
        else:
            nextVertex = adjlist[currentVertex][degree[currentVertex]-1]
            degree[currentVertex] -= 1
            edgecount -= 1
            myStack.push(nextVertex)
            previous = nextVertex
            while nextVertex != currentVertex:
                nextVertex = adjlist[previous][degree[previous]-1]
                degree[previous] -= 1
                if degree[previous] == 0:
                    edgecount -= 1
                myStack.push(nextVertex)
                previous = nextVertex

    finalCircuit = []
    while not circuit.isEmpty():
        finalCircuit.append(circuit.pop())

    return finalCircuit


def outputString(circuit,allcomb):
    '''
    Outputs the final string
    :param circuit: the circuit
    :param allcomb: all combination
    :return: the final output string
    '''
    finalStr = []
    output = ''
    for i in range(len(circuit)):
        finalStr.append(allcomb[circuit[i]])

    for i in range(len(finalStr[0])):
        output += chr((finalStr[0][i]) + 65)

    for i in range(1,len(finalStr)):
        output += chr((finalStr[i][-1]) + 65)

    return output


def main():
    letters = int(input("enter a number:"))
    size = int(input("enter a number:"))
    file = open('outputTask1.txt', 'w')
    if letters >= 2 and letters <= 5 and size >= 2 and size <= 3:
        print(getCombinations(letters,size))
        comb = getCombinations(letters,size)
        print("adjlist:", adjList(comb, size))
        adjlist = adjList(comb, size)
        print(getCircuit(adjlist,letters))
        file.write(outputString(getCircuit(adjlist,letters),comb))
        file.close()
    else:
        print("Out of RANGEEEE! Bye.")




if __name__ == '__main__':
    main()

