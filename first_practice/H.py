int1 = int(input())
int2 = int(input())
k1 = int(input())
k2 = int(input())
min1 = k1 + int1*(k1-1) 
max1 = k1 + int1*(k1+1) 
min2 = k2 + int2*(k2-1) 
max2 = k2 + int2*(k2+1) 
if min1 > min2 :              
    min = min1
else :
    min = min2
if max1 > max2 :              
    max = max2
else :                        
    max = max1
if min > max :      
    print(-1)
else :
    print(min , max)