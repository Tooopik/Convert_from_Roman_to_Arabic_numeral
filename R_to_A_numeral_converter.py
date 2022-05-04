numbers = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'}


def max_number_to_use_idx(arabicNumber, numbersDict):
    maxArabic = 0
    for number in numbersDict:
        if number < arabicNumber:
            maxArabic = number
    maxNumberToUseIdx = list(numbersDict).index(maxArabic)
    return maxNumberToUseIdx


def convert_number_to_rome(arabicNumber, numbersDict):
    idx = 0
    resultList = []
    equal = 0

    if arabicNumber in numbersDict:
        idx = list(numbersDict).index(arabicNumber)
        resultList.append(list(numbersDict)[idx])

    else:
        maxNumberToUseIdx = max_number_to_use_idx(arabicNumber, numbersDict)
        resultList.append(list(numbers)[maxNumberToUseIdx])
        while True:
            if maxNumberToUseIdx >= 1 and maxNumberToUseIdx < 6:
                resultList.append(list(numbersDict)[maxNumberToUseIdx - 1])
            elif maxNumberToUseIdx == 6:
                resultList.append(list(numbersDict)[maxNumberToUseIdx])
            else:
                resultList.append(list(numbersDict)[maxNumberToUseIdx])

            if arabicIn == 4:
                resultList = []
                resultList.append(list(numbersDict)[0])
                resultList.append(list(numbersDict)[maxNumberToUseIdx + 1])
                break

            elif arabicIn == 40:
                resultList = []
                resultList.append(list(numbersDict)[2])
                resultList.append(list(numbersDict)[maxNumberToUseIdx + 1])
                break

            elif arabicIn == 400:
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
                    resultList.append(list(numbersDict)[maxNumberToUseIdx - 1])
                    resultList.append(list(numbersDict)[maxNumberToUseIdx + 1])
                    break
    return resultList


arabicIn = 2671


arab1000 = 2000
arab100 = 600
arab10 = 70
arab1 = 1

final = []
if arab1000 != 0:
    final.extend(convert_number_to_rome(arab1000, numbers))
if arab100 != 0:
    final.extend(convert_number_to_rome(arab100, numbers))
if arab10 != 0:
    final.extend(convert_number_to_rome(arab10, numbers))
if arab1 != 0:
    final.extend(convert_number_to_rome(arab1, numbers))

result = ''
for i in final:
    result += numbers[i]
print('*'*33)
print(f'*** Liczba: {arabicIn} to: {result} ***')
print('*'*33)
