n = int(input())
arr = list(map(int, input().split()))
key = int(input())

arr.append(0)
arr.sort()

ans = 0
for i in range(len(arr)-1) :
    if arr[i] == key or arr[i+1] == key:
        ans = 0
        break
    elif arr[i] < key and key < arr[i+1]:
        ans = (key - arr[i]) * (arr[i+1] - key) - 1
        break

print(ans)