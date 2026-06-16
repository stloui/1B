n = input().strip()
arr_line = input().split()

valid = True

if not n.lstrip('-').isdigit():
    valid = False
else:
    n = int(n)
    if n <= 0 or len(arr_line) != n:
        valid = False

arr = []
if valid:
    for x in arr_line:
        if not x.lstrip('-').isdigit():
            valid = False
            break
        arr.append(int(x))

if not valid:
    print("No Proceed")
else:
    m = 0
    for i in range(n):
        for j in range(i, n):
            nilai = arr[i] // arr[j]
            if len(str(nilai)) > m:
                m = len(str(nilai))

    for i in range(n):
        print(" " * (i * (m + 1)), end="")
        for j in range(i, n):
            print(str(arr[i] // arr[j]).rjust(m), end="")
            if j != n - 1:
                print(" ", end="")
        print()