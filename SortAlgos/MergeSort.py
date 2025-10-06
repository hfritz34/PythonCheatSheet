def merge(left, right):
    '''
    Merge takes in two SORTED arrays, left and right, and merges them together using two pointers, i and j
    Ex.
    left = [1,3,5] right = [2,4,6]
    merge(left,rigt)
    -> [1,2,3,4,5,6]
    '''
    i = j = 0
    res = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res.extend(left[i:])
    res.extend(right[j:])

    return res

def merge_sort(arr):
    if len(arr) <= 1:
        return arr


    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]


    left_sort = merge_sort(left)
    right_sort  = merge_sort(right)

    return merge(left_sort,right_sort)

print(merge_sort([43,20,4,1,9,19,32,23,34]))

