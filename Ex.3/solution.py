import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

if a != 0:
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = int((-b + D ** 0.5) / (2 * a))
        x2 = int((-b - D ** 0.5) / (2 * a))
        print (x1)
        print (x2)
    elif D == 0:
        x1 = x2 = int(-b / (2 * a))
        print(x1)
        print(x2)
    else:
        print("Ошибка, введите другие данные!")
else:
    print("Ошибка, введите другие данные!")