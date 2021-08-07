#グローバル宣言
#関数内の変数をグローバル変数として扱いたい場合に使用
#ローカル変数は関数内で完結するため、関数ごとにグローバル宣言をする必要がある

#例(関数同士で値をやり取りする)
def FizzBuzz():
    global count #グローバル宣言
    if count % 15 == 0:
        print("FizzBuzz")
    elif count % 3 == 0:
        print("Fizz")
    elif count % 5 == 0:
        print("Buzz")
    else:
        print(count)

def loop():
    global value, count #countのグローバル宣言を行わないとFizzBuzzに値が引き継がれない
    for count in range(1, value + 1): #(1, value + 1)はcountに都合の良い値が入るようにつじつま合わせ
        FizzBuzz() #FizzBuzz()内でcountをグローバル宣言しているためcountの値を引き継げられる

def Input():
    global value #グローバル宣言
    value = int(input("整数値を入力してください\n入力した値までの判定を行います-->"))
    loop() #loop()でもvalueはグローバル宣言をしているため値を引き継げられる

Input() #実行

#関数の処理を一時停止させるもの"yeild"(function_4.pyに続く…)