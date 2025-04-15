
inpt = input('Type your name: ')
print(inpt)

inpt = float(input('What is the temperature in F: '))
cel = (inpt - 32) * 5/9
print(f"The temperature in degrees celcius is", {cel})

print("Hello World")
print("Hello\nWorld")

numbs = {1,2,4,5,6,8,10}
print('Numbers in set', 1, ":", numbs)
print('Numbers in set ', 1, " : ", numbs, sep = "")

name1 = 'Piper'
name2 = 'Niven'
print(f"{name1} says hi to {name2}")