
n=int(input("enter the number of elements in list"))
l = []
print("enter the values for list")
for i in range(0,n):
    k=input()
    l.append(k)
print(l)

print("list with values less than 5 ")
m = []
for r in l:
    p=int(r)
    if 5 > p:
        m.append(p)
print(m)
'''
l=[1,1,2,3,5,8,13,21,34,55,89]
m = []
for r in l:
    p=int(r)
    if 5 > p:
        m.append(p)
print(m)
'''
