msg = "hello world"
print(msg)


x = 2 + 2
y = "Jason"
print(x)
print(y)

x = "awesome"
print("Prime is " + x)


# Return type of object
x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))
# returns
# <class 'int'>
# <class 'float'>
# <class 'complex'>

x = str("s1")
y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)
#  returns s1, 2, 3.0

# LISTS
thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = list(("apple", "banana", "cherry"))
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Remove last item
# thislist.pop() 

# Remove item
# thislist.remove("banana")

#  Add to end
# thislist.append("orange")

# Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
# print 3

# Check to see if item exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# Prints out character at position
a = "Hello, World!"
print(a[1])
# return e


# Creates set
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Check
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
# Returns a is greater than b

#and
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# or 
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# Print dictionary
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)
"""
returns
brand Ford
model Mustang
year 1964
"""

#create array
cars = ["Ford", "Volvo", "BMW"]
print(cars)
# Return ['Ford', 'Volvo', 'BMW']

# Creating a class 
class MyClass:
  x = 5

print(MyClass)
# Prints <class '__main__.MyClass'>

#Creating objects
class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)
# return 5

# convert Python to json
import json
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)
# Returns {"name": "John", "age": 30, "city": "New York"}

# Convert json to Python
import json
# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])
# Returns 30


# Creating a function 
def myFunction():  

# List: ["apple", "banana", "cherry"]  
# Tupple: ("apple", "banana", "cherry")  
# Set: {"apple", "banana", "cherry"}  
# Dictionary: {"name": "apple", "color": "green"}  
# If statment: if x > y:  
# while: while x > y:  
# Writing a for loop: for x in y:  
