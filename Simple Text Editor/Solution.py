q = int(input())
s = ""
arx = []
for _ in range(q):
    z = input().split()
    match z[0]:
        case '1':
            arx.append(s)
            s += z[1]
        case '2':
            arx.append(s)
            s = s[:-int(z[1])]
        case '3':
            print(s[int(z[1]) - 1])
        case '4':
            s = arx.pop()