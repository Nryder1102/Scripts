from math import *
from graphics import *
def calc():
    cont = 1
    h = 0
    
    m = int(input("Input how many numbers: "))
    a = input("Input 1 operation [/][*][+][-]: ")
    a = a
    print(a)
    for i in range(m):
        t = int(input("Input number: "))
        h = t = h
        print(h)
    if a == "/":
        h = t / h
        print(h)
    if a == "*":
        h = h * h
        print(h)
    if a == "+":
        h = t + h
        print(h)
    if a == "-":
        h = t - h
        print(h)
    print(h)
    print("Your equation's outcome is:",h)
    confirm = input("Would you like to continue? [Y/N]: ")
    if confirm == "y" or "Y":
        calc()
                    
        
        
calc()
