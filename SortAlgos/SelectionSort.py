def findSmallest(arr):

    smallest = arr[0]
    smallestIndex = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallestIndex = i 
    return smallestIndex


def selectionSort(arr):
    sortedList = []
    copiedArr = list(arr)
    for i in range(len(copiedArr)):
        smallest = findSmallest(copiedArr)
        sortedList.append(copiedArr.pop(smallest))
    return sortedList 


print(selectionSort([4,8,1,25,3,5,11,9]))
