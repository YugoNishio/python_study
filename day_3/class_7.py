#property(property/getter/setter)
#pythonの組み込みのデコレータ関数
"""用語
プロパティ(property):属性への参照(アクセス)するときに使われる考え方
                     具体的にはクラス外部から直接参照せずにメソッドを通して属性値の取得・設定・削除をする時に使用
ゲッター(getter):属性値の取得をするメソッド
セッター(setter):属性値の設定をするメソッド
@~(デコレータ):クラス/関数に特殊な振る舞いをさせる機能(正体は関数を返す関数)
               今回はデコレータを利用した話なので[@property]となる(関数として実行する書き方もある)
"""

"""プロパティの書き方(デコレータを使うことでシンプルなコードに)
@property
def プロパティ名(self):
    pass
"""
"""ゲッターの書き方
@プロパティ名.getter
def プロパティ名(self):
    return self.変数名
"""
"""セッターの書き方
@プロパティ名.setter
def プロパティ名(self, value):
    self.変数名 = value #引数名は適当
"""

class Planet:
    def __init__(self): #コンストラクタ
        self.__name = 'Earth' #インスタンスの初期化
        #self.half_size = half_size
        self.__radius = 6371 #プライベート変数化しないと無限再帰処理に入る

    @property
    def name(self): #プロパティ名を[name]とする
        pass #特にこの関数で実行する内容無し
    @name.getter
    def name(self):
        return self.__name #nameメソッドがインスタンス変数の値を持つことになる

    @property
    def radius(self):
        return self.__radius #プロパティとゲッターは一つにまとめられる
    
    @radius.setter
    def radius(self, half_size):
        if half_size is not 6371: # != でも動作
            print("半径", half_size, "[km]ですか…それは現在の地球ではないですね!")

planet_e = Planet() #インスタンス生成
print(planet_e.name, planet_e.radius) #ゲッター呼び出し(プライベート変数だが通常のように呼び出せる)
#前回ではプライベート変数の呼び出しは [planet_e._Planet__name]のようにしてました.
#planet_e.name = 'Mars' もちろんこの表記で書き換えは出来ない
#planet_e._Planet__name = 'Mars' なおこの表記は直接インスタンス変数を参照しているため書き換えられる

planet_e.radius = 100 #セッターの呼び出し