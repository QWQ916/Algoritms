n = int(input())
a = list(map(int, input().split()))
l, r = 0, n - 1
i = -1
while r >= l:
    m = (r + l) // 2
    if m == 0:
        l = 1
    elif m == n - 1:
        r = m - 1
    else:
        if a[m] > a[m + 1] and a[m] > a[m - 1]:
            i = m
            break
        elif a[m] > a[m - 1]:
            l = m + 1
        else:
            r = m - 1
print(i)
