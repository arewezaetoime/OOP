class Range:
    def __init__(self, start: int, end: int) -> None:
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration

        result = self.current
        self.current += 1
        return result


for i in Range(1, 11):
    print(i)
