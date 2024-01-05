'''x,z,y=input("Expression:")
x=float(x)
y=float(y)
if z=="+":
    print("x+y")
if z=="-":
    print("x-y")
if z=="*":
    print("x*y")
if z=="/":
    print("x/y")'''
x, y, z = input("arithmetic expression: ").split(" ")

if y == "+":
    print(float(x) + float(z))
elif y == "-":
    print(float(x) - float(z))
elif y == "*":
    print(float(x) * float(z))
elif y == "/":
    print(float(x) / float(z))
