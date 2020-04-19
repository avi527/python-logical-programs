# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
a=7
b=5
for i in range(2000,3201):
	if (i%a==0) and (i%b!=0):
		print(i,end=",")
print("---------------------------------------------")

# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
input_factorial=9
fact=1
for i in range(fact,input_factorial):
	fact=fact*i
	print(i,fact)
print("---------------same question 2nd way ------------------")

userinput=int(input("enter your number"))
factorial=1
for factnum in range(factorial,userinput+1):
	factorial=factorial*factnum
	print(factorial)

print("---------------------------------")
# Question:
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) 
# such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

n=8
d=dict()
for i in range(1,n+1):
	d[i]=i*i
print(d)
 
print("---------------------------------")

# Question:
# Write a program which accepts a sequence of comma-separated numbers
# from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

num=34,67,55,33,12,98
print(list(num))
print(num)
print("--------------------------------")

# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class Test:
	def __init__(self,myinput):
		self.myinput=myinput
	def getString(self):
		print(self.myinput)
	def printString(self):
		print(self.myinput.upper())
myinput=input("enter your text")
t=Test(myinput)
t.getString()
t.printString()
print("----------------------------------")
