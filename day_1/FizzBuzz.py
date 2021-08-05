try:
    num = int(input("整数を入力してください"))
    for value in range(1,num + 1):
        if value >= 20:
            print("20に到達したため,")
            break
        elif value % 15 == 0:
            print("FizzBuzz")
        elif value % 3 == 0:
            print("Fizz")
        elif value % 5 == 0:
            print("Buzz")
        elif value % 4 == 0:
            continue
        else:
            print(value)
except ValueError:
    print("整数が入力されませんでした")
except:
    print("正常にプログラムが実行されませんでした")
finally:
    print("プログラムを終了します")