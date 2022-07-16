a = int(input())
b = 1
cnt = 1
tmp = a
a -= 1

while a > 0 :
    b += 1
    a -= b
    if(a % b == 0):
        cnt += 1
        
print(cnt)