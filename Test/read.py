with open('textfile.txt', 'r') as readdata:
    print(readdata.read())

with open('textfile.txt', 'a+') as writedata:
    writedata.write('\nForth line by python.')

with open('textfile.txt', 'r') as readdata:
    print(readdata.read())