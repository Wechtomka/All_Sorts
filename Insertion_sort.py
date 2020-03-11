def insert_sort(a):
    print("insert_sort is import")

    n = len(a)
    for i in range(1, n):
        key = i  # номер элемента для которо гоищем место в отсортированном массиве
        while key > 0 and a[key - 1] > a[key]:
            a[key], a[key - 1] = a[key - 1], a[key]
            key -= 1
    return (a)
