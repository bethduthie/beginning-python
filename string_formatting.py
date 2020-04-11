# person = {'name': 'Joan', 'age': 23}

# l = ['Joan', 23]

# sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)

# sentence2 = 'My name is {0[0]} and I am {0[1]} years old.'.format(l)

# print(sentence, sentence2)


# class person():

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# P1 = person('Jack', '33')

# sentence = 'My name is {0.name} and I am {0.age} years old.'.format(P1)

# print(sentence)

# sentence = 'My name is {name} and I am {age} years old.'.format(name='Jenn', age='23')
# print(sentence)

# for i in range(1, 11):
#     sentence = 'The value is {:03}.'.format(i)
#     print(sentence)

# pi = 3.14159265

# sentence = 'Pi is equal to {:.2f}.'.format(pi)
# print(sentence)

import datetime
mydate = datetime.datetime(2020, 9, 24, 12, 30, 45)

sentence = '{:%B %d, %Y}'.format(mydate)
print(sentence)



