def reverse_text(some_string):
    for c in reversed(some_string):
        yield c


for char in reverse_text('step'):
    print(char, end='')