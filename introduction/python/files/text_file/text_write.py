with open('data.txt','r') as in_file:
    content = in_file.readlines()
    print(content)

with open('tmp.txt','w') as out_file:
    data = reversed(content)
    out_file.writelines(data)
