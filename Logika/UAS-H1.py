CHARS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
def spiral(mat, n):
    out = []
    top = 0
    bot = n - 1
    left = 0
    right = n - 1
    while top <= bot and left <= right:
        for y in range(left, right + 1):
            out.append(mat[top][y])
        top += 1
        for z in range(top, bot + 1):
            out.append(mat[z][right])
        right -= 1
        if top <= bot:
            for y in range(right, left - 1, -1):
                out.append(mat[bot][y])
            bot -= 1
        if left <= right:
            for z in range(bot, top - 1, -1):
                out.append(mat[z][left])
            left += 1
    return out
def ubah(number):
    teks = ""
    for d in str(number):
        teks += CHARS[int(d)]

    if number >= 10: #s
        return "_" + teks + "_"
    else:
        return teks
def main():
    s = input().strip()
    if '-' in s:
        print("No proceed")
        return
    data = []
    for c in s:
        if c.isdigit():
            data.append(int(c))
        elif c in CHARS:
            data.append(CHARS.index(c))
        else:
            print("No proceed") 
            return
    if len(data) == 0: #ds
        print("No proceed")
        return
    n = len(data)
    matriks = []
    for z in range(n):
        line = []
        for y in range(n):
            line.append(data[z] * data[y])
        matriks.append(line)
    order = spiral(matriks, n)
    results = ""
    for x in order:
        results += ubah(x)
    print(results)
main()