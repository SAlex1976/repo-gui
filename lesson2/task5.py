# Task_5
# List rating
rating_list = [8, 5, 5, 3, 2]
print(rating_list)
user_number = int(input('Insert the number: '))
for i, number in enumerate(rating_list):
    if user_number < number:
        continue
    rating_list.insert(i, user_number)
    break
else:
    rating_list.append(user_number)
print(rating_list)