def bubble_sort(a):
    n = len(a)
    for j in range(1, n):
        for i in range(n - j):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
    return (a)

# print(bubble_sort([10, 3, 4, 2, 1]))
