# import modules
# index = modules.find_index(courses, 'Maths')

# Quicker way:
# import modules as m
# index = m.find_index(courses, '')

# Even quicker (ie less typing):
from modules import find_index, test

courses = ['History', 'Maths', 'Physics', 'Compsci']

index = find_index(courses, 'Art')

print(index)
print(test)

# if module has been moved to another folder you can add it manually:
# import sys
# sys.path.ammend(/users/havelock/desktop/module) (as an example)

# to create system path on windows:
# right click on computer/this PC and select properties
# go to advanced system settings > enviromental variables > New...
