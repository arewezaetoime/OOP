
class MyIterator:

    def __init__(self, start=0, end=20):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        self.current += 1

        return self.current - 1


my_iterator = MyIterator()

for i in my_iterator:
    print(i)