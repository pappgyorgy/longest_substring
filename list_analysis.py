
def identifySublist(digitCharList):

    longestSubList = idxBeg = idxEnd = 0
    subListCenter = 1

    types = list(map(
        lambda e:
            [1, -1][isinstance(e, str)],
        digitCharList
    ))

    while subListCenter < (len(digitCharList) - ((longestSubList // 2) + 1)):
        incValue = 0
        sum = 0

        while (subListCenter - (incValue + 1) >= 0) and (subListCenter + incValue < len(digitCharList)):
            sum += types[subListCenter + incValue]
            sum += types[subListCenter - (incValue + 1)]

            if sum == 0:
                subListLength = (incValue + 1) * 2
                if subListLength > longestSubList:
                    idxBeg = subListCenter - (incValue + 1)
                    idxEnd = subListCenter + incValue
                    longestSubList = subListLength

            incValue += 1

        subListCenter += 1


    return (idxBeg, idxEnd)