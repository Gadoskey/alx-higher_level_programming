def print_list_integer(my_list=[]):
    for i in my_list:
        print(i)

print_list_integer = __import__('test-0-print_list_integer').print_list_integer
my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

