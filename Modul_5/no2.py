#No2

a = [3, 5, 7, 17, 23, 47, 68, 101]
b = [2, 4, 8, 22, 27, 31, 37, 41]

def test1(a,b):
    c = a + b
    for i in range(1,len(c)):
        nilai = c[i]
        pos = i
        while pos >0 and nilai<c[pos - 1]:
            c[pos]= c[pos-1]
            pos -= 1
        c[pos] = nilai
    print(c)

def test2(a,b):
    ad0 = len(a)
    ad1 = len(b)
    x= 0
    y=0
    c = []
    while x < ad0 and y < ad1:
        if a[x]<b[y]:
            c.append(a[x])
            x += 1
        else:
            c.append(b[y])
            y += 1
    while x<ad0:
        c.append(a[x])
        x += 1
    while y<ad1:
        c.append(b[y])
        y += 1
    return c
