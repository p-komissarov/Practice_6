n, m = map(int, input().strip().split("x"))
k = int(input().strip())

if k > 0 and k < n * m:
    if k % m == 0 or k % n == 0:
        print("Успешно")
    else:
        print("Неосуществимо")
else:
    print("Неосуществимо")