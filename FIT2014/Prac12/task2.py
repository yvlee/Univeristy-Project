def getCombinations(m, n):
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

def convertToGray(comblist, n):
    subsetList = []

    for item in comblist:
        binary = [0]* n
        binary[0] = item[0]
        for i in range(len(item) - 1):
            if item[i] != item[i+1]:
                binary[i+1] += 1
        subsetList.append(binary)

    return subsetList

def getSubsetString(slist,letters):
    final = []
    for item in slist:
        templist = []
        for i in range(len(item)-1,-1,-1):
            if item[i] != 0:
                templist.append(letters[i])
        final.append(templist)
    return final


def theletters(n):
    letters = 'abcdefghijklm'
    newStr = ''
    newStr +=(letters[:n])
    finalstr = ''
    for i in range(len(newStr)-1,-1, -1):
        finalstr += newStr[i]
    return finalstr

def main():
    n = int(input("enter a number:"))
    comb = getCombinations(2, n)
    #print(convertToGray(comb, n))
    graycode = convertToGray(comb,n)
    letters = theletters(n)
    allSubsets = getSubsetString(graycode,letters)
    #print(allSubsets)

    file = open('outputTask2.txt','w')
    for i in range(len(allSubsets)):
        file.write("subset "+ str(i + 1) + ": "+ str(allSubsets[i]) +"\n")

    file.close()

if __name__ == '__main__':
    main()
