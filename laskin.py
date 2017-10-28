def plus ():
    print ("Insert first number:")
    a = raw_input()
    print ("Insert second number")
    b = raw_input
    print (" ")
    print a + b

def minus ():
    print ("Insert first number:")
    c = raw_input()
    print ("Insert second number")
    d = raw_input
    print (" ")
    print "c - d"

def mul ():
        print ("Insert first number:")
        e = raw_input()
        print ("Insert second number")
        f = raw_input
        print (" ")
        print "e * f"

def div ():
        print ("Insert first number:")
        g = raw_input()
        print ("Insert second number")
        h = raw_input
        print (" ")
        print "g / h"

def ExpHelper(a,b):
    i = 0
    tulos = 0
    while i < int(b):
        tulos = tulos + int(a) * int(a)
        i += 1
    return tulos

def Exp():
    a = raw_input("Insert first number: ")
    b = raw_input("Insert second number: ")

    print ExpHelper(a,b)

print ("Welcome to Rekos calculator!")

print ("Do you want to add, substract, multiplie or divide")
lasku = raw_input()

if lasku == "add":
    plus()
if lasku == "substract":
    minus()
if lasku == "multiplie":
    mul()
if lasku == "divide":
    div()
if lasku == "power":
    Exp()
