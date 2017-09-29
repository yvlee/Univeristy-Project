def readFile(filename):
    '''
    This function loops through the dictionary and appends into a list.
    :param filename: The dictionary.txt
    :return: a list of all texts in dictionary.txt
    '''
    dictList = []
    file = open(filename, "r")
    for line in file:
        line = line.strip('\n')
        dictList.append(line)
    return dictList

def checkLetters(n, base):
    '''
    This function counts the no.of occurence of each letter of each word
    :param n:
    :param base:
    :return:
    '''
    buckets = []
    for i in range(len(n)):
        counter = [0 for _ in range(base)]
        for j in range(len(n[i])):
            pos = ord(n[i][j])-ord('a')
            counter[pos] = counter[pos] + 1
        buckets.append(counter)

    finalbucket = []
    count = 0
    for item in buckets:
        temp = []
        string = ''
        temp.append(n[count])
        for i in range(len(item)):
            string += str(item[i])
        temp.append(string)
        finalbucket.append(temp)
        count += 1
    return finalbucket


def RadixLSD(alist):
    '''
    This function does LSD radix sort
    :param alist:
    :return:
    '''
    tmp = []
    length = 0
    k = 1
    for check in alist:
        if len(check[k]) > length:
            length = len(check[k])
        tmp.append(check)

    for i in range(length-1,-1,-1):
        buckets = [[] for _ in range(20)]
        for j in range(len(tmp)):
            buckets[int(tmp[j][k][i])].append(tmp[j])
        tmp = []
        for item in buckets:
            if len(item) != 0:
                for a in range(len(item)):
                    tmp.append(item[a])
    return tmp

def allAnagrams(sortedlist):
    tmp = []
    anagram = []
    current = int(sortedlist[0][1])
    for i in range(1,len(sortedlist)):
        if len(tmp) == 0:
            tmp.append(current)
        check = int(sortedlist[i][1])
        if current != check:
            tmp.append(sortedlist[i - 1][0])
            current = check
            anagram.append(tmp)
            tmp = []
        else:
            tmp.append(sortedlist[i-1][0])

    tmp.append(int(sortedlist[-1][1]))
    tmp.append(sortedlist[-1][0])
    anagram.append(tmp)
    return anagram

def largestAnagram(anagramlist):
    maxLen = len(anagramlist[0])
    maxAnagram = anagramlist[0]
    for i in range(1,len(anagramlist)):
        if len(anagramlist[i]) > maxLen:
            maxLen = len(anagramlist[i])
            maxAnagram = anagramlist[i]

    maxanagram = []
    for i in range(1,len(maxAnagram)):
        maxanagram.append(maxAnagram[i])

    return maxanagram

def getScrabbleWords(string, alist):
    temp = []
    temp.append(string)
    if string == "***":
        return "Bye."

    for item in (checkLetters(temp, 26)):
        occ = item[1]
    output = binarySearch(alist, occ)

    return output

def binarySearch(alist, item):
    '''
    Use binary search because i have a sorted list and not empty list m
    This function does binary search for input query with the list of anagram.
    :param alist: anagram list
    :param item: input query
    :return: the list of anagrams that is the same group of anagram with input query.
    '''
    first = 0
    last = len(alist) - 1
    found = False
    temp = []
    while first <= last and not found:
        midpoint = (first + last) // 2
        if int(alist[midpoint][0]) == int(item):
            found = True
            otherAnagrams = alist[midpoint]
            for i in range(1, len(otherAnagrams)):
                temp.append(otherAnagrams[i])

        else:
            if int(item) < int(alist[midpoint][0]):
                last = midpoint - 1
            else:
                first = midpoint + 1

    return temp


def getWildCardWords(n,base,alist):
    '''
    Task 3.
    This function is to find anagrams with a wildcard(size 1)
    :param n: input string
    :param base: number of letters (26)
    :param alist: anagram list
    :return: returns the list of anagrams with a wildcard
    '''
    counter = [0 for _ in range(base)] #constant size: 26
    for i in range(len(n)):
        pos = ord(n[i]) - ord('a')
        counter[pos] = counter[pos] + 1

    k = 0
    tmp = []
    while k < len(counter):
        #this loop is to add all possible new words with one wildcard to a temporary list
        string = ''
        counter[k] += 1
        for i in range(len(counter)):
            string += str(counter[i])
        tmp.append(string)          #constant size: 26
        counter[k] -= 1             #minus the same position to get back original digit
        k += 1

    temp = []
    wildcard = []
    for i in range(len(tmp)):
        #this loop is to loop through every item in the temporary list
        item = tmp[i]
        result = binarySearch(alist, item)
        temp.append(result)

    for i in range(len(temp)):
        item = temp[i]
        for j in range(len(item)):
            if len(item) >0:
                wildcard.append(item[j])
    return wildcard

    '''
    for item in temp:
        if len(item) > 0:
            wildcard.append(item)
    return wildcard
    '''

def theMain():
    dictionary = readFile("Dictionary.txt")
    sortedList = RadixLSD(checkLetters(dictionary, 26))
    anagrams = allAnagrams(sortedList)
    print("The largest group of anagrams:", largestAnagram(anagrams))
    query = input("Enter a query (*** to exit): ")
    while query != "***":
        querystr = getScrabbleWords(query, anagrams)
        print("anagrams without wildcard:", querystr)
        print("anagrams with wildcard:", getWildCardWords(query, 26, anagrams))
        query = input("Enter a query (*** to exit): ")


if __name__ == '__main__':
    theMain()
