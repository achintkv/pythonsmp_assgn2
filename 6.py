def fn(tp):
    final_int = int(''.join(map(str,tp)))
    return final_int
tp=[]
n=int(input('Enter the no of elements-'))
print('Enter the elements-')
for i in range(0,n):
    tp.append(input())
tp=tuple(tp)
   
print(fn(tp))
