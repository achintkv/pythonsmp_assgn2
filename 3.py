n=int(input('Enter the no of elements -'))
lst=[]
print('Enter the elements -')
for i in range(0,n):
    m=int(input())
    if m not in lst:
        lst.append(m)
print (lst)