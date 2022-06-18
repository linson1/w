

while True:
    number = input("请输入数字：")

    keyboard = {
        "0": " ",
        "1": " ",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    if number.isdigit():
        def a(number):  # a从输入中取值
            if not number:
                return []
            res = []
            if len(number) == 0:
                return []
            if len(number) == 1:
                return keyboard[number]

            result = a(number[:-1])
            for i in result:
                for j in keyboard[number[-1]]:
                    res.append((i + j))
            return res
        b = a(number)
        n = 0
        for k in b:
            print(k, end="\t")
            n = n + 1
            if n == 5:
                print()
                n = 0
        y_n = input("是否继续y/n：")
        if y_n == "y" or y_n == "Y":
            continue
        elif y_n == "n" or y_n == "N":
            break

    else:
        print("请确保输入的是数字")
        break
