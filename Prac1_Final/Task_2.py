def countTransposition(input1,input2):
    '''
    Complexity:
    This function counts the minimum transposition for one permutation to transposed to another permutation
    :param input1: the base
    :param input2: the transposed string
    :return: the number of transpositions
    '''
    oriString = input1
    transposedString = input2
    transposition = 0
    for i in range (len(transposedString)):
        tempNum = transposedString[i]
        for j in range (len(oriString)):
            if tempNum == oriString[j]:
                transposition += j
                oriString = oriString[:j] + oriString[j+1:]
                break
    return transposition


if __name__ == '__main__':

    first = input("Input Permutation 1 = ")
    second = input("Input Permutation 2 = ")
    with open('Output.txt', 'a') as file:
        file.write("---------------------------------------------------------------------------------------------"+"\n")
        file.write("OUTPUT FORMAT FOR Q2:")
        file.write("\n" + "Input Permutation 1 = " + first + "\n" + "Input Permutation 2 = " + second + "\n")
        file.write("Output (smallest number of inversion): " + str(countTransposition(first, second)) + "\n")
    file.close()