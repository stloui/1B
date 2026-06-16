num = input().strip()
valid = num.isdigit() and int(num) >= 0
if valid:
    n = int(num)
    arr_input = input().strip().split()
    if len(arr_input) != n:
        valid = False
    else:
        arr = []
        for x in arr_input:
            if not x.isdigit():
                valid = False
            arr.append(int(x))
if not valid:
    print("No Proceed")
else:
    m = 0
    for i in range(n):
        for j in range(i, n):
            value = arr[i] - arr[j]
            length = len(str(value))
            if length > m:
                m = length
    for i in range(n):
        print(" " * (i * (m + 1)), end="")
        for j in range(i, n):
            print(str(arr[i] - arr[j]).rjust(m), end="")
            if j != n - 1:
                print(" ", end="")
        print()

