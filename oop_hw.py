# import math


# class Line():
#     def __init__(self, coor1, coor2):
#         self.coor1 = coor1
#         self.coor2 = coor2

#     def distance(self):
#         x1, y1 = self.coor1
#         x2, y2 = self.coor2
#         return math.sqrt((x2-x1)**2 + (y2-y1)**2)

#     def slope(self):
#         x1, y1 = self.coor1
#         x2, y2 = self.coor2
#         return (y2-y1) / (x2-x1)


# c1 = (3, 2)
# c2 = (8, 10)

# myline = Line(c1, c2)

# print(myline.distance())
# print(myline.slope())


# class Cylinder:

#     pi = 3.14

#     def __init__(self, height=1, radius=1):
#         self.height = height
#         self.radius = radius

#     def volume(self):
#         return self.pi * self.height * (self.radius)**2

#     def surface_area(self):
#         top = self.pi * (self.radius**2)
#         return (2 * top) + (2*self.pi*self.radius*self.height)


# mycyl = Cylinder(2, 3)
# print(mycyl.volume())
# print(mycyl.surface_area())


# Challenges

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner: {self.owner}\nAccount balance: ${self.balance}'

    def deposit(self, dep_amt):
        self.balance = self.balance + dep_amt
        print(f'Added {dep_amt} to account. You now have {self.balance} in account.')

    def withdrawal(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance = self.balance - wd_amt
            print(f'Withdrawal accepted. You have {self.balance} left in account.')

        else:
            print('Insufficiant funds.')


a = Account('Jose', 500)

print(a)
# a.deposit(200)
# a.withdrawal(600)


