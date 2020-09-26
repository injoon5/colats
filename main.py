num = int(input('수는???'))
numnum = 1

while num>1:
    if(num%2==1):
      num = num*3+1
      print(num)
      print()
      numnum = numnum+1
    else:
        num = num/2
        print(num)
        print()
        numnum = numnum+1
print(numnum)
        
