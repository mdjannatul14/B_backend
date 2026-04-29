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
year = input("your year: ")
year = int(year)

if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
    print(year, "is leap year")   
else:
    print("is not leap year")

