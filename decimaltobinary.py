#For each digit from right to left:
    #peel off the right digit
    #multiple it by 2 to some power
    #add that to the running decNum total
    #binNum //= 10

#BINARY TO DECIMAL CONVERSION

#def binarytodecimal(binnum):
    #decnum = 0
    #power = 0
    #while binnum > 0:
    #    decnum = decnum + 2 ** power * (binnum%10)
   #     binnum = binnum// 10
  #      power += 1
 #   return decnum

#print(str(bintodec(100001010)))


#DECIMAL TO BINARY CONVERSION

#CONSTANT CONVERSION

def convert(fromNum, fromBase, toBase):
    toNum = 0
    power = 0
    while fromNum > 0:
        toNum += fromBase ** power * (fromNum % toBase)
        fromNum //= toBase
        power += 1
    return toNum

print(str(convert(0101010101,2,10)))

print(str(convert(20020,10,2)))
