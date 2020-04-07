# be descriptive with titles, use underscores when using multiple words
# ie my_message not my message
# tripple " when going onto multiple lines

greeting = 'Hello'
name = 'Michael'

# message = greeting + ', ' + name
message = '{}, {}. Welcome!'. format(greeting, name)
# message = f'{greeting}, {name}. Welcome!'

print(message)
