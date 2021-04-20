import sys
import math


cliLineInputNumber = 1
fileInputNumber = 2


def convertStringsIntoFloats(numbers):
    convertedNumbers = []
    for entry in numbers:
        try:
            convertedNumbers.append(float(entry))
        except ValueError:
            # catching inputs other than floats
            print(f"{entry} can't be converted to a float")
    return convertedNumbers


def getNumberInput(option):
    floatingInputNumbers = []

    if (option == cliLineInputNumber):
        print("Please enter floating numbers:")
        temp = sys.stdin.readline().split()
        floatingInputNumbers = convertStringsIntoFloats(temp)
    elif (option == fileInputNumber):
        f = open(sys.argv[2], "r")
        temp = f.readline().split()
        f.close()

        floatingInputNumbers = convertStringsIntoFloats(temp)
    else:
        print("Argument doesn't match a floating number input option!\n")
        sys.exit(1)
    return floatingInputNumbers


# adding all values up and dividing by the total number
def calculateMean(numbers):
    temp = 0.0

    for number in numbers:
        temp += number
    return temp / len(numbers)


# sort values, count total numbers,
# if odd numbers just divide, if even choose the next one
def calculateMedian(numbers):
    numbers = sorted(numbers)
    size = len(numbers)

    if (size % 2 == 0):
        return numbers[int(size / 2) + 1]
    else: 
        return numbers[int(size / 2)]


def calculateDeviation(numbers):
    size = len(numbers) 
    
    if (size <= 1):
        return null

    mean = calculateMean(numbers)
    deviation = 0.0

    for number in numbers:
        deviation += (float(number) - mean)**2
    deviation = math.sqrt(deviation / float(size - 1))

    return deviation

def calculateDeviation(numbers):
    size = len(numbers) 
    
    if (size <= 1):
        return null

    mean = calculateMean(numbers)
    deviation = 0.0

    for number in numbers:
        deviation += (float(number) - mean)**2
    deviation = math.sqrt(deviation / float(size - 1))

    return deviation


if __name__ == "__main__":
    nums = getNumberInput(int(sys.argv[1]))
    mean = calculateMean(nums)
    median = calculateMedian(nums)
    deviation = calculateDeviation(nums)

    print(f"Floating Numbers: {nums}\nMean: {mean}\nMedian: {median}\nStandard Deviation: {deviation}\n")
