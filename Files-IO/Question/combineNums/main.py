# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping(common). One .txt file
# has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.

def getPrimeNumbers(pFile):
    with open(pFile, "r") as file:
        prime_numbers = file.read().strip().split()
        prime_numbers = set(map(int, prime_numbers))
    return prime_numbers


def getHappyNumbers(hFile):
    with open(hFile, "r") as file:
        happy_numbers = file.read().strip().split()
        happy_numbers = set(map(int, happy_numbers))
    return happy_numbers


if __name__ == "__main__":
    prime_file = "combineNums\primenumbers.txt"
    happy_file = "combineNums\happynumbers.txt"
    combine_file = "combineNums\overlapping_numbers.txt"

    prime = getPrimeNumbers(prime_file)
    happy = getHappyNumbers(happy_file)

    overlapping_numbers = prime.intersection(happy)
    overlapping_numbers = sorted(overlapping_numbers)
    print(f"Their are total {len(overlapping_numbers)} common numbers.")

    with open(combine_file, "w") as file:
        file.write(
            f"Their are total {len(overlapping_numbers)} common numbers.\n")
        for num in overlapping_numbers:
            file.write(f"{num}\n")
