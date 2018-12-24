# Day 1

def readFile():
    frequencyList = []

    file = open("input.txt", "r")

    for x in file:
        frequencyList.append(int(x))

    file.close()

    return frequencyList

def part1(frequencyList):
    sum = 0
    for x in frequencyList:
        sum += x
    return sum

def part2(frequencyList):
    resultingFrequencyList = set()
    firstFrequencyReachesTwice = 0
    duplicateResultingFrequency = False
    sum = 0

    resultingFrequencyList.add(0)
    
    while not duplicateResultingFrequency:
        for x in frequencyList:
            sum += x

            if sum in resultingFrequencyList:
                duplicateResultingFrequency = True
                firstFrequencyReachesTwice = sum
                break

            resultingFrequencyList.add(sum)

        if duplicateResultingFrequency:
            break

    return firstFrequencyReachesTwice

def main():
    frequencyList = readFile()
    part1answer = part1(frequencyList)
    print("Part 1: " + str(part1answer))

    part2answer = part2(frequencyList)
    print("Part 2: " + str(part2answer))

main()
