n=int(input("enter the number of elements in list"))
l = []
print("enter the values for list")
for i in range(0,n):
    k=input()
    l.append(k)
print(l)
k = int(input("enter the element you want to search"))


m = []
i=int(0)
for r in l:
    p=int(r)
    if k == p:
        m.append(i)
    i=i+1
print(m)

