#Create a function:
def my_fellows():
     print("Hi")
     print("How are you")
     my_fellows()

#Call a function:
def my_fellows():
     print("Hi")
     print("How are you")
my_fellows()

#Arguments in functions:
def my_fellows(fname):
    print(fname + " " + "is my fellow")
my_fellows("sheraz")
my_fellows("Ali")
my_fellows("Amir")
#Number of Arguments:
def my_fellows(fname,lname):
    print(fname+"  "+lname)
my_fellows("Sheraz","Rana")
my_fellows("Ali","Sharjeel")
my_fellows("Amir","nawaz")

#pass two arguments and get 1 argument:
def my_fellows(fname,lname):
    print(fname+"  "+lname)
my_fellows("Sheraz","Rana")# if we get 1or3 arguments in function . then error will be occure.

#Arbitrary Arguments, *args:
def my_fellows(*fellows):
      print("my class fellows is="+ " "+ fellows[1])
my_fellows("Sheraz","Ali","Amir")

#Keyword Arguments:
def my_fellows( fellow1,fellow2,fellow3 ):
    print("my best fellow is"+fellows[3])
    my_fellows(fellow1= "Sheraz", fellow2=  "Ali" , fellow3= "Amir")
#By passing the Arbitrary Keyword Arguments, **kwargs:
def my_friends(**friends):
  print("Hes last name is " + friends["lname"])
my_friends(fname = "Amir", lname ="Nawaz")

#By passing Default Parameter Value:
def my_function(country = "Pakistan"):
  print("I am from " + country)

my_function("Sweden")
my_function()
my_function("india")
my_function("pakistan")

#By Passing a List as an Argument:
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "grapes","orange"]

my_function(fruits)

#Return Values:
def my_function(x):
  return 4 * x

print(my_function(56))
print(my_function(76))
print(my_function(9))
#The pass Statement:
def  my_function():
    pass
# having an empty function definition like this, would raise an error without the pass statement

# Recursive FUNCTION:


def tri_recursion(j):
  if(j > 0):
    result = j + tri_recursion(j - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

# Methods
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#Modify Object Properties

p1.age = 40
print(p1.age)