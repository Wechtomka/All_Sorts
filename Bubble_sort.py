def bubble_sort(a):
    n= len(a)
    for j in range(n - 1):
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
    return (a)