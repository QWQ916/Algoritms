a = [0, 2, 13, 17, 33, 40, 54, 66, 70, 75, 92, 101, 112, 132, 133, 139, 150]
n, x = len(a), 17
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
