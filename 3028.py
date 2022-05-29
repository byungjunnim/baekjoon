cups = [1, 0 ,0]
mix = list(input())
for way in mix:
    if way == 'A':
        a = cups[0]
        b = cups[1]
        cups[0] = b
        cups[1] = a
    elif way == 'B':
        c = cups[1]
        d = cups[2]
        cups[1] = d
        cups[2] = c
    elif way == 'C':
        e = cups[0]
        f = cups[2]
        cups[0] = f
        cups[2] = e

for k in range(1, 4):
    if cups[k-1] != 0:
        print(k)

