#イテレータとジェネレータ
"""用語
yield：ジェネレータ関数を実装する際に使用
ジェネレータ関数(generator function)：ジェネレータイテレータ(別名ジェネレータ(ネット特有の表記ゆれ))というオブジェクトを返す関数
ジェネレータイテレータ(ジェネレータ)：ジェネレータ関数で生成されるオブジェクト
イテレータ：配列やそれに類似するデータ構造の各要素に対する繰り返し処理の抽象化 range()とか
            (データの流れを表現するオブジェクト)
※注意：ジェネレータイテレータはイテレータの一種
"""

#ジェネレータ関数の使いどころ
#あらかじめ繰り返す値を全て計算しておけないとき。(計算コストを節約)
#メモリの使用量を抑えたい時とも言える

#例(計算コスト)
def one_GB(): #ジェネレータ関数
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

generator = one_GB() #ジェネレータ関数の呼び出し。戻り値はジェネレータイテレータオブジェクト
for _ in one_GB(): #one_GB()はジェネレータ関数の為、繰り返しが可能
    set_g = next(generator) #next関数：ジェネレータイテレータ(イテレータ)の先頭要素を取得。要素は配列(リスト)の様に番号に振り分けられる。
    print("使用したデータ量は" + str(set_g[0]) + "[MB]です") #[0]はdata
    print("残りタスクは" + str(set_g[1]) + "[MB]です") #[1]はRemCap(RemainingCapacity)