#関数定義の基本
#def 関数名(引数):
#   実行する内容
#   return 返り値 #場合によっては必要ない

#関数実行の基本
#関数名(引数)

#返り値を持つ関数の例(入力された値を3倍にして出力)
def calculation(value): #関数名:Calculation 引数:value
    answer = value * 3
    return answer #answerの値を返り値とする
#↓実行(c言語でいうmain文)
fx = calculation(float(input("値を入力してください-->"))) #value=float(input("値を入力してください-->"))   変数fxに返り値のanswerが入る
print("3倍した値は",fx,"です")


#返り値を持たない関数の例(入力した値の絶対値を出力)
def functionAbs(num): #引数をnumとする。num = float(input("値を入力してください-->"))
    if num < 0:
        num = -num #他にも符号反転の方法あり
    print("絶対値は",num,"です") #print関数に返り値は持たない(C言語と同じ)
#↓実行(c言語でいうmain文)
functionAbs(float(input("値を入力してください-->"))) #関数を実行


#引数を持たない関数の例(定型的な命令を実行する場合)
def Auto():
    Auto_num = float(input("値を入力してください-->"))
    Auto_ans = Auto_num * 6
    print("6倍した値は",Auto_ans,"です")
#↓実行(c言語でいうmain文)
Auto() #引数を持たないのでこのような呼び出し方になる

#ローカル変数とグローバル変数(function_2.pyに続く…)