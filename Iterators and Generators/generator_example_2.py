def first_n(number):
    num = 0

    while num < number:
        yield num
        num += 1


# example 1
sum_first_n_func = sum(first_n(5))
print(sum_first_n_func)

# example 2
for n in first_n(5):
    print(n)