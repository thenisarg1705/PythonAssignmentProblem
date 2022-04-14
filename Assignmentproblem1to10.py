#problem 1
#You are given a string. Your task is to count the frequency of letters of the string and
#print the letters in descending order of frequency.
#If the following string is given as input to the program: aabbbccde
#Then, the output of the program should be:
#b 3
#a 2
#c 2
#d 1
#e 1
#code:
st = input("Enter String : ") dicts = {}
for ch in st:
if ch in dicts: dicts[ch] += 1
else:
dicts[ch] = 1 l = len(set(st))
for i in range(0, l): maxli = [0, 0] for key in dicts:
if dicts[key] > maxli[1]: maxli[0] = key maxli[1] = dicts[key]
print(maxli[0] + " " + str(maxli[1])) dicts.pop(maxli[0])


#problem 2
#Write a procedure to find min, max, mean, standard deviation, variance of number list.
#Exampl e
#Input : 10 50 80 70 49 23 11 4
#output : 4 80 37. 13 27. 25 848. 70
#code:
numbers = list(map(int,input("Enter numbers : ").split())) import numpy
import statistics

def Average(lst):
return sum(lst) / len(lst) print("Minimum : " + str(min(numbers)))
print("Maximum : " + str(max(numbers))) print("Average : " + str(Average(numbers)))
print("Standard Deviation : " + str(statistics.stdev(numbers))) print("Vartiance : " + str(numpy.var(numbers)))


#problem 1
#You are gi ven an i nteger array hei ght of lengt h n. There are n vertical lines dra wn such
#that the t wo endpoi nts of the ith line are (i, 0) and (i, hei ght[i]).
#Find two lines that together with the x-axis form a container, such that the container
#contains the most water.
#Return the maximum amount of water a container can store. Notice that you may not slant the container.
#Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
#Output: 49
#Explanation: The above vertical lines are represented by array [1, 8, 6, 2, 5,4, 8, 3, 7]. In
#this case, the max area of water (blue section) the container can contain is 49.
#Example 2:
#Input: height = [1, 1]
#Output: 1

heights = list(map(int,input("Enter numbers : ").split())) maxh = 0
for i in heights: if i > maxh:
maxh=i


maxh2 = 0 heights.pop(heights.index(maxh)) for i in heights:
if i > maxh2:
maxh2=i print(maxh2*maxh2)



#Problem:4           Given a list of integers, write a program to print the count of all possible unique
#combinations of numbers whose sum is equal to K. Input
#The first line of input will contain space-separated integers. The second line of input will contain an integer, denoting K. Output
#The output should be containing the count of all unique combinations of numbers
#whose sum is equal to K. Sample Input 1
#2 4 6 1 3
#6
#Sample Output 1
#3

from itertools import combinations

values =[int(i) for i in input('Enter space-separated integers: ').split()]
values.sort()

K = int(input('Enter K: ')) counterUniqueCombinations=0
print("The unique combinations with the sum equal to "+str(K)+" are:")
for i in range(1, len(values)+1):
com =list(set(combinations(values, i))) for combination in com:
if sum(combination) == K: print(combination) counterUniqueCombinations += 1
print("The count of all unique combinations is: "+str(counterUniqueCombinations))






#Explain about the different types of Exceptions in Python with suitable example.

#Some of the basic inbuilt exceptions are: 1.exception ArithmeticError
#This class is the base class for those built-in exceptions that are raised for various arithmetic errors such as:
#•	OverflowError
#•	ZeroDivisionError
#•	FloatingPointError


try:
a = 10/0 print (a)
except ArithmeticError:
print ("This statement is raising an arithmetic exception.")
else:
print ("Success.")





# problem7 Write a django code to send an email with attachment
#code
from django.shortcuts import render from .forms import ContactForm
from django.core.mail import send_mail

def contactview(request): name=''
email='' comment=''

form= ContactForm(request.POST or None) if form.is_valid():
name= form.cleaned_data.get("name") email= form.cleaned_data.get("email") comment=form.cleaned_data.get("comment")


comment= name + " with the email, " + email + ", sent the following message:\n\n" + comment;
send_mail('The title of this post', comment, 'admin@gmail.com', ['admin@gmail.com'])


context= {'form': form}
return render(request, 'contact/contact.html', context) else:
context= {'form': form}
return render(request, 'contact/contact.html', context)




#problem:8	Program to demonstrate the Overriding of the Base Class method in the Derived Class
Code	class P1_class():

def show(self):
print("Inside Parent Class 1")


class P2_class():

def display(self):
print("Inside Parent Class 2")
 
	
class Child_class(P1_class, P2_class): def show(self):
print("Inside Child Class")


obj = Child_class()

obj.show() obj.display()






#problem:9	Write Pythonic code to create a function named move_rectangle() that takes an object of Rectangle class and two numbers named dx and dy. It should change the location of the Rectangle by adding dx to the x coordinate of corner and adding dy to the y
#coordinate of corner.
#Code	
class Point(object): pass

class Rectangle(object): pass

rectangle = Rectangle()

bottom_left = Point() bottom_left.x = 8.0
bottom_left.y = 3.0

top_right = Point() top_right.x = 9.0
top_right.y = 6.0

rectangle.corner1 = bottom_left rectangle.corner2 = top_right

dx = 15.0
dy = 16.0

def move_rectangle(rectangle, dx, dy):
print(f"The rectangle started with bottom left corner at ({rectangle.corner1.x},{rectangle.corner1.y})"
f"\nTop right corner at
 
	({rectangle.corner2.x},{rectangle.corner2.y})" f"\ndx is {dx} and dy is {dy}")
rectangle.corner1.x = rectangle.corner1.x + dx rectangle.corner2.x = rectangle.corner2.x + dx rectangle.corner1.y = rectangle.corner1.y + dy rectangle.corner2.y = rectangle.corner2.y + dy print(f"It ended with a bottom left corner at
({rectangle.corner1.x},{rectangle.corner1.y})" f"\nTop right corner at
({rectangle.corner2.x},{rectangle.corner2.y})")

move_rectangle(rectangle, dx, dy)
