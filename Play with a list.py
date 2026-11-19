L = [4, 5, 1, 2, 9, 7, 10, 8]
count = 0
for i in L:
    count += 1
    
avg = count/len(L)
print("Sum: ", count)
print("average: ", avg)

L.sort()
print("Smallest element: ", L[0])
print("largest element: ", L[-1])