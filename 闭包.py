#Author:xubojoy
def add_number(num):
    def adder(number):
        print(num, number)
        return num + number
    return adder



a = add_number(20)
print(a(21))