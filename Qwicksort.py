def QS(M):
    sorted = my_qwicksort(M)


def my_qwicksort(M, key=0):
    if len(M) <= 1:
        return M

    Left_M = []
    Right_M = []
    Middle_M = []

    partition = M[key]
    for x in M:
        if x < partition:
            Left_M.append(x)
        elif x == partition:
            Middle_M.append(x)
        else:
            Right_M.append(x)

    return my_qwicksort(Left_M) + Middle_M + my_qwicksort(Right_M)


print("my_qwicksort done")
