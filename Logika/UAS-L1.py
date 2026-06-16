arr = eval(input())
target = int(input())
n = len(arr) #<======Panjang array
found = False
for i in range(n):
    for j in range(i + 1, n): #loop 2x woi
        if arr[i] + arr[j] == target:
            print((arr[i], arr[j]))
            found = True
            break
    if found:
        break
if not found:
    print("No proceed")