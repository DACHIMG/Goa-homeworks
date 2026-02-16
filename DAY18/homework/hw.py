# while loop_ი ანვითარებს სანამ ჭეშმარიტი არ იქნება
# for loop_ს ბევრჯერ გამოაქვს ტერმინალში რაღაცა და ცვლადს თუ დავუმატებთ შეგვიძლია, რომ სიტყვა დავმარცვლოთ

for i in range(1,11,1):
   print(i)

for i in range(2,20,2):
   print(i)

# for loop_ი გამოიყენება რაღაცის ბევრჯერ გამოტანაში და რაღაცის დამარცვლაში
# while loop_ი ანვითარებს სანამ ჭეშმარიტი არ იქნება

password = "dachi2016"
user_guess = ""

while password != user_guess: 
 user_guess = input(" guess the password: ")
 print("guess until you get it right")
print("you guess it")
