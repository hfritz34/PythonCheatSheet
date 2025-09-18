#Sublists aka slicing in python
#Baklava

arr = [1,2,3,4,5,6]

print(arr[1:3]) #prints 2, 3. So we include right element, leave left element out

print(arr[::-1]) #prints list backwards, so [6,5,4,3,2,1]

#You can slice strings in a similar way
s = "abcdef"

print(s[0:3])

#Remeber though that strings are immutable in python
s[0] ="A"

#Unpacking in python

a, b, c = [1,2,3]

print(a)
print(b)
print(c)


#For loops in python
for i in range(len(arr)):
    print(i)

#Just value
for n in arr:
    print(n)

#Index and value
for i,n in enumerate(arr):
    print(i,n)


