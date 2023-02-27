def draw(size):
    our_figure = []

    for line in range(size):
        space_data = size - line - 1
        start_data = line + 1
        our_figure.append(' ' * space_data + '* ' * start_data)

    for line in range(size - 2, - 1, -1):
        space_data = size - line - 1
        start_data = line + 1
        our_figure.append(' ' * space_data + '* ' * start_data)

    return '\n'.join(our_figure)

print(draw(int(input())))

