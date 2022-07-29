from cmath import pi


a = 1
b = 3

c = a + b
if c == 4:
    print("#1")

c = a * b 
if c == 3:
    print("#2")

c = b * (a + b)
if c == 12:
    print("#3")

c = b * b - b 
if c == 6:
    print("#4")

    c = pow(b, b) - b 
if c == 24:
    print("#5")

x = 7.17
y = -2.32
z = x / y
if z == -717/232:
    print("#6")

v = pow(y, 5)
print(v)
z = x / v
if z == -280078125 / 2625427072:
    print("#7")

print(bin(15))

def password_change():
    data = 1
    data = 2
    data = 3
    data = 4
    data = 5
    data = 6
    data = 7

    

rotate = False

start = input("start: ")
if start.lower == "yes": 
    rotate = True

while rotate == True: 
    password_change()    

g = "a.b"
h = "c.d"
k = g + h 
print(k)