ele = int(input())
n=int(input())
arr = []
for i in range(0, ele):
    arr.append(int(input()))
s=0
for i in range(arr[0],arr[n]):
    s=s+i
print (s)
