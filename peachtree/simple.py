"""
def devnet() :
    #prints simple function
    print("Simple function")

devnet()
help(devnet)
"""

max(50,3,4,5,6)

def hello(*args):
    for arg in args:
        print("Hi", arg, "!")
hello("Caleb", "Savannah", "Sydney")

def hello(**kwargs):
    for key, value in kwargs.items():
        print("Hello", value, "!")

hello(kwarg1="Caleb", kwarg2="Savannah", kwarg3="Sydney")

def greeting(name, message=". Good morning"):

    print("Hello", name, message)

greeting("Caleb")
greeting("Sydney", ", howdy!")

