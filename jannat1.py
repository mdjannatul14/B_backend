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


#mini calculator
number1 = input("your frist number: ")
number2 = input("your secound number:")

number1 = int(number1)
number2 = int(number2)

sum = (number1 + number2)
print(sum)




