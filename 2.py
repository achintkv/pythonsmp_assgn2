n=int(input('Enter the no of elements -'))
lst=[]
print('Enter the elements -')
for i in range(0,n):
    lst.append(input())
a=len(lst)
lst=set(lst)
b=len(lst)
if a==b:
    print('The elements are Unique')
else:
    print('The elements are not Unique')
