number_of_quick_picks = int(input("How many quick picks?: "))
import random
random_list = []
random_number = 0
for i in range(number_of_quick_picks):
    for j in range(6):
        random_number = random.randint(1, 45)
        while random_number in random_list:
            random_number = random.randint(1,45)
        random_list.append(random_number)
    random_list.sort()
    print(random_list)
    random_list.clear()