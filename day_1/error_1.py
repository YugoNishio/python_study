# エラーへの対処(例外処理)
# try-except
# if_2.pyで整数以外の値を入力すると、ターミナル上で"ValueError"という例外が発生したと書かれている

try:
    if int(input("整数を入力してください-->")):  # 整数が入力されれば条件がTrue
        print("整数が入力されました!")
except ValueError: #数値として解釈できない場合にTrue
    print("整数が入力されませんでした!")
except ZeroDivisionError: #0で割ったときに出るエラー
    pass #例外をキャッチしても特に何も行わずにスルーしたいとき用
except: #その他のエラー
    print("予期していないエラーです!")
else: #例外が発生した場合はelse節は実行されない
    print("プログラムが正常に終了しました!")
finally: #例外の発生関係なく、常に実行される
    print("プログラムの実行、ありがとうございます!")
