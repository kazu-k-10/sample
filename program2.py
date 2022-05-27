for num in range(1, 101):
    string = ''

    # ここから記述
    if num % 15 == 0:       # num が15の倍数の時
        string = "FizzBizz"
        
    elif num % 3 == 0:     # num が3の倍数の時
        string = "Fizz"
        
    elif num % 5 == 0:     # num が5の倍数の時
        string = "Bizz"

    else:                  # num がそれ以外の数字の時
        string = num
    # ここまで記述

    print(string)
