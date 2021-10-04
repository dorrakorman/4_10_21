#targil 3 homework - from itay
a = 1
b = 1
c = 1
d = 1
e = 1
f = 1
g = 1
h = 1
while a != 0:
    x = int(input('enter num='))
    a = x % 2
while b != 0:
    x = int(input('enter num='))
    b = x % 3
while c != 0:
    x = int(input('enter num='))
    c = x % 4
while d != 0:
    x = int(input('enter num='))
    d = x % 5
while e != 0:
    x = int(input('enter num='))
    e = x % 6
while f != 0:
    x = int(input('enter num='))
    f = x % 7
while g != 0:
    x = int(input('enter num='))
    g = x % 8
while h != 0:
    x = int(input('enter num='))
    h = x % 9
    if x == 10:
        break
print(x)
print('finish')
