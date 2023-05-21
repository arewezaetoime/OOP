def generator_string_func(some_string):
    for char in some_string:
        yield char
        # return char ---> for example on what returns the return statement and how the program ends on with the
        # first iteration compared to yield statement where the program ends on when there are no more characters to
        # iterate over


my_string = 'Lud-poludql'

for next_element in generator_string_func(my_string):
    print(next_element, end=' ')