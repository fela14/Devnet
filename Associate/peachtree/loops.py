
n = 20
if n == 20:
    print('This number is 20')

x = 18
if x == 17:
    print('This number is 17')
elif x < 10:
    print('This number is less than 10')
elif x > 10:
    print('This number is greater than 10')
    
score = int(input("What is your score: "))

if score >= 90:
    print("Grade is A")
elif score >= 80:
    print ("Grade is B")
elif score >= 80:
    print ("Grade is C")
elif score >= 80:
    print ("Grade is D")
elif score >= 80:
    print ("Grade is E")
else:
    print("Grade is F")


Dataset= (1,2,3,4,5)
for x in Dataset:
    print(x)

for a in range(3):
    print(a)

for b in range(1,5):
    print(b)

for c in range(1,22,5):
    print(c)


count = 1
while (count < 5):
    print("Loop count is:", count)
    count += 1
else:
    print("Loop count is finished")

while True:
    x = input("Enter some text to print \n Type 'done' to quit> ")

    if x == 'done':
        break
    print(x)
print('Done!')



