# Task: I.Print all numbers from 1 to 100 using a for loop.
for i in  range(1,101):
    print(i)
# II. Write a program to print the sum of the first n natural
# numbers. (n*n+1/ 2)

# n=int(input("enter the n value"))
# sum=0
# for i in range(n+1):
#     sum+=i
# print(sum)
# using the n*n+1/2
# n=int(input("enter the n value"))
# sum=0
# # for i in range(n):
# sum=n*(n+1)//2
# print(sum)

# iii. Print all even numbers between 1 and 50 using a while
# loop.

for i in range(1,51):
    if i%2==0:
    
        print(i)

# iv. Write a program to display the multiplication table of a given
# number. First 20
# num=int(input("enter a number to display multiplication  table"))
# for i in range(1,21):
#     print(num,"*",i,"=",num*i)

# Write a program to calculate the factorial of a number using
# a while loop.
num=int(input("enter a number"))




if num<=0:
    print("enter a valid number")
else:
    fact=1
    i=1
    while(num>=i):
        fact=fact*i
        i+=1
    print(fact)

#  iv. Print all numbers from 1 to 100 that are divisible by 3 and 5
# using a for loop.
   
for i in range(1,101):
    if i%5==0:
        print(i,"divided by 5")
    elif i%3==0:
        print(i,"divided by 3")

       

    



