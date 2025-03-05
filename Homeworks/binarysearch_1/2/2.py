n, x = list(map(int, input().split()))
a = list(map(int, input().split()))
l, r = 0, n - 1
i, f = -1, 10**10
while r >= l:
    m = (r + l) // 2
    if a[m] < x:
        p = abs(x - a[m])
        if p < f:
            i, f = m, p
        elif p == f:
            i = min(i, m)
        l = m + 1
    elif a[m] > x:
        p = abs(x - a[m])
        if p < f:
            i, f = m, p
        elif p == f:
            i = min(i, m)
        r = m - 1
    else:
        i = m
        break
print(i)
