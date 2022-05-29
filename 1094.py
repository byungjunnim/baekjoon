X = int(input())
bin_num = []
while X // 2 > 1:
    bin_num.append(X % 2)
    X = X // 2
bin_num.append(X // 2)
bin_num.append(X % 2)

cnt = 0
for elem in bin_num:
    if elem == 1:
        cnt += 1

print(cnt) 
