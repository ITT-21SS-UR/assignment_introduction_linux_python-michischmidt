import sys
import math


cliLineInputNumber = 1
fileInputNumber = 2


def convert_strings_into_floats(numbers):
    convertedNumbers = []
    for entry in numbers:
        try:
            convertedNumbers.append(float(entry))
        except ValueError:
            # catching inputs other than floats
            print(f"{entry} can't be converted to a float")
    return convertedNumbers


def get_number_input(option):
    floatingInputNumbers = []
    if (option == cliLineInputNumber):
        print("Please enter floating numbers:")
        temp = sys.stdin.readline().split()
        floatingInputNumbers = convert_strings_into_floats(temp)
    elif (option == fileInputNumber):
        f = open(sys.argv[2], "r")
        temp = f.readline().split()
        f.close()

        floatingInputNumbers = convert_string_sinto_floats(temp)
    else:
        print("Argument doesn't match a floating number input option!\n")
        sys.exit(1)
    return floatingInputNumbers


# adding all values up and dividing by the total number
def calculate_mean(numbers):
    temp = 0.0
    for number in numbers:
        temp += number
    return temp / len(numbers)


# sort values, count total numbers,
# if odd numbers, add mid and to the right and divide
def calculate_median(numbers):
    numbers = sorted(numbers)
    size = len(numbers)
    mid = len(numbers) // 2
    if (size % 2 == 0):
        return (numbers[mid] + numbers[mid - 1]) / 2.0
    else:
        return numbers[mid]


# get mean, adds values up minus the mean to the power of 2
# then the sqr root of the deviation divided by the size is taken
def calculate_deviation(numbers):
    size = len(numbers)
    if (size <= 1):
        return null
    mean = calculate_mean(numbers)
    deviation = 0.0
    for number in numbers:
        deviation += (number - mean)**2
    deviation = math.sqrt(deviation / float(size - 1))
    return deviation


if __name__ == "__main__":
    nums = get_number_input(int(sys.argv[1]))
    mean = calculate_mean(nums)
    median = calculate_median(nums)
    deviation = calculate_deviation(nums)

    print(f"""
    Floating Numbers: {nums}
    Mean: {mean}
    Median: {median}
    Standard Deviation: {deviation}""")
