n = int(input())
p1 = 100
p2 = 100
for tc in range(1, n+1):
    a, b = map(int, input().split())
    if a > b:
        p2 -= a
    elif a < b:
        p1 -= b

print(p1)
print(p2)
