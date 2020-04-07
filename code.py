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
