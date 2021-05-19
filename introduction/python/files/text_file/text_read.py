file = open('data.txt')
for line in file:
    print("> {}".format(line), end='')
file.close()
