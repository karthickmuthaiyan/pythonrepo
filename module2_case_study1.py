#Question 1)
nums = set([1,1,2,3,3,3,4,4]) 
print(len(nums))
print(nums)
#Ans: 4

#Question 2)
d = {"john":40, "peter":45} 
print(list(d.keys())) 
#Ans: ['john','peter']

#Question 3)
password = input("Enter your password: ")


has_lower = False
has_upper = False
has_digit = False
has_special = False
special_characters = "$#@"
if len(password) >= 6 and len(password) <= 12:
    has_length = True    
for char in password:
    if char.islower():
        has_lower = True
    elif char.isupper():
        has_upper = True
    elif char.isdigit():
        has_digit = True
    elif char in special_characters:
        has_special = True
    
if has_lower and has_upper and has_digit and has_special and has_length:
    print("Password is valid")
else:
    print("Password is not valid")


#Ans:
#        Enter your password: Gokul#12
#        Password is valid
#        Enter your password: Gokul
#        Passwors id not valid
#

#Question 4
a= [4,7,3,2,5,9]
for i in range(len(a)):
    print("Value in index position "+str(i)+" is "+str(a[i]));


#    Ans: 
#    Value in index position 0 is 4
#    Value in index position 1 is 7
#    Value in index position 2 is 3
#    Value in index position 3 is 2
#    Value in index position 4 is 5
#    Value in index position 5 is 9
   
#Question 5
a= "H1e2l3l4o5w6o7r8l9d"
str=""
for j in range(len(a)):
    if j % 2 == 0:
        str+=a[j]
        #print(a[j])
print(str)

#Ans: Helloworld

#Question 6 
a=input("Enter a string to reverse:")
print(a[::-1])

#    Ans: 
#    Enter a string to reverse: Hello World
#    dlroW olleH


#Question 7

def f_count_chars(string):
    count_char = {}
    for char in string:
        if char in count_char:
            count_char[char] +=1 
        else:
            count_char[char] = 1
    return count_char

a=input("Enter a string to count characters:")
result_dict=f_count_chars(a)
for char,count in result_dict.items():
    print (f"{char},{count}")

#Ans
#Enter a string to count characters:Hello
#H,1
#e,1
#l,2
#o,1


#Question 8 
a= [1,3,6,78,35,55,120] 
b=[12,24,35,24,88,120,155]
A=set(a)
B=set(b)
# intersection 
print("Intersection :", A & B) 



# Q: With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this 
# list after removing all duplicate values with original order reserved. 

def f_rem_dup(lis):
    f_list =[]
    for number in lis: 
        if number in f_list:
            continue;
        else:
            f_list.append(number)
    return f_list

v_list = [12,24,35,24,88,120,155,88,120,155]
print("Starting list:",v_list)
result_list = f_rem_dup(v_list)
print("Starting list:", result_list)

#Ans:  
#Starting list: [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
#Starting list: [12, 24, 35, 88, 120, 155]



#Question: 10
# By using list comprehension, please write a program to print the list after removing 
#the value 24 in [12,24,35,24,88,120,155]. 


my_list = [12,24,35,24,88,120,155]
print("Current List", my_list)
new_list=[x for x in my_list if x != 24]
print(new_list)

#Ans:
#Current List [12, 24, 35, 24, 88, 120, 155]
#Enter number to remove :24
#[12, 35, 24, 88, 120, 155]


# Question: 11
#By using list comprehension, please write a program to print the list after removing 
#the 0th,4th,5th numbers in [12,24,35,70,88,120,155]. 

my_list = [12,24,35,24,88,120,155]
print("Current List", my_list)
new_list=[x for (i,x) in enumerate(my_list) if i not in (0,4,5)]
print(new_list)


# Ans
#Current List [12, 24, 35, 70, 88, 120, 155]
#Enter indices to remove :0 4 5
#[24, 35, 70, 155]


# Question 12
# By using list comprehension, please write a program to print the list after removing 
# delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155]. 

my_list = [12,24,35,70,88,120,155]
print("Current List", my_list)
filtered_numbers = [x for x in my_list if x % 5 == 0 and  x % 7 == 0]
my_list=filtered_numbers
print(my_list)

#Ans:
#Current List [12, 24, 35, 70, 88, 120, 155]
#[35, 70]


#Question: 13
# Please write a program to randomly generate a list with 5 numbers, which are 
# divisible by 5 and 7 , between 1 and 1000 inclusive.
import random
def f_random_num():
    num_list=[]
    while (len(num_list)<5):
        n=random.randint(1,1000)
        if n%5 ==0 and n%7 ==0 :
            num_list.append(n)
    return num_list

v_num_list=f_random_num()
print("List of 5 random numers divisible by 5 & 7",v_num_list)
    
#Ans:
# List of 5 random numers divisible by 5 & 7 [630, 980, 735, 70, 455]

#Question 14
# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by 
#console (n>0).


def f_num_compute(n):
    sum=0
    for i in range(1,n+1):
        sum +=i/(i+1)
    return sum


v_num=input("Enter a number > 0 :")    
if int(v_num) <=0 :
    print("Enter a number greater than 0")
else:
    f_num_compute(v_num)