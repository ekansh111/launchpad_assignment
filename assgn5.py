inp = input("enter any input string")

i = len(inp) - 1
s = e = i + 1
res = ''

while i >= 0:
    if inp[i] == ' ':
        s = i + 1
        while s != e:
            res += inp[s]
            s += 1
        res += ' '
        e = i
    i -= 1
    s = 0
while s != e:
    res += inp[s]
    s += 1
print(res)