#yield文：ジェネレータ関数の定義に使用
"""用語
ジェネレータ関数：イテレータを作成するための関数. イテレータを戻り値とする
ジェネレータ関数によって作成されたイテレータ(ジェネレータ関数の呼び出し)：「ジェネレータイテレータ」や「ジェネレータ」と呼ぶ
"""

#yield(イールド)
"""
関数の処理を一時停止(returnは処理を終了させる)
値を返す
"""
#使用用途
#あらかじめ繰り返す値を全て計算しておけないとき。(計算コストを節約)
#メモリの使用量を抑えたい時とも言える

#例(計算コスト)
def one_GB(): #ジェネレータ関数:繰り返し可能なオブジェクト range()も繰り返し可能なオブジェクト
    Cap = 1024 #1GB = 1024MB
    data = 230 #実行時に230MBのメモリを消費したとする
    RemCap = Cap - data #残りのタスク量
    yield data, RemCap #2つ以上の値を返す時はこの様に書く

    data = 370 #実行時に370MBのメモリを消費したとする
    RemCap = set_g[1] - data #残りのタスク量 #set_[1]は一つ前のRemCapの値
    yield data, RemCap

    data = 424
    RemCap = set_g[1] - data
    yield data, RemCap

iterator = one_GB() #ジェネレータ関数の呼び出し。戻り値はイテレータの為、変数iteratorはイテレータが入る
for _ in one_GB(): #one_GB()はジェネレータ関数の為、繰り返しが可能
    set_g = next(iterator) #next関数：イテレータの先頭要素を取得。要素は配列(リスト)の様に番号に振り分けられる。
    print("使用したデータ量は" + str(set_g[0]) + "[MB]です") #[0]はdata
    print("残りタスクは" + str(set_g[1]) + "[MB]です") #[1]はRemCap(RemainingCapacity)