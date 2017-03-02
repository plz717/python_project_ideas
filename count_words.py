def count_words(f):
    'count the seperate words in file f and return the total count'
    all_lines = f.readlines()
    count = 0
    for line in all_lines:
        is_white_spase = True  # initialize the white_spae mode
        for i in range(0, len(line)):
            # white_space mode means: space or the end of a string
            if line[i] == ' ' or line[i] == '\n':
                is_white_spase = True
            elif(is_white_spase):   # only  add count when encounter a letter while in white_space mode
                count += 1
                is_white_spase = False
    print("count is:", count)
    return count


file = open("/home/plz/python_program/project _ideas/README.md")
count = count_words(file)
