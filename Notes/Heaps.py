import heapq
myList = [9,5,4,1,3,2]
heapq.heapify(myList)
print(myList)
print(myList[0]) #should always be smallest number in the list, python heaps are min heaps by default

