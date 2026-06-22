def insertion(arr):
    n = len(arr)

    for current in range(1, n):
        current_card = arr[current]
        correct_position = current - 1

        while correct_position >= 0 and arr[correct_position] > current_card:
            arr[correct_position + 1] = arr[correct_position]
            correct_position -= 1

        arr[correct_position + 1] = current_card

    return arr

lst = [5, 2, 4, 6, 1, 3]
print(insertion(lst))
