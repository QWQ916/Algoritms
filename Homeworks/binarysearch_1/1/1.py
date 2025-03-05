n, x = list(map(int, input().split()))
a = list(map(int, input().split()))
l, r = 0, n - 1
i = -1
if x <= a[r]:
    while r >= l:
        m = (r + l) // 2
        if a[m] < x:
            l = m + 1
        elif a[m] > x:
            i = m
            r = m - 1
        else:
            i = m
            break
print(i)
