import re

class PasswordEntry:
    def __init__(self, min, max, letter, password):
        self.min = int(min)
        self.max = int(max)
        self.letter = letter
        self.password = password

    def isValidPart1(self):
        numLetter = self.password.count(self.letter)
        return 1 if numLetter >= self.min and numLetter <= self.max else 0
    
    def isValidPart2(self):
        firstCheck = self.password[self.min - 1] == self.letter
        secondCheck = self.password[self.max - 1] == self.letter
        return 1 if firstCheck ^ secondCheck else 0

def numValidPasswords(passwords, part):
    numValid = 0
    for passwordEntry in passwords:
        numValid += passwordEntry.isValidPart1() if part == 1 else passwordEntry.isValidPart2()
    return numValid

def main():
    with open('input/input2.txt', 'r') as input:
        passwords = [PasswordEntry(*re.split('-| |: ',line.strip())) for line in input]
    
    print("Part 1 answer: ", numValidPasswords(passwords, 1))
    print("Part 2 answer: ", numValidPasswords(passwords, 2))

if __name__ == "__main__":
    main()