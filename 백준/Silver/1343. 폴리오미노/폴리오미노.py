import array

arr = input()

arr = arr.replace("XXXX", "AAAA")
arr = arr.replace("XX", "BB")

if 'X' in arr:
    print(-1)
    
else:
    print(arr)