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

class Earth:
    def __init__(self): #コンストラクタ
        self.__year = '16世紀' #インスタンスの初期化プライベート変数化しないと無限再帰処理に入る
        self.__established_theory = '天動説'

    @property
    def year(self): #プロパティ名を[name]とする
        pass #特にこの関数で実行する内容無し
    @year.getter
    def year(self): #メソッドを通して属性値を取得
        return self.__year #nameメソッドがインスタンス変数の値を持つことになる

    @property
    def established_theory(self):
        return self.__established_theory #プロパティとゲッターは一つにまとめられる
    
    @established_theory.setter
    def established_theory(self, change_theory): #メソッドを通して属性値を設定
        self.__established_theory = change_theory #ここでインスタンス変数に値設定

earth = Earth() #インスタンス生成
print(earth.year, earth.established_theory) #ゲッター呼び出し(プライベート変数だが通常のように呼び出せる)

"""ちなみに…
前回ではプライベート変数の呼び出しは [planet_e._Planet__name]のようにしてました.
planet_e.name = 'Mars' もちろんこの表記で書き換えは出来ない
planet_e._Planet__name = 'Mars' なおこの表記は直接インスタンス変数を参照しているため書き換えられる
"""

earth.established_theory = "地動説" #セッターの呼び出し
print(earth.year, earth.established_theory) #定説の改変完了…

#オブジェクト指向プログラミングと言えば"継承"(class_8.pyに続く…)