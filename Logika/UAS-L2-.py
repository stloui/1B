arr_input = input()
arr_str = arr_input[1:-1].split(',')
arr = []
for x in arr_str:
    arr.append(int(x))
target = int(input())
n = len(arr)
found = False
for i in range(n):
    for j in range(i + 1, n):
        if abs(arr[i] - arr[j]) == target:
            print((arr[i], arr[j]))
            found = True
            break
    if found:
        break
if not found:
    print("No Proceed")