# example
# class NameOfClass():
#     def __init__(self, param1, param2):
#         self.param1 = param1
#         self.param2 = param1

#     def some_method(self):
#         print(self.param1)


# class Dog():
#     # class object attribute
#     species = 'Mammal'

#     def __init__(self, breed, name, spots):
#         self.breed = breed
#         self.name = name
#         self.spots = spots

# Operations/Actions == Methods
#     def bark(self):
#         print('Woof! My name is {} '.format(self.name))


# my_dog = Dog('Lab', 'Rex', False)

# print(my_dog.breed)
# print(my_dog.spots)
# my_dog.bark()


# class Animal():
#     def __init__(self):
#         print('Animal created')

#     def who_am_i(self):
#         print('I am an animal')

#     def eat(self):
#         print('I am eating')


# class Dog(Animal):
#     def __init__(self):
#         Animal.__init__(self)
#         print('Dog created')


# my_dog = Dog()
# eating = my_dog.eat()
# eating


class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print('This book has been deleted.')


b = Book('American Gods', 'Neil Gaiman', 700)
