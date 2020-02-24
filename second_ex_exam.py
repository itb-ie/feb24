def get_letter(file_name, letter):
    with open(file_name) as f:
        appear = 0
        # read line by line
        for line in f:
            appear += line.count(letter)
    return appear

print(get_letter("text.txt", "a"))
