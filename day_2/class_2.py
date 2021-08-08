#コンストラクタ関数について
"""用語
コンストラクタ:オブジェクト(型)が扱うデータ(インスタンス)の初期化(今回は半径"radius"を使用するので必要)
インスタンス:対象のクラスのオブジェクト
インスタンス変数:あるインスタンスの固有の変数
インスタンス生成:クラスからインスタンスを作ること/オブジェクト生成とも呼ぶ
"""
#コンストラクタ関数の書き方
"""
class クラス名:
   def __init__(self,引数2,引数3): #コンストラクタ、別名初期化メソッド
       self.変数名1 = 引数2 #インスタンス変数の初期化
       self.変数名2 = 引数3
"""

class Circle: #オブジェクトの定義: コンストラクタを定義するために存在
    def __init__(self, radius): #コンストラクタ関数: インスタンス生成を行うと勝手に呼び出される特殊な存在
        #コンストラクタの第一引数selfはコンストラクタによって生成されるオブジェクト自身(今回は)
        self.radius = radius #インスタンス変数の初期化
    
    def area(self): #メソッド
        return radius * radius * 3.14 #circle.area()の値はコレ

radius = int(input("整数値を入力してください")) #変数radiusは引数に代入する用(関数と同じ様な感じ)
circle = Circle(radius) #インスタンスを生成: 変数名 = クラス名(引数) selfは要らない
print("円の半径:", radius)
print("円の面積:", circle.area()) #areaメソッドの呼び出し(Circleクラスにあるarea関数の戻り値を表示)

#インスタンス変数の性質について(class_3.pyに続く…)