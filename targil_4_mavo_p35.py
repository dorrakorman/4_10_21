#targil 4 mavo amud 35

 i = 1
 bead = 0
 neged = 0
 nimna = 0
 while i <= 9:
     x = int(input('enter num='))
     if x ==1:
         bead = bead + 1
     if x ==2:
         neged = neged + 1
     if x ==3:
         nimna = nimna + 1

     if x ==4:
         print('veto', i)
         break
     i = i + 1
 print("bead=",bead,"neged=",neged,"nimna=",nimna)
