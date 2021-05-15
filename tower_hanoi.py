def towerhanoi(n,start,destination,spare):
    global count

    if n > 0:
        towerhanoi(n-1,start,spare,destination)
        destination.append(start.pop())
        count = count + 1

        towerhanoi(n-1,spare,destination,start)

#initiate call from start A to destination C 
numbersteps = []
for i in range(1,10):
    A = list(range(i,0,-1))
    B = []
    C = []
    count = 0
    towerhanoi(i,A,B,C)
    numbersteps.append(count)


print(numbersteps)
    
        
