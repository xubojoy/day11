#Author:xubojoy
fahrenheit = 0
while fahrenheit <= 250:
    celsius = (fahrenheit - 32) / 1.8
    print('%5d %7.2f' % (fahrenheit,celsius))  #等价于print('{:5d} {:7.2f}'.format(fahrenheit, celsius))  #%5d 或者 {:5d} 默认保留5个位置的整数   %7.2f或者{:7.2f} 默认占7个单位的保留两位小数的浮点型
    fahrenheit = fahrenheit + 25

