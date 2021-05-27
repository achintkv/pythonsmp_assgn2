lst = []

n = int(input('No of elements in the list : '))
print ('Enter the elements -')
for i in range(0,n):
    ele = int(input())
    lst.append(ele)

check = 0

for i in range(len(lst)):
    for j in range(len(lst)):
        if i!=j:
            if lst[i] == lst[j]:
                check =1

if(check==1):
    print('False')
else:
    print('True')