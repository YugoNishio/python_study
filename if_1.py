#if文の基本

#if 条件式1:
#   条件式1がTrueのときに実行する内容
#elif 条件式2:
#   条件式1がFalseかつ条件式2がTrueのときに実行する内容
#else:
#   すべての条件式がFalseのときに行う処理

#例
con = int(input("整数値を入力してください-->")) #con(conditions)
if (con > 8) and (con != 13):
    print("その値は8より大きいですね")
elif con == 13:
    print("私の誕生日の日ですね")
else:
    print("8以下の値です")

#条件について(if_2.pyに続く…)