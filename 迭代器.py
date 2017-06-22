#Author:xubojoy
class Counter(object):
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        #返回下一个值直到当前值大于 high
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

c = Counter(5, 10)

for i in c:
    print(i, end=' ')

print('-'*20)
c = Counter(5, 10)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))


c = Counter(5, 10)
iterator = iter(c)
while True:
    try:
        x = iterator.__next__()
        print(x, end=' ')
    except StopIteration as e:
        break

