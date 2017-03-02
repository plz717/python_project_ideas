import re


def replace(source, target, file):

    f = open(file, 'r')
    all_lines = f.readlines()  # read all lines into memory
    f.close()

    with open(file, 'w') as f_new:  # totally covered original contents
        for line in all_lines:
            if source in line:
                print("source in line")
                f_new.write(re.sub(source, target, line))
            else:
                f_new.write(line)
            # f_new.close()
    return f_new


a = replace('0', 'a',
            '/home/plz/python_program/python简明教程/README')
