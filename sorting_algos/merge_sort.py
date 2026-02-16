# 42 37 53 17

# split it in half
# 42 37 | 53 17

# Look at left side of list
# 42 37

# Split that
# 42 | 37

# A list with only 1 item will be sorted by default.
# 37 42

# Same for the right side of the list

# right side of original list
# 53 17

# divide the list in half
# 53 | 17

# merge the lists in sorted order
# 17 53

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    sorted_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list
