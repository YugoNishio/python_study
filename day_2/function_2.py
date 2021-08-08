#グローバル変数とローカル変数
"""
関数外で代入された変数は全てグローバル変数
関数内で代入された変数は全てローカル変数
"""

#function_1.pyのコード
def calculation(value): #value：ローカル変数
    answer = 3 * value #answer：ローカル変数
    return answer #answerの値を返り値とする
fx = calculation(float(input("値を入力してください-->"))) #fx：グローバル変数
print("3倍した値は",fx,"です")

#ローカル変数は関数内でしか参照できない
answer = 10 #Pythonはローカル変数と同じ名前の変数をグローバル変数として定義できる
print("3倍した値は",fx,"です") #関数の実行結果が反映されている

#グローバル変数はどんな場合でも参照できる(変数名の衝突が起きる可能性)
fx = 10 #fxはグローバル変数の為、書き換えることが可能
print("3倍した値は",fx,"です") #必ず10が出力(関数実行後にfxに代入しているため)

#グローバル宣言について(function_3.pyに続く…)