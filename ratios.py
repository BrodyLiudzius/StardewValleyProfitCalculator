import sys

arr = sys.argv[1:]

for i in range(len(arr)):
    arr[i] = float(arr[i])

arr.sort()
min = arr[0]

for i in range(len(arr)):
    arr[i] /= min

print(arr)