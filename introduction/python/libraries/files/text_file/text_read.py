file = open('data.txt', 'r', encoding="utf-8")
for line in file:
    print(f"> {line}", end='')
file.close()
