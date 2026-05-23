number = 17
if number > 10:
    print("more than 10")
else:
    print("less than 10")

name = input("Enter any number:")
if name == 15:
    print("equal to 15")
else:
    print("not equal to 15")

name = input("Enter any string:")
if name == "group84":
    print("you are correct")
else:
    print("you are wrong")

for number in range(50, 101, 5):
    print(number)

name = "დაჩი მგალობლიშვილი"

for letter in name:
    print(letter)

number = 20

while number <= 50:
    print(number)
    number += 1

("for loop")
for number in range(0, 101):
    print(number)

("while loop")
number = 0
while number <= 100:
    print(number)
    number += 1

("for loop")
for number in range(0, 101):
    print(number)

("while loop")
number = 0
while number <= 100:
    print(number)
    number += 1

("for loop")
for number in range(10, 21):
    print(number)

("while loop")
number = 10
while number <= 20:
    print(number)
    number += 1

("while loop")
number = 100
while number <= 200:
    print(number)
    number += 5

("for loop")
for number in range(100, 201, 5):
    print(number)

("for loop")
for number in range(10, -1, -1):
    print(number)

("while loop")
number = 10
while number >= 0:
    print(number)
    number -= 1

number = (input(" Enter any number: "))
if number > 0:
    print("this number is correct")
elif number < 0:
    print("this number is not correct")
else:
    print("this number is zero")



age = input(" Enter your age: ")
if age == 0-12:
  print("your a child")
elif age == 13-19:
    print("your a tenager (grown up)")
elif age == 20-64:
    print("your an adult")
elif age == 65-120:
    print("your old")
elif age >= 120:
  print("guru or wizard")
else:
    print("incorrect info")

a = input("Enter first number: ")
b = input("Enter second number: ")
c = input("Enter third number: ")

if a >= b and a >= c:
    print("highest number:", a)
elif b >= a and b >= c:
    print("highest number:", b)
else:
    print("highest number::", c)

num = input(" Enter any number 1-7: ")
if num == 1:
    print("monday")
elif num == 2:
    print("thursday")
elif num == 3:
    print("wednesday")
elif num == 4:
    print("thursday")
elif num == 5:
    print("friday")
elif num == 6:
    print("saturday")
elif num == 7:
    print("sunday")
else:
    print("i dont know what day that is")

number = float(input(" Enter any number: "))
if number > 50:
    print(number * 5)
else:
    print(number ** 2)

password = input(" Enter any password: ")
if password == "goa123" :
    print("Password is correct!")
else:
    print("Incorrect password!")

n = int(input(" Enter any number: "))
total = 0
for number in range(1, n + 1):
    total += number
print("total is:", total)
