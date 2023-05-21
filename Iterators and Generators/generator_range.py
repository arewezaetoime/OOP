def generate(start, end):
    for n in range(start, end + 1):
        yield n


print(list(generate(1, 10)))