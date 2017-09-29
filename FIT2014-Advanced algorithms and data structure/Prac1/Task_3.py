def checkSquareMatrix(n):
    '''
    Complexity: O(n^2)
    To check if matrix is square matrix, if not return error
    :param n: input text file of matrix
    :return: if input is a square matrix, return the the size. else return error
    '''
    row = 0
    column = 0
    errorMessage = "Error"
    for i in range (len(n)):
        column += 1
        for j in range (len(n[i])):
            row += 1
    row2 = row // column
    if column == row2:
        return column
    else:
        return errorMessage

def factorial(num):
    '''
    Complexity: O(n)
    Counts the factorial of num
    :param num: should be the return of checkSquareMatrix
    :return: the number of factorial
    '''
    counter = 1
    sumFac = 1
    for i in range(1,num+1):
        sumFac *= counter
        counter += 1
    return sumFac


def convertBase(n, digit):
    '''
    Complexity: O(M) * O(N), overall categorised as O(N)
    This function converts number in base 10 to number in base factorial
    :param n: the dividend
    :param digit: factorial
    :return: number in base factorial
    '''
    baseFac = ''
    for i in range(digit-1, -1, -1):        #Complexity is O(N)
        div = factorial(i)                  #Complexity is O(M)
        quotient= str(n // div)
        n = n % div
        baseFac += quotient
    #print(len(baseFac))
    return baseFac  #rmb to change to return

def sumBaseFac(n):
    '''
    To sum up the basefactorial digits
    :param n: the base factorial string
    :return: the sum of the base-! digits
    '''
    totalSum = 0
    for i in range(len(n)):
        totalSum += int(n[i])
    #print(sumString)
    return totalSum

def convertPermutation(baseFactor, aString):
    permutedList = []
    for i in range(len(baseFactor)):
        x = int(baseFactor[i])
        permutedList.append(int(aString[x]))
        aString = aString[:x] + aString[x+1:] #slicing the string
    #print(str(permutedList) + "pL")
    return permutedList

def checkSign(sum, multList):
    '''
    This function is to denote the sign for finding determinant. If even number, sum. If off, subtract.
    :param sum: sum of base fac
    :return: returns a multiply list with correct signs
    '''
    for i in range(len(sum)):
        if sum[i] % 2 == 0:
            multList[i] *= 1
        else:
            multList[i] *= -1
    return multList

def calculation(mList):
    '''
    This function calculates the determinant
    :param mList: the multiply list
    :return: the determinant of the matrix
    '''
    output = 0
    for i in range (len(mList)):
        output += mList[i]
    return output


def findPosition(permute,matrix):
    '''
    This function finds the number of the matrix at the given position
    :param permute: row position
    :param matrix: column position
    :return: the numbers of the matrix
    '''
    multiply = []
    #print(permute, 'permute')
    for i in range(len(permute)):
        rowPos = permute[i] - 1
        #print(rowPos)
        x = matrix[rowPos][i]
        multiply.append(x)
    #print(multiply)
    return multiply

def multiplyCalculation(mult):
    '''
    This function does a multiplication for all the 6 permutations
    :param mult: multiply list from findPosition
    :return: returns the product for every permutations
    '''
    product = 1
    for i in range(len(mult)):
        product *= mult[i]
    return product

def taskTwoMain(matrix):
    '''
    A main function to call other functions
    :param n: n will be my matrix
    :return:
    '''
    x = checkSquareMatrix(matrix)
    permuteList = []
    sumList = []
    oriString = ''
    for i in range (factorial(x)):
        oriString += str(i)

    for i in range(factorial(x)):  # loops thru 24 times because factorial(4)
        BaseFactorialDigit = convertBase(i, x)
        thePermutation = convertPermutation(BaseFactorialDigit, oriString)
        theSum = sumBaseFac(BaseFactorialDigit)
        sumList.append(theSum)
        permuteList.append(thePermutation)

    # print(permuteList)
    productList = []
    for j in range(len(permuteList)):
        x = findPosition(permuteList[j], matrix)
        y = multiplyCalculation(x)
        productList.append(y)

    a = checkSign(sumList, productList)
    return calculation(a)


if __name__ == '__main__':
    matrix = []
    file = open("Matrix.txt", "r")
    for line in file:
        line = line.strip('\n')
        line = line.split(',')
        tmp = []
        for item in line:
            tmp.append(int(item))
        matrix.append(tmp)

    file.close()
    with open('Output.txt', 'a') as fileWrite:
        fileWrite.write("---------------------------------------------------------------------------------------------" + "\n")
        fileWrite.write("OUTPUT FORMAT FOR Q3:" + "\n")
        fileWrite.write("N = " + str(checkSquareMatrix(matrix)) + "\n")
        fileRead = open("Matrix.txt", "r")
        fileWrite.write("Input Matrix: " + "\n")
        for item in fileRead:
            item = item.strip('\n')
            item = item.replace(',',' ')
            fileWrite.write(item + "\n")

        fileWrite.write("\n" + "Determinant = " + str(taskTwoMain(matrix)) + "\n")
    fileWrite.close()


