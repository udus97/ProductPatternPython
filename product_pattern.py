def main():
    def patternChecker(firstWord,secondWord):
        # Split the words into an array
        firstWord = list(firstWord.lower())
        secondWord = list(secondWord.lower())

        # Remove whitespace and quotation marks from the words using list comprehension
        firstWord = [x for x in firstWord if x.isalpha()]
        secondWord = [y for y in secondWord if y.isalpha()]

        # compare the lengths of the two words
        # If they are not the same, return false
        if(len(firstWord) != len(secondWord)):
            return False
        else:
            # sort the array containing the words in ascending order
            firstWord.sort()
            secondWord.sort()
            # If the two words are equal, they match our criteria
            if (firstWord == secondWord):
                return True
            else:
                return False
    # Open the file in read mode
    fileName = 'testFile.txt'
    theFile = open(fileName,'r')

    # Loop through each line in the file and remove the newline - \n character
    for eachLine in theFile:
        eachLine = eachLine.rstrip('\n')
        # Split the line into an array of two words where the separator is the ',' character
        eachLine = eachLine.split(',')
        # Pass each word in the array as arguments to the function which checks if they obey the P@tter pattern
        if(patternChecker(eachLine[0],eachLine[1])):
            print("Valid Pattern")
        else:
            print("Invalid Pattern")

    # Close the file handle
    theFile.close()

main()
input()