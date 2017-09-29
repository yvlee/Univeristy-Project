def factorial(num):
    '''
    Complexity: O(N)
    Counts the factorial of num
    :param num: the number to find the factorial
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
    return baseFac

def convertPermutation(baseFactor, aString):
    '''
    Complexity: O(n)
    This function does the convertion of 1 permutation for string
    :param baseFactor: The base factorial
    :return:one converted permutation from one base factorial
    '''
    permutedString = ''
    for i in range(len(baseFactor)):
        x = int(baseFactor[i])
        permutedString += aString[x]
        aString = aString[:x] + aString[x+1:] #slicing the string
    #print(permutedString)
    #print(oriString)
    return permutedString

def sumBaseFac(n):
    '''
    Complexity: O(n)
    To sum up the base factorial digits
    :param n: the base factorial string
    :return: the sum of the base-! digits
    '''
    totalSum = 0
    for i in range(len(n)):
        totalSum += int(n[i])
    #print(sumString)
    return totalSum

def distinctValue(aList):
    '''
    This function gets distinct value from the sum and appends into a list to check for frequency
    :param aList: takes in the sum list
    :return: distinct values from the sum in another list
    '''
    dictionary = []
    for i in range(len(aList)):
        if aList[i] not in dictionary:
            dictionary.append(aList[i])
    return dictionary


def printFreqList(dict,aList):
    '''
    This function finds the frequency by looping thru either distinct value list/sum list (because same length), if appear once in sum list, increase frequency
    :param dict: takes in the distinct value list
    :param aList: takes in the sum list
    :return: a frequency list
    '''
    freqList = [0] * len(dict)
    for i in range(len(aList)):
        index = aList[i]
        freqList[index] += 1
    return freqList

def weightedAverage (sum, freq, fac):
    '''
    Complexity is O(n^2)
    This function finds the weighted average
    :param sum: takes in the distinct values
    :param freq: takes in the frequency
    :param fac: takes in factorial of n
    :return: the weighted average
    '''
    totalSum = 0
    for i in range(len(sum)):
        product = sum[i] * freq[i]
        totalSum += product
    weightedAvg = totalSum // fac
    return (weightedAvg)

def permute(n):
    '''
    A main function to call other functions
    :param n: input a number
    :return: EVERYTHING lol
    '''
    oriString = 'abcdefghij'
    tempList = []
    for i in range(factorial(n)):                   #loops thru 24 times because factorial(4)
        BaseFactorialDigit = convertBase(i,n)       #converts base 24 times
        thePermutation = convertPermutation(BaseFactorialDigit,oriString)
        theSum = str(sumBaseFac(BaseFactorialDigit))
        file.write("(" + str(i) + ")_10   " + "(" + str(BaseFactorialDigit) + ")_!    " + str(theSum) + "    " + str(thePermutation + "\n"))
        tempList.append(int(theSum))

    file.write("\n" + "Frequency Table"+ "\n")
    file.write("--------------------"+ "\n")
    file.write("Sum " + "Freq"+ "\n" )
    x = distinctValue(tempList)
    y = printFreqList(x, tempList)
    for i in range(len(x)):
        file.write(str(x[i]) + "     " + str(y[i]) + "\n")

    file.write("Weighted average sum = " + str(weightedAverage(x,y,factorial(n)))+ "\n")


def printHeaders(a,b):
    file.write("Input to the script: N = " + str(a)+ "\n")
    file.write("Total number of permutations = " + str(b)+ "\n")
    file.write("--------------------------------------------"+ "\n")
    file.write("Base-10  "+" Base-!" + "    "+ "Sum" + "  " + "Permutation"+ "\n")



if __name__ == '__main__':
    file = open("Output.txt", "w")
    file.write("OUTPUT FORMAT FOR Q1:" + "\n")
    n = 4
    fac = factorial(n)
    printHeaders(n,fac)
    permute(n)
    file.close()



