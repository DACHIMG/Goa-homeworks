print(5 > 3)
print(10 > 20)
print(7 > 7)
print(1 > 5)
print(100 > 50)

print(3 < 5)
print(10 < 2)
print(7 < 7)
print(10 < 2)
print(0 < 1)

print(5 >= 5)
print(10 >= 3)
print(1 >= 1)
print(0 >= 1)
print(2 >= 8)

print(5 <= 5)
print(3 <= 10)
print(8 <= 2)
print(3 <= 3)
print(1 <= 0)

print(5 == 5)
print(3 == 7)
print(0 == 0)
print(2 == 2)
print(10 == 1 )

print(5 != 3)
print(7 != 7)
print(0 != 1)
print(2 != 2)
print(9 != 10)

# <, >, ==, !=, <=, >=.
# logical operators გამოიყენება true ან false_ის გასაგებად
print(5 < 10)
print(5 > 1)
print(6 == 100)

user_number = int(input(" Remember this number: "))
my_number = int(input(" Enter any number: "))

if user_number < my_number:
    print("your number is more than my_number:")
else:
    print("your number is lower than my_number ")

dachi = str(input("Enter any name:"))
giorgi = str(input(" Enter any name: "))

if dachi != giorgi:
    print("it is equal")
else:
    print("it isnt equal")

age = int(input("Enter your age:"))
if age > 18:
    print("it is more than 18")
else:
    print("it is less then 18")