# li = [9, 1, 4, 3, 7, 2, 6, 8, 5]

# s_li = sorted(li, reverse=True)

# print('Sorted Variable:', s_li)

# li.sort()

# print('Original:', li)

# tup = {2, 6, 4, 3, 8, 5, 1, 9, 7}
# s_tup = sorted(tup)
# print('Tuple:', s_tup)

# di = {'nane': 'Corey', 'job': 'programmer', 'age': None, 'os': 'Mac'}
# s_di = sorted(di)
# print(s_di)


# li = [-6, -5, -4, 1, 2, 3]
# s_li = sorted(li, key=abs)
# print(s_li)


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)


e1 = Employee('Carl', 37, 7000)
e2 = Employee('Sarah', 29, 8000)
e3 = Employee('Susan', 43, 9000)

employees = [e1, e2, e3]


def e_sort(emp):
    return emp.name


s_employees = sorted(employees, key=e_sort)

print(s_employees)

