import sys


inputChoice = 0
cliLineInputNumber = 1
fileInputNumber = 2
floatingInputNumbers = []


def convertInput():
    global inputChoice, floatingInputNumbers
    inputChoice = int(sys.argv[1])

    if (inputChoice == cliLineInputNumber):
        temp = sys.stdin.readline().split()
        for entry in temp:
            try:
                floatingInputNumbers.append(float(entry))
            except ValueError:
                print(f"{entry} can't be converted to a float")

    elif (inputChoice == fileInputNumber):
        print(sys.argv)
    else:
        print("Argument doesn't match a file input option!\n")


if __name__ == "__main__":
    convertInput()
