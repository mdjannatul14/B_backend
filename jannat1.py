"""#dataa type
#int data typy
a = 10
print(a)

#flot data typy
a = 3.33
print(a)

#range data type 
number = range(0,100,2)
print(*number)

number2 = range(00,1000,200)
print(*number2)

#conditional lojic

sex = input("your sex point:")
sex = int(sex)

if sex <= 80:
    print("med")
elif 81 <= 100:
    print("powerfull")
else:
    print("you are gay")"""

#leap year

"""year = input("year: ")
year = int(year)

if year % 4 == 0:  
    if year % 100 == 0 and year % 400 == 0:
        print( year, "is leap year")
    elif year % 100 != 0:
        print(year, "is leap year")
    else:
        print(year, "is not leap year")
else:
    print(year, "is not leap year")
"""
#short
"""year = input("your year: ")
year = int(year)

if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
    print(year, "is leap year")   
else:
    print("is not leap year")"""

"""x = ['1','2','3']
y = x[1] + x[2]
print(y)"""



"""def namota_er_ghor(n):
    print(n, "x 1 =",  n*1)
    print(n, "x 2 =",  n*2)
    print(n, "x 3 =",  n*3)
    print(n, "x 4 =",  n*4)
    print(n, "x 5 =",  n*5)
    print(n, "x 6 =",  n*6)
    print(n, "x 7 =",  n*7)
    print(n, "x 8 =",  n*8)
    print(n, "x 9 =",  n*9)
    print(n, "x 10 =",  n*10)

n = input("inter yout number: ")
n = int(n)
for i in range(1,n+1):
    namota_er_ghor(i)
    print()

def namoter_ghor(n):

    for i in range(1,11):
        print("{} x {} = {}".format(n,i,n*i))
namoter_ghor(5)"""

"""number = input("your number: ")
number = int(number)

for i in range(number,101,):
    print(i)
"""


"""#mini calculator
number1 = input("your frist number: ")
number2 = input("your secound number:")

number1 = int(number1)
number2 = int(number2)

sum = (number1 + number2)
print(sum)

#celsius to fahrenheit
celsius = input("your celsius: ")
celsius = float(celsius)

fahrenheit = (celsius * 9/5) + 100
print(fahrenheit)"""

#mini project
"""name = input("you name: ")
age = input("your age: ")
age = int(age)

if age >= 18:
    print(name+" congratulation you are adult and your eligible for vote")

else:
    print("sorry "+name+" you are a child and you are not eligible for vote")"""



import math
import os
import random
import re
import sys



"""if __name__ == '__main__':
    n = int(input().strip())
    

if (n % 2) == 1:
    print('Weird')
    
elif (n % 2) == 0 and 2 < n > 5:
    print("Not Weird")
elif (n % 2) == 0 and 6 < n > 20:
    print("weird")
elif (n % 2) == 0 and n <= 20:
    print("Not Weird")"""



"""def leap_year(year):
    leap = False

    if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
        print(year,True)
    else:
        print(year,False)
    # Write your logic here
    
    return leap

year = int(input())
print("is_leap"(year))
"""


"""if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end="")


x = int(input())
y = int(input())
z = int(input())
n = int(input())

result = [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n]
print(result)
"""

"""if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr=[]
    for i in range(n):
        arr.append(int(input()))
        arr.sort()
    print(arr[-2])
"""




                