numbers = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'}


def convert_number_to_rome(arabicNumber, numbersDict):
    idx = 0
    resultList = []
    equal = 0
    maxArabic = 0

    for number in numbersDict:
        if number <= arabicNumber:
            maxArabic = number
    maxNumberToUseIdx = list(numbersDict).index(maxArabic)

    if arabicNumber in numbersDict:
        idx = list(numbersDict).index(arabicNumber)
        resultList.append(list(numbersDict)[idx])

    else:
        while True:
            resultList.append(list(numbersDict)[maxNumberToUseIdx])
            if sum(resultList) == arabicNumber and len(resultList) <= 3:
                break
            elif len(resultList) >= 4:
                resultList = []
                break

        if sum(resultList) != arabicNumber:
            resultList.append(list(numbersDict)[maxNumberToUseIdx])
            while True:
                if maxNumberToUseIdx >= 1 and maxNumberToUseIdx < 6:
                    resultList.append(list(numbersDict)[maxNumberToUseIdx - 1])
                elif maxNumberToUseIdx == 6:
                    resultList.append(list(numbersDict)[maxNumberToUseIdx])
                else:
                    resultList.append(list(numbersDict)[maxNumberToUseIdx])

                if arabicNumber == 4:
                    resultList = []
                    resultList.append(list(numbersDict)[0])
                    resultList.append(list(numbersDict)[maxNumberToUseIdx + 1])
                    break

                elif arabicNumber == 40:
                    resultList = []
                    resultList.append(list(numbersDict)[2])
                    resultList.append(list(numbersDict)[maxNumberToUseIdx + 1])
                    break

                elif arabicNumber == 400:
                    resultList = []
                    resultList.append(list(numbersDict)[4])
                    resultList.append(list(numbersDict)[maxNumberToUseIdx + 1])
                    break

                else:
                    if len(resultList) <= 4:
                        equal = sum(resultList)
                        if equal == arabicNumber:
                            break

                    else:
                        resultList = []
                        resultList.append(list(numbersDict)[
                                          maxNumberToUseIdx - 1])
                        resultList.append(list(numbersDict)[
                                          maxNumberToUseIdx + 1])
                        break
    return resultList


def message(final, arabicNumber):
    result = ''
    for i in final:
        result += numbers[i]
    print('*'*(26 + len(arabicNumber) + len(result)))
    print(f'*** Arabic: {arabicNumber} | Roman: {result} ***')
    print('*'*(26 + len(arabicNumber) + len(result)))


print('Welcome to the Arabic to Roman numeral converter')
while True:
    print('Enter a number from 1 to 3999')
    arabicIn = input('>>> ')
    try:
        if int(arabicIn) < 1 or int(arabicIn) > 3999:
            print(f'Number {arabicIn} is wrong')
            break
    except ValueError:
        print(f'The sign "{arabicIn}" is not a number!')
        break

    splitNumber = []
    for n in str(arabicIn):
        splitNumber.append(n)

    if len(splitNumber) >= 1:
        arab1 = int(splitNumber[-1])
    if len(splitNumber) >= 2:
        arab10 = int(splitNumber[-2]) * 10
    else:
        arab10 = 0
    if len(splitNumber) >= 3:
        arab100 = int(splitNumber[-3]) * 100
    else:
        arab100 = 0
    if len(splitNumber) == 4:
        arab1000 = int(splitNumber[-4]) * 1000
    else:
        arab1000 = 0

    final = []
    if arab1000 != 0:
        final.extend(convert_number_to_rome(arab1000, numbers))
    if arab100 != 0:
        final.extend(convert_number_to_rome(arab100, numbers))
    if arab10 != 0:
        final.extend(convert_number_to_rome(arab10, numbers))
    if arab1 != 0:
        final.extend(convert_number_to_rome(arab1, numbers))

    message(final, arabicIn)
    print('Do you want to convert another number ? (y/N)')
    userChoice = input('>>> ')
    if userChoice == 'N':
        break
