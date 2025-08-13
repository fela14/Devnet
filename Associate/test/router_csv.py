import csv

my_router = open('router.csv')
read_router = csv.reader(my_router)
list_router = list(read_router)
print(list_router)

print(list_router[0][0])
print(list_router[1][1])
print(list_router[2][2])

with open('router.csv') as your_router:
    read_your_router = csv.reader(your_router)
   
    for row in read_your_router:
        device = row[0]
        ip = row[1]
        location = row[2]

        print(f'{device} is in {location.rstrip()} and has ip {ip}')

print("####### Adding new router to list #######")
device = input('Enter device name: ')
ip = input('Enter ip address: ')
location = input('Enter device\'s location: ')
router = [device, ip, location]

with open('router.csv', 'a', newline='') as data:
    write_data = csv.writer(data)
    write_data.writerow(router)

with open('router.csv') as your_router:
    read_your_router = csv.reader(your_router)
   
    for row in read_your_router:
        # if not row:
        #     continue
        device = row[0]
        ip = row[1]
        location = row[2]

        print(f'{device} is in {location.rstrip()} and has ip {ip}')
