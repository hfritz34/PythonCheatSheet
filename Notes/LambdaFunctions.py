add_1 = lambda x: x + 1 
print(add_1(1))

def add_2(a):
    return a + 2 

print(add_2(1))

values = [(1, 'b', "hello"), (2,'a', "world"), (3, 'c', "ok")]

sorted_values = sorted(values, key = lambda x: x[1])

print(sorted_values)

    


