n=int(input("enter the number of elements in list"))
l = []
m = []
print("enter the  list")
for i in range(0,n):
    k=input()
    l.append(k)
print(l)

for i in l:
    if i not in m:
        m.append(i)
print(m)
