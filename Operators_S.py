################Arthimetic operators###############  
a = 21
b = 10

c = a + b
print ("Value of c is ", c)

c = a - b
print ("Value of c is ", c )

c = a * b
print ("Value of c is ", c) 

c = a / b
print ("Value of c is ", c)
print(c)

c = a % b
print ("Value of c is ", c)
print(c)

a = 2
b = 3
c = a**b 
print ("Value of c is ", c)
print(c)

a = 10
b = 5
c = a//b 
print(c)
print ("Value of c is ", c)

#############Assignment operator#####################
a=1
b=c=s=g=2
d,e,f = 3,4,'xyz'

##########Unary Operator###############
a=5
a
-a
a=-a
a

##########Comparsion operator or Relational###############
x = 12
y = 14

x=y
# Output: x > y is False
print('x > y is',x>y)

# Output: x < y is True
print('x < y is',x<y)

# Output: x == y is False == is for comparing = is for assigning
print('x == y is',x==y)

# Output: x != y is True
print('x != y is',x!=y)

# Output: x >= y is False
print('x >= y is',x>=y)

# Output: x <= y is True
print('x <= y is',x<=y)

###############logical operators##################

x = 5
y = 10
not(x<6 and y>9)
x<6 and y>9
x<3 or y>12
5<3 or 10>12
x<6 or y>12

print('x and y is',x and y)

print('x or y is',x or y)

print('not x is',not x)

##################Special operators###############
#identity
 
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1]
y3 = [1]
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)  

# Output: True
print(x2 is y2) 

# Output: False
print(x3 is y3)


#Membership

x = 'Hello world'
y = {1:'a',2:'b'}

# Output: True
print('H' in x)

# Output: True
print('hello' not in x) #small letter H

# Output: True
print(1 in y)

# Output: False
print('a' in y)


##################Bitwise operator##############

a = 10  
b = 13
# Print bitwise AND operation   
print(a & b)
2|10|
2|5|-0
2|2|-1
2|1|-0

2|4|
2|2|-0
2|1|-0

1010
0100
-----
0000  

a = 12
b =13
# Print bitwise OR operation
print(a | b)
1010
0100
-----
1110  = 2**3+2**2+2**1+2**0=
         8+4+2+0=14

2**3+2**2+2**1+2**0
 8 +  4 +  2 +  0
 14

a = 10
b = 4
# print bitwise XOR operation 
print(a ^ b)


a = 12
b = 4
# Print bitwise NOT operation 
print(~a)

a = 10
b = 2
# print bitwise left shift operation 
print(a << 2)

# print bitwise right shift operation  
print(a >> 2) 
1010
0100
-----
1110 =11.1000= 2**1+2**0=2
'''
# print bitwise left shift operation  
The left shift operator ( << ) shifts the first operand the 
specified number of bits to the left. Excess bits shifted off 
to the left are discarded. Zero bits are shifted in from the right.
'''
print(a << 2) 
1010
0100
-----
1110.000 =111000.= 2**5+2**4+2**3+2**2+2**1+2**0=40

'''
0 is written as "0"
1 is written as "1"
2 is written as "10"
3 is "11"
4 is "100"
5 is "101"
.
.
1029 is "10000000101" == 2**10 + 2**2 + 2**0 == 1024 + 4 + 1'''


a = 10
b = 4
# print bitwise right shift operation 
print(a >> 2)


#identity operators
x1 = 2
y1 = 2
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

print(x is not z)
print(x is not y)
print(x != y)


#Membership operators
x = ["apple", "banana"]

print("banana" in x)
print("pineapple" not in x)
print("pineapple"  in x)

x = 'Hello world'
y = {1:'a',2:'b'}

# Output: True
print('H' in x)

# Output: True
print('hello' not in x)

# Output: True
print(1 in y)

# Output: False
print('a' in y)

#x+=2
x

x*=3
x

x/=3
x

x//=3
x


# Python program to illustrate the use  
# of 'is' identity operator 
x = '5'
if (type(x) is str): 
    print ("true") 

if x==6: 
    print ("true") 
else: 
    print ("false") 
    
if (type(x) is int): 
    print ("true") 
else: 
    print ("false") 
      
# Python program to illustrate the  
# use of 'is not' identity operator 
x = 5.2
if (type(x) is not int): 
    print ("true") 
else: 
    print ("false") 



# Python program to illustrate 
# Finding common member in list  
# using 'in' operator 
list1=[1,2,3,4,5] 
list2=[6,7,8,9] 
for item in list1: 
    if item in list2: 
        print("overlapping")       
else: 
    print("not overlapping") 
    
    
    
# Python program to illustrate 
# not 'in' operator 
x = 24
y = 20
list = [10, 20, 30, 40, 50 ]; 
  
if ( x not in list ): 
   print ("x is NOT present in given list")
else: 
   print ("x is  present in given list")
  
if ( y in list ): 
   print ("y is present in given list")
else: 
   print ("y is NOT present in given list")
   
   
   
   
   
   
   
