import random

count = 0
my_list = []  # empty list
while count < 10:
    my_list += [random.randint(1, 100)]  # conc of lists
    count += 1
print(my_list)

print('The smallest element of our list is:', min(my_list))
