# tuples are immutible (can't be changed)

tuple_1 = ('history', 'maths', 'bio')
tuple_2 = tuple_1

tuple_1[0] = 'art'

print(tuple_1)
print(tuple_2)
# code won't run because its trying to make a change to a tuple