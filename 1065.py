N = int(input())
cnt = 0

if N >= 100:
    for k in range(100, N+1):
        a = k // 100
        b = (k % 100) // 10
        c = k % 10
        if (a-b) == (b-c):
            cnt += 1
    print(cnt+99)
elif 1 <= N <= 99:
    print(N)