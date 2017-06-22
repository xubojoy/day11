#Author:xubojoy
def my_generator():
    print('inside-------')
    yield 'a'
    yield 'b'
    yield 'c'



for char in my_generator():
    print(char)




def counter_generator(low, high):
    while low <= high:
        yield low
        low += 1


for i in counter_generator(5, 10):
    print(i, end=' ')



s = sum(x*x for x in range(1, 10))
print(s)
