#まずは第一回勉強会の復習をしましょう.

#input()とprint()
num = int(input("整数を入力してください"))
char = input("文字を入力してください")
print(num, char + "　次はif文とtry-exceptです\n")

#if文と例外処理(try-except)
try:
    num = int(input("もう一度整数を入力してください"))
    if num > 10:
        print("10より大きい値です")
    elif num == 10:
        print("10が入力されました")
    else:
        print("10以下の値です")
except ValueError:
    print("整数が入力されませんでした")
except:
    pass
finally:
    print("\n")

#for
print("for文の内容です")
for i in range(10, 17):
    if i == 11:
        continue
    if i == 15:
        break
    print(i)

#while
print("\nwhile文の内容です")
value = 0
while True:
    print(value)
    value += 1
    if value == 3:
        break
else:
    print("ループ条件がFalseになったため、終了します")
print("ループ終了")