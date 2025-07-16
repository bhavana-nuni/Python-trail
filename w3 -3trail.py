class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

class fun():
  def __len__(hi):
    return 0
  
myobj = fun()
print(bool(myobj))

def myFunction() :
  return True

print(myFunction())

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

x = 200
print(isinstance(x, int))
print(F"{x:.2f}")

print(5 + 4 - 7 + 3)

thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print(len(thislist))
print(type(thislist))

fruits = ['apple', 'banana', 'cherry']
print(fruits[1])  # banana
fruits.append('mango')  # Can modify


mylist = ["apple", " banana", "mango"]
print(mylist[1])

print(mylist[-1])

print(mylist[2:5])

print(mylist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

thislist = ["apple", "banana", "cherry"]
if "xxxx" in thislist:
  print("Yes, 'apple' is in the fruits list")
else:
   print("not availabke")

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
thislist.insert(2, "watermelon")
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
newlist = ["hitha","neha","latha"]
thislist.extend(newlist)
print(thislist)
thislist.remove("banana")
print(thislist)
thislist.pop(0)
print(thislist)
del thislist[0]
print(thislist)
thislist.clear()
print(thislist)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

a = ["ab", "ba", "cb"]
for i in range(len(a)):
  print(a[i])

a = ["ab", "ba", "cb"]
i = 0
while i < len(a):
  print(a[i])
  i = i + 1

fruits = ["apple", "banana", "cherry", "kiwi"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
  
print(newlist)
newlist = [x for x in fruits]
newlist = [x for x in range(10)]

newlist = [x for x in range(10) if x < 5]

newlist = [x.upper() for x in fruits]

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

def myfun(n):
  return abs(n-50)

thislist = [100, 50, 65,82,23]
thislist.sort(key = myfun)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)



thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)