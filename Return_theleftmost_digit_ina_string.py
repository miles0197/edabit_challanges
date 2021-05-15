def left_digit(num):
    num = str(num)
    for i in num:
        if i.isdigit():
          return int(i)
        
			
print(left_digit(5555))
print(left_digit('ajdkasdkjasd51231'))
