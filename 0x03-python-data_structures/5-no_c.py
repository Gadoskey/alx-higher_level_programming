#!/usr/bin/python3

def no_c(my_string):
    small = 'c'
    big = 'C'
    new_string = ''
    for i in my_string:
        if i != small and i != big:
            new_string  += i
    return(new_string)
