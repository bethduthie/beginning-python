# strings
message = 'Hello world'

print(message)

# len = length

print(len(message))

print(message[0])

print(message[0:5])

# .upper() prints in uppercase, .lower() prints in lowercase
# .count('example') counts where something appears in string


greeting = 'Hello'
name = 'Michael'
# message = greeting + ', ' + name
message = '{}, {}. Welcome!'. format(greeting, name)
# message = f'{greeting}, {name}. Welcome!'

# numbers
# addition 3 + 2
# substraction 3 - 2
# multiply 3 * 2
# division 3 / 2
# floor division 3 //2
# exponet 3 ** 2
# modulus 3 % abs()

# comparations (bolian fucntions)
# equal ==
# not equal !=
# greater than >
# less than <
# greater or equal to >=
# less or equal to =

# lists examples

nums = (2) # example number
print(sum(nums)/len(nums))
# finds average

courses = ['history', 'maths', 'pysics', 'compsci']
courses2 = ['art', 'education']

print(courses.index('maths'))

courses.append('art')
# adds art at the end of list

courses.extend(courses2)
# adds second list seemlessly into first

courses.sort()
# sorts list into alphabetical/numerical order

courses.sort(reverse=True)
# sorts into descing order

(min)  #  finds the minimum value
(max)  #  finds the max value
(sum)  #  totals all values

# dictionaries

student = {'name': 'John', 'age': 25, 'courses': ['Maths', 'Pysics']}

student.update({'name': 'Jane', 'age': 26, 'phone': 555-5555})  #updates and adds values/keys

del student['age'] #deletes keys

print(student.keys())
print(student.values())
print(student.items()) # prints both the keys and the values

for keys, values in student.items():
	print(keys, values)
