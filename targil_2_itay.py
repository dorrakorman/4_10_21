#targil 2 homework
 i = 1
 sum = 0
 num = 0
 while i <= 9:
     x = int(input('enter num='))
     if x == 0:
         break
     if x > 77:
         sum = sum + x
         num = num + 1
     i = i + 1
 print('sum=',sum,'num=',num)