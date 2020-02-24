punctuation2 = ",.;:!?\"'()[]{}-*<>"
def common_words(file_name):
    fd = open(file_name, "r")
    #our dictionary
    d = {}
    for line in fd:
        for c in punctuation2:
            line = line.replace(c, " ")
        # words is a list of each word in my line of text
        words = line.split()
        for word in words:
            #we do not care about words less than 4 letters long
            if len(word) < 4:
                continue
            # we put the word in the dictionary and increase word count
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
    # by the end I have a dictionary with all the words that appear in the book

    values = list(d.values())
    values.sort(reverse=True)
    common = []
    # just get the first 10 most common words [:10]
    for numbers in values[:10]:
        for keys in d:
            if d[keys] == numbers:
                common.append((keys, numbers))
    print("the most common words are:")
    for i in common:
        print(i[0], i[1], "times")

# end of the function so let's call it:
print("Dracula most common words")
common_words("dracula.txt")
print("Harry Potter most common words")
common_words("hp.txt")

