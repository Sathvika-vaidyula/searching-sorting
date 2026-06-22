def bubble(arr):
    size = len(arr)

    for i in range(size):
        for j in range(size - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

lst = [5, 4, 3, 2, 1]
print(bubble(lst))
