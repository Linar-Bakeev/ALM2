def intwo(n):
    if n < 1:
        return 0
    num = ""
    while n >= 1:
        num = str(int(n % 2)) + num
        n = n / 2
    return num


def main():
    global res, a, b, oper
    print("S0 | 000 Код операции = 0 ОП1 = 0 ОП2 = 0")

    input = open('input.txt', 'r')
    l = 0
    print("S1 | 000 Код операции = 0 ОП1 = 0 ОП2 = 0")

    line = input.read()
    input.close()
    print("S2 | 000 Код операции = 0 ОП1 = 0 ОП2 = 0")

    l = len(line)
    print("S3 | 000 Код операции = 0 ОП1 = 0 ОП2 = 0")

    if l != 18:
        print("001| Неправильная длина строки! l = ", l)
        exit()
    else:

        oper = int(line[0:2], base=2)
        a = int(line[2:10], base=2)
        b = int(line[10:18], base=2)
        print("S4 | 000 Код операции = ", intwo(oper), "=", oper, "ОП1 = ", intwo(a), "=", a, "ОП2 = ", intwo(b), "=",
              b)

    if oper == 0 or oper == 3:
        if oper == 0:
            res = a * b
            print("S5 | 000 Результат умножения = ", intwo(res), '=', res)
            if res > 255:
                print("010 | Переполнение разрядности!")
                exit()

        else:
            if (b != 0):
                res = a / b
                print("S6 | 000 Результат деления = ", intwo(res), '=', res)
            else:
                print("100 | Деление на 0!")
                exit()

    else:
        print("011 | Неверный код операции!")
        exit()
    # print(intwo(res))
    output = open('output.txt', 'w')
    output.write(intwo(res))
    output.close()
    print("S0 | 000 Код операции = ", intwo(oper), "=", oper, "ОП1 = ", intwo(a), "=", a, "ОП2 = ", intwo(b), "=", b,
          "Результат=", res)


main()