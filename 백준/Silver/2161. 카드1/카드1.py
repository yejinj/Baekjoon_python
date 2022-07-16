n = int(input())
arr1 = [i for i in range(1, n + 1)]
arr2 = []

while len(arr1) != 1:
    arr2.append(arr1.pop(0))
    arr1.append(arr1.pop(0))

for i in arr2:
    print(i, end = " ")
    
print(arr1[0])