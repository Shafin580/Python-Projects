

import re

print("Python Calculator:\n")
print("type 'quit' to exit the program.\n")

run=True
previous = 0

def perform_math():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        run = False
        print("Calculator closed!")
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
            print("Result: ", previous)
        else:
            previous = eval(str(previous) + equation)
            print("Result: ", previous)

while run:
    perform_math()






