                                #Python Operators

#---------------------------Python Arithmetic Operators---------------------

'''
Operator 	Name 	            Example 	
+ 	        Addition 	           x + y 	
- 	        Subtraction 	        x - y 	
* 	        Multiplication 	        x * y 	
/ 	        Division 	            x / y 	
% 	        Modulus 	            x % y 	
** 	        Exponentiation 	        x ** y 	
// 	        Floor division 	        x // y
'''

x=12
y=5

#-------------------------Addition------------
ans=x+y
mystr="Sum of {} and {} is : {}"
print(mystr.format(x, y, ans))
#Sum of 12 and 5 is : 17

#-------------------------Subtraction------------
ans=x-y
mystr="Subtraction of {} and {} is : {}"
print(mystr.format(x, y, ans))
#Subtraction of 12 and 5 is : 7

#-------------------------Multiplication------------
ans=x*y
mystr="Multiplication of {} and {} is : {}"
print(mystr.format(x, y, ans))
#Multiplication of 12 and 5 is : 60

#-------------------------Division------------
ans=x/y
mystr="Division of {} and {} is : {}"
print(mystr.format(x, y, ans))
#Division of 12 and 5 is : 2.4

#-------------------------Modulus------------
ans=x%y
mystr="Modulus of {} and {} is : {}"
print(mystr.format(x, y, ans))
#Modulus of 12 and 5 is : 2

#-------------------------Exponentiation------------
x=5
y=2
ans=x**y
mystr="Exponentiation of {} and {} is : {}"
print(mystr.format(x, y, ans))
#Exponentiation of 5 and 2 is : 25

#-------------------------Floor division------------
x=20
y=3
ans=x//y
mystr="Floor division of {} and {} is : {}"
print(mystr.format(x, y, ans))
#Floor division of 20 and 3 is : 6

#---------------------------End of Arithmetic Operators---------------------