n=int(input('Enter the no of elements in Tuple1 -'))
m=int(input('Enter the no of elements in Tuple2 -'))
tuple1=[]
tuple2=[]
lst=[]
print ('Enter the elements of Tuple1 -')
for i in range(0,n):
    tuple1.append(int(input()))
print('tuple1 =',tuple(tuple1))
print ('Enter the elements of Tuple2 -')
for i in range(0,m):
    tuple2.append(int(input()))
print ('tuple2 =',tuple(tuple2))
tuple1=tuple(tuple1)
tuple2=tuple(tuple2)
if m>n:
    c=n
else:
    c=m
for i in range(0,c):
    lst.append(tuple1[i]+tuple2[i])
if m>n:
    for i in range(c,m):
        lst.append(tuple2[i])
else:
    for i in range(c,n):
        lst.append(tuple1[i])
lst=tuple(lst)
print ('The Required Tuple is -',lst)