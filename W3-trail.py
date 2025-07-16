a = "Hello World"
print(a.lower())

a = " Check to eliminate spaces"
print(a.strip())

a = "Hello, World"
print(a.split("W"))

a = "Hello"
b = "World"
c = a + " " + b
print(c)

a = 23
b = f"my name is bhavana , my age is {a}"
print(b)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

h = f"i am calculating the multiplication {12 * 12}"
print(h)

sam = " Today is the \"Independence\" day"
print(sam)

a = 100
b = 101
if b > a :
    print("b is greater than a")
else:
    print("b is not greater than a")

print(bool("Hello"))
print(bool(15))

x = "Hello"
y =  ' '

print(bool(x))
print(bool(y))

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
print(bool({}))