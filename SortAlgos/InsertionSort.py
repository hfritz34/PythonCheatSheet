'''
The mental model:

Left side = sorted, right side = unsorted
Pick the next unsorted element (moving left to right)
Slide it left until it finds its spot in the sorted section
Repeat until done
'''

 
def insertion_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr 

print(insertion_sort([3,2,5,1,7,4,9,2]))
