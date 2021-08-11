#classについて
"""用語
クラス:オブジェクトを定義する(どんなオブジェクトなのかの説明)
メソッド:クラス内にある関数
オブジェクト:変数の一種、様々な値・処理を一括りしたもの、大抵クラスが元
オブジェクトの生成:クラスからオブジェクトを作ること/インスタンス生成とも呼ぶ(class_2.py)
"""

class Planet: #オブジェクトの定義 普通クラス名の先頭は大文字
    def earth(self): #メソッド 最低1つ引数が必要な為、第一引数はself(慣例)
        print("地球は過ごしやすい") #humanメソッドの実行内容
        self.mars('寒すぎる') #marsメソッドの呼び出し 同じオブジェクト(planet)内なのでself(第一引数の利用)

    def mars(self, message): #メソッド
        print('火星は' + message) #引数を出力 ""でも''でも文字列と認識されるようです

    def venus(self): #venusは呼び出されていないので実行されない.試しに呼び出してみましょう
        print("金星は暑すぎる")

planet = Planet() #オブジェクトの生成(今回のオブジェクトはspace) オブジェクト名 = クラス名()
planet.earth() #earthメソッドの呼び出し(実行) オブジェクト名.メソッド名()

#コンストラクタ関数について(class_2.pyに続く…)