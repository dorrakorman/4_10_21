#targil 3 mavo amud 35
d = -5
i = 1
c = 40
while i <= 9:
    x = int(input('enter number ='))
    if x < d or x > c:
        print('not valid ', x)
        break
    i = i + 1
print('valid process', x)    