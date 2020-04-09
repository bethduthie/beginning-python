import random

nums = range(1, 50)

lottery = []

for i in range(5):
    random_num = random.choice(nums)
    while random_num in lottery:
        random_num = random.choice(nums)
    lottery.append(random_num)


lottery.sort(reverse=False)

print(lottery)
