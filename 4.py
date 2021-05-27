n=int(input('Enter the no of elements in Set1 -'))
m=int(input('Enter the no of elements in Set2 -'))
set1=[]
set2=[]
print ('Enter the elements of Set1 -')
for i in range(0,n):
    set1.append(input())
print ('Enter the elements of Set2 -')
for i in range(0,m):
    set2.append(input())
set1=set(set1)
set2=set(set2)
if set1==set2:
    print('They are subsets of each other')
elif set1==(set1|set2):
    print('Set2 is a subset of Set1')
elif set2==(set1|set2):
    print('Set1 is a subset of Set2')
else:
    print('They are not subsets of each other.')