from yaml import load, load_all
import xmltodict
import yaml
import json

kids = ['Caleb', 'Sydney', 'Savanna']
print(kids)
emptylist1 = ['hi', 'hey', 'hola']
print(emptylist1)
kids[1] = "Sidney"
print(kids[1])

a = [1,2,3]
b = [4,5,6]
c = a + b
print (c)
d = [1,2,3,4,5,6,7,8,9,10]
print (d[1:5])
print (d[0:-4])
print (d[:])
print (d.clear())
print (d.sort())

person = (2012, 'Mike', 'CCNA')
print(person)
print(type(person))
print(person[0])
#person[0] = 15
#print(person[0])

(a, b, c) = ("fred", "latana", "nike")
print(a)
print(c)
print(b)

cabinet = { 
    "scores": (19,76,85),
    "name": "Chris",
    "company": "Cisco"
}
print(type(cabinet))
print(cabinet["scores"])
print(cabinet["name"])
print(cabinet["company"])

cabinet["address"] = {
    "street": "123 Anywhere Dr",
    "city": "Franklin",
    "state": "IN"
}
print(cabinet["address"])

numbs = {1,2,4,5,6,8,10}
odds = {1,3,5,7,9}
print(type(numbs))
print(type(odds))
print(numbs | odds)
print(numbs & odds)

stream = open('sample.json', 'r')
document = json.load(stream)
for doc in document:
    print(doc)





with open('custom.json', 'r') as data:
    jsondata = data.read()
    jsondict = json.loads(jsondata)
    print(jsondict['Interface'][1]["description"])

    jsondict['Interface'][1]["description"] = "Uplink -> Equinix"

with open('custom.json', 'w') as jdata:
    json.d = json.dump(jsondict, jdata, indent=2)
    print(jsondict['Interface'][1]["description"])

x = 0
while True:
    try:
        # prompts user to enter name of file
        filename = input("Which file would you like to open: ")
        with open(filename, 'r') as data:
            readfile = data.read()

    except FileNotFoundError:
        # error message for incorrect filename
        print(f"Sorry {filename} was not found")

    else:
        # correct filename opens the file
        print(readfile)
        x = 0
        break
        
    finally:
        x += 1
        if x == 3:
            # maximum tries exceeded
            print("Please check file name and rerun program")
            break


        
