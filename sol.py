import sys

def main():

    # Second Cycle of Read
    file = open(path, "r")
    singleSet = set()
    concatSet = set()

    longest = 0 # Length of the longest concatenated word
    secondLongest = 0 # Length of the second longest concatenated word
    answer = ['a', 'a'] # An array of the longest and the second longest concat-words

    # First identify concatenated words
    for line in file:

        if (line[len(line) - 1] == '\n'):
            line = line.rstrip('\r\n')

        if (len(singleSet) == 0):
            singleSet.add(line)
            continue

        concatedWord = numOfConcat(line, "", 0, [])
        if (concatedWord == 1):
            singleSet.add(line)
        elif (concatedWord > 1):
            concatSet.add(line)
            if (len(line) > longest):
                answer[1] = answer[0]
                secondLongest = longest
                answer[0] = line
                longest = len(line)
            elif (len(line) > secondLongest):
                answer[1] = line
                secondLongest = len(line)

    print("The longest concatenated word is: " + str(answer[0]) + " / length: " + str(len(answer[0])))
    print("The second longest concatenated word is: " + str(answer[1]) + " / length: " + str(len(answer[1])))
    print("The total number of concatenated words is: " + str(len(concatSet)))

    file.close()

# word: each word from our text file
# currentWord: previous prefix that is in the dictionary
# index: starting index we want to iterate through the target word
# prefix: a list of possible prefix of the target word
def numOfConcat(word, currentWord, index, prefix):
    partition = prefix
    w = currentWord

    for c in word[index:]:
        w += c
        if (w in dictionary):
            partition.append(w)
            w = ""

    if (w != ""):
        newWord = partition.pop()
        start = 0
        for prevWord in partition:
            start += len(prevWord)
        return numOfConcat(word, newWord, start + len(newWord) , partition)
    return len(partition)

if __name__ == "__main__":
    # argv: sol.py - filePath
    if (len(sys.argv) != 2):
        print("Wrong number of arguments: Please include your path of the file.")
        exit(1)
    path = str(sys.argv[1])

    # First Cycle of Read
    dictionary = set()
    file = open(path, "r")
    for line in file:
        if (line[len(line) - 1] == '\n'):
            line = line.rstrip('\r\n')
        dictionary.add(line)
    file.close()
    main()
