def linear(arr, target):
    size = len(arr)

    for i in range(size):
        if arr[i] == target:
            return i

    return -1

l = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

print(linear(l, target))
