import sys

def main():

    # Second Cycle of Read
    file = open(path, "r")
    singleSet = set()
    concatSet = set()

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

    longest = 0
    secondLongest = 0
    answer = ['a', 'a']

    # Find the longest and the second longest concatenated words
    for concatWord in concatSet:

        if (len(concatWord) > longest):
            tmp = answer[0]
            answer[0] = concatWord
            longest = len(concatWord)
            if (len(tmp) > secondLongest):
                answer[1] = tmp
                secondLongest = len(tmp)
        elif (len(concatWord) > secondLongest):
            answer[1] = concatWord
            secondLongest = len(concatWord)

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
