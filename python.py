# -*- coding: utf-8 -*-
"""python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B2IS0I6bYwt_2SyzfTK2gTTJQmgny5X4
"""

print("hello world")

age =24
n = "vinayak"
print(age)
print(n)
print("name")
print(n,type(n))

age=30
n="harry"
print(n)
print(age)
str = "monkey eats va"
print(str)



"""Data type in python::::---->>>>
Numeric
Sequence Type
Boolean
Set
Dictionary
Binary Types
"""

### finding type using type()
rate = 4.7
print(rate,type(rate))

"""Arthmatic operation
+	Addition	x + y
-	Subtraction	x - y
*	Multiplication	x * y
/	Division	x / y
%	Modulus	x % y
**	Exponentiation	x ** y
//	Floor division	x // y
"""

a =2
b =67
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

a = 45
b = 54
print('a>b',a>b)
print('b<a',a<b)

"""not operator--> it will always give ooposite of what u have give for ex if u give 0 it will give 1
or opertor--> it will give true if in either of a cases true exist for example
if u have given 0 and 1 it will give 1
AND operator ---> it will give true only if both are true

![download.png](data:image/png;base64,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)
"""

x = True
y = False
print("x and y  is ", x and y)
print("x and y  is ", x or y)
print("x and y  is ", not y)

### input and output
name = input();
### check data type
print(type(name))
## output
print(name)

""" input() will always give u string!!!
to avoid this  we can u type casting just add datatype and u are good to go
int(input())
"""

a = int(input())
b = int(input())
c = a*b
print(c)

"""#### we re using if here after if( cdtn) : use this"""

### if
age = int(input())
if(age==13):
    print(" welcome in you are in your teens")

else:
    print("you are older or younger")

"""the previous example is somewhat in complete we are"""

age = int(input())
if(age==13):
  print("welcome to teens")
elif(age>13):
  print(" you are older")
else:
  print("you are younger champ")

"""### range and list
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
##### list
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
"""

#### lets learn more about lists
## lets make an list now
fruits = ["banana ", "apple", " xtu ", " papya"]
print(fruits[0])
print(fruits[1])
### len function is used to calculate length
print(len(fruits))
###

a = range(10)
print(a)
# now convert it into a list
a = list(a)
print(a)

### for loop
for i in range(10):
  print(2*i)

### runing for loop in list
### u can use any variable in plaace of t
a = ['xbf','huu','bhjj']
for t in a:
  print(t*4)

### lets learn while
n =5
while(n>=0):
  print(n)
  n-=1

### break and countinue
n = 6
for i in range(10):
  if(i==6):
    break;
  print(i)

# it skips the digit
n = 6
for i in range(10):
  if(i==6):
    continue;
  print(i)

# slicing
s = "vinayak"
print(s[1:3])
## cont
t = "sharma"
print(s+t)
## runing for loop
for t_char in s:
  print(t_char)

### is alpha is used to check alphabate
s = "billo"
print(s.isalpha())
t = "billo123"
print(t.isalpha())
print(s.isdigit())
print(s.islower())
# these two were used to make upper or lower
print(s.upper())
print(s.lower())

### yah pa type define nhi karta hai
name = " vinayak"
name = 1234
print(name)

my = ['vinayak ',1234]
print(my)

# creating list
a = [x for x in range(10)]
print(a)
a = [x for x in range(10) if x%2==0]
print(a)

# using append the elemnt apppears in last
b = [x for x in range(10)]
b.append(4)
print(b)
# insert position , value
b.insert(1,56);
print(b)
# sort
b.sort()
print(b)

#pop
b.pop(1)
print(b)
# reverse
b.reverse()
print(b)
#findind index
print(b.index(3))
#clear
b.clear()
print(b)

### more list function
b = [1,2,3,4,5]
# calculate the length
print(len(b))
## calculate the max
print(max(b))
# calculate min
print(min(b))
#sum
print(sum(b))

"""tupes in pythons ------>>>> Tuples are used to store multiple items in a single variable. Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage. A tuple is a collection which is ordered and unchangeable."""

### lets see this
a = [1,2 ,3 ,3]
a[0] = " anuj"
print(a)
### this is list thats why it got changed
a = (1,2,3,4)
a[0] = " anuj"

# it will give eroor
# tuple opperations are same like list but u cant change the assigned thing  len max min

"""Dictionary --->>> What is a dictionary on Python?
In Python, dictionaries are mutable data structures that allow you to store key-value pairs. Dictionary can be created using the dict() constructor or curly braces' {}'. Once you have created a dictionary, you can add, remove, or update elements using the methods dict. update(), dict
"""

# it didnt store duplicate value
a = { 1,2 ,3,4,1,2,}
print(a)

# lets create one
mrks = {'arjun':56,'billo':67,45:67}
print(mrks['billo'])
print(mrks[45])
for i in mrks:
  print(i,mrks[i])
mrks['arjun'] = 100
print(mrks)

# functions in python
# modeule
import math
dir(math)

### function for avg
a = int(input())
b = int(input())
print(avg(a,b))
def avg(a,b):
  return (a+b)/2

#### one more example
def gth(name, dish ):
  print("good morning ",name)
  print("time to eat ",dish )
gth("vinayak","momo")