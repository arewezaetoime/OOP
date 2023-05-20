from time import thread_time

t = thread_time()
my_list = [1, 2, 3, 4, 5, 6]

my_iterator = iter(my_list)

for _ in range(1_0_0):

    try:
        print(next(my_iterator))
    except StopIteration:
        print('Idi nahui blyat')
        break

print(t)