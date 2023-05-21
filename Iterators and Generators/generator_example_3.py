def yield_example():
    num = 1

    print("This is returned first")
    yield num
    num += 1

    print("This is returned first")
    yield num
    num += 1

    print("This is returned first")
    yield num


for i in yield_example():
    print(i)