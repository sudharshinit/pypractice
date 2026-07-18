import math 
x=[]
y=[]
a=[2,3,4]
b=[0,2,2]
for i in range(0,len(a)-1):  
 m = math.gcd(a[i],a[i+1])  
 x.append(m)
print(x)
x.sort()
print("Sorted x:", x)
for i in range(len(b)) :
 k = x[b[i]]
 y.append(k) 
print(y)


