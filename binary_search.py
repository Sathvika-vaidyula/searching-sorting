def binary(arr, target):
    size = len(arr)
    start = 0
    end = size - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            start = mid + 1

        else:
            end = mid - 1

    return -1


sorted_list = [1, 2, 3, 4]
target = 3

print(binary(sorted_list, target))
