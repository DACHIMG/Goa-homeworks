numbers = {1, 2, 3, 4, 5}
numbers = {1, 5}
print(numbers)
# ცვლადსა და სიას შორის განსხვავება არის, რომ ცვლადი გამოიყენება რაღაცა სახელის შესანახად და სია გამოიყენება რაღაცა ელემენტების ჩამოსაწერად და სახელის შესანახად
# index_ინგი არის, რომ როცა სია გაქვს ჩამოწერილი და ერთი ელემენტის გამოტანა გინდა index_ინგით გამოიტან
# სიები გვეხმარება, რომ რაღაცა ელემენტები შევინახოთ და ჩამოვწეროთ
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(nums[4])
print(nums[-1])
print(nums[3:7])
print(nums[3])
nums[1] = 25
print(nums)

students = ["Alex", "Ben", "Chris", "David", "Elena", "Frank", "George"]
top_three = students[3]
print(top_three)
print(students[2])
students.append("Hannah")
students.remove("David")
print(students)
print(students[-2:])
# ლისტი Python-ში არის მონაცემთა ტიპი, რომელიც ინახავს რამდენიმე მნიშვნელობას ერთ ცვლადში.
# slice_ინგით შეგვიძლია რომელიმე ელემენტი ამაოვიღოთ
