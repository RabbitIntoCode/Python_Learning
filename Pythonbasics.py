# Single line with int datatype and separator
print('Hello User','Welcome to learning Material',1,sep="/")
#Multi line print (use 3 '' or "")
print('''Hello User,
'Welcome to learning Material',1''')
#print 'Welcome to learning Material'-along with single quotes in single line --> cna use Escape character(\)
print('Hello User \'Welcome to learning Material\'',1)


#Multi Variable assignment
x, y , z = 1,10, 20
#if all variables are same
a=b=c =30


#Multi-line code
a = 10+20+30+\
    30+40+50
print(a)
b = (10+20+30
    +30+40+50)
print(b)


#Type Casting
a = type(1.2)
print(a)

#implicit type casting
a = 10
b =20.56
print(type(a+b))

#Explicit Typecasting
b = input()
c  = int(b) 
print(type(c)) 

print(type(6//2)) # gives int 

print(("hello" == "world")) # gives boolean type

#String Operations

#Indexing 0-n and Slicing
x  = 'India'
print(x[0])
print(x[:]) #this means 0:len(x)
print(x[3:])
print(x[:len(x)])
#Replace in String 
x  = 'India'
print(x.replace('In' ,'Proud of In'))
#Separate values by  a special character and Store/display then in the form of a list
x  = 'Proud of India'
my_list  = x.split(" ")
print(my_list)

#If with startwith and endswith fn's
file = "raw_data.orc"
if file.startswith("raw") and file.endswith(".csv"):
    print("Raw CSV File")
else:
    print("Not Raw csv file")

# Word Count 
x = "India is my country and all Indians are patriotic about their country except some who are considered as sleepercells"
print(x.count("India"))

#Without Raw String ('):
raw_string = "C:\new_folder\file.txt"
print("Raw String:", raw_string)

#With Raw String ('r):
raw_string = r"C:\new_folder\file.txt"
print("Raw String:", raw_string)

#Pass real time values to print
#i) .format() 
name = "Rabbit"
age = 50
print("My name is {} and I am {} years old.".format(name, age))

#ii) % Operator 
name = "Johnathan"
age = 30
print("My name is %s and I am %d years old." % (name, age))


#isfunctions (isnumeric, isalnum,isalpha)--applicable only for strings ,Returns Error on application for other data types
var_space = 'Rabbit 123! , Enjoy learning!'
var = 'Rabbit'
print(var.isalnum()) #True, rabbit123 also returns true
print(var.isnumeric()) #False
print(var.isalpha()) #True
#Returns False as it contains special characters(" ")
print(var_space.isalnum()) #False
print(var_space.isnumeric()) #False
print(var_space.isalpha()) #False

# To print if special characters present in our string ignoring spaces
import re

def contains_special_characters(input_string):
    # Define a regular expression pattern to match special characters.
    # [^a-zA-Z0-9\s] matches any character that is NOT a letter (a-z, A-Z),
    # a digit (0-9), or a whitespace character (\s).
    special_char_pattern = re.compile(r'[^a-zA-Z0-9\s]')
    
    # Use the search() method to find the first occurrence of the pattern in the string.
    # If a match is found, search() returns a match object; otherwise, it returns None.
    if special_char_pattern.search(input_string):
        return True
    else:
        return False

# Example usage:
var_space = 'Rabbit 123! , Enjoy learning!'
string2 = "This is a normal string12"


print(f"'{var_space}' contains special characters: {contains_special_characters(var_space)}")
print(f"'{string2}' contains special characters: {contains_special_characters(string2)}")

#Conditional Statements:
# IF , ELif, Else , Nested if use cases:
#1.Dog or cat person
catsOrDogs = input("Are you a cat person? Or a dog person?: ")
if catsOrDogs == "cat":
  print("Meow")
elif catsOrDogs == "dog":
  print("Woof")
else:
    print("Invalid input")
#Nested IF Else
#2. Find the largest of 3 numbers 
x, y, z = 40,20,30
if(x>y):
    if(x>z):
        print("{} is greatest".format(x))
    else:
        print("{} is largest".format(z))
else:
    if(y>z):
        print("{} is greatest".format(x))
    else:
        print("{} is largest".format(z))
        
# 3. Check if a year is a leap year or not
'''Rules:
A year is leap if: divisible by 4, and (not divisible by 100 unless divisible by 400)'''
year = int(input("Enter the year"))
if(year%4 == 0):
    if(year%100 == 0):
        if(year%400 == 0):
            print("Leap Year")
        else:
            print("Not Leap year")
    else:
        print("Leap year")
else:
    print("Not Leap year")


#LOOPS
#For Loop : Executes in  a valid Window /Range

tab_list = ["Orders","customers","Products"]
for i in tab_list:
    if(i.lower() == "orders"):
        print("Table Order")
    else:
        print("No Table Order")
# To consider integers for a specific range 
for i in range(1,10):
    print(i)
# See the execution of nested for loop
for i in tab_list:
    print(i)
    for x in i:
        print(x)

#break(intepreter stops the execution of that loop then and there as soon as this word is encountered and comes out of the loop)
# i value won't be incremented further after break
tab_list = ["Orders","customers","Products"]
for i in tab_list:
    if(i.lower() == "orders"):
        break
    print(i) #No o/p
tab_list = ["Orders","customers","Products"]
for i in tab_list:
    if(i.lower() == "orders"):
        break
print(i) #o/p = Orders(executes the latest i value)
      
#continue(If we don't want to process a particular tables data but want to continue with the loop then continue can be used 
# i value will be incremented further after continue
tab_list = ["Orders","customers","Products"]
for i in tab_list:
    if(i.lower() == "orders"):
        continue
print(i) #o/p = Products(executes the latest i value)

tab_list = ["Orders","customers","Products"]
for i in tab_list:
    if(i.lower() == "orders"):
        continue
    print(i) #o/p = customers, Products, If we give print inside if then we won't have any o/p

#While Loop:(doesn't iterate values incrementally), Works as long as the condition is true
#1) Print a string 10 times
x = 1
while(1==1): #Will always be True , hence goes for infinite loop
    x = x+1
    print("hello")
    if(x>10):
        break #breaks infinite loop once the condition is reached
#2) 
x = 1
while(1==1): #Will always be True , hence goes for infinite loop
    x = x+1
    if(x>10):
        print("hello") #o/p only one 'hello' as this condition will be met only one time
        break #breaks infinite loop once the condition is reached

    

