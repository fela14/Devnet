import csv

samplefile = open('custom.csv')
samplereader = csv.reader(samplefile)
sampledata = list(samplereader)

print(sampledata)
print(sampledata[0])
print(sampledata[0][1])
"""
with open('custom.csv') as data:
    csv_data = csv.reader(data)
    for row in csv_data:
        device = row[0]
        ip = row[1]
        location = row[2]
        print(f"{device} is in {location.rstrip()} and has IP {ip}")
"""
print("Please add a new router to the list.\n")
hostname = input("What is the hostname?: ")
ip = input("What is the ip address?: ")
location= input("where is the current location?: ")
router = [hostname, ip, location]

with open('custom.csv', 'a') as data:
    csv_list = csv.writer(data)
    csv_list.writerow(router)

with open('custom.csv') as data:
    csv_data = csv.reader(data)
    for row in csv_data:
        device = row[0]
        ip = row[1]
        location = row[2]
        print(f"{device} is in {location} and has IP {ip}")    






