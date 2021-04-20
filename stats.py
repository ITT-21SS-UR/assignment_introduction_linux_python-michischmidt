import sys


cliLineInputNumber = 1
fileInputNumber = 2


def convertInputIntoFloats(numbers):
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
        print("Please enter floating numbers:\n")
        temp = sys.stdin.readline().split()
        floatingInputNumbers = convertInputIntoFloats(temp)
    elif (option == fileInputNumber):
        f = open(sys.argv[2], "r")
        temp = f.readline().split()
        f.close()

        floatingInputNumbers = convertInputIntoFloats(temp)
    else:
        print("Argument doesn't match a floating number input option!\n")
        sys.exit(1)

    return floatingInputNumbers


if __name__ == "__main__":
    nums = getNumberInput(int(sys.argv[1]))
    # calculateMean()
    # calculateMedian()
    # calculateStandardDeviation()
