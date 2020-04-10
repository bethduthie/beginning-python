# List comprehensions

# nums = range(1, 11)

# my_list = []
# for n in nums:
#     my_list.append()
# print(my_list)

# my_list = [n for n in nums]
# print(my_list)

# my_list = [n*n for n in nums]
# print(my_list)

# my_list = []
# for n in nums:
# 	if n%2 == 0:
# 		my_list.append(n)
# print(my_list)

# my_list = [n for n in nums if n%2 == 1]
# print(my_list)

# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter, num))
# print(my_list)

# my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
# print(my_list)

# Dictionary comprehensions

# names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
# heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# print zip(names, heroes)

# my_dict = {}
# for name, hero in zip(names, heroes):
#     my_dict[name] = hero
# print(my_dict)

# my_dict = {name: hero for name, hero in zip(names, heroes) if name != 'Peter'}
# print(my_dict)

# Set comprehensions
# nums = {1, 1, 2, 3, 3, 4, 4, 5, 5, 7, 7, 8, 9, 9}

# my_set = set()
# for n in nums:
#     my_set.add(n)
# print(my_set)

# my_set = {n for n in nums}
# print(my_set)

# Generator expressions
nums = range(1, 11)


