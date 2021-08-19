#継承(メソッドのオーバーライド)
"""用語
オーバーライド:親クラスのメソッドを子クラスで再定義する行為(要はメソッドの上書き)
"""
class Planet: #スーパークラス(親クラス)
    def __init__(self, name = None, orbital_plane = 'same', orbit = 'circle'): #コンストラクタ 非入力時の設定完備
        self.name = name #インスタンス変数の初期化(引数の代入)
        self.orbital_plane = orbital_plane
        self.orbit = orbit

    @property #なんとなくプロパティのゲッター使用
    def common(self):
        return self.name, self.orbital_plane, self.orbit #複数返り値指定

    def common_info(self):
        print("名前:" + earth.common[0], "軌道面:" + earth.common[1], "軌道:" + earth.common[2])
        #複数戻り値が存在することでcommonメソッドが配列(リスト)の振る舞いをする

    def environment(self): #親クラス内でメソッドを用意してる
        environment = "----" #取りあえず何も書かない
        print(earth.common[0] + "って" + environment + "ですよね")
    
class Earth(Planet): #サブクラス(子クラス)
    def environment(self): #オーバーライドしたメソッド
        environment = "過ごしやすい" #ここでスーパークラスの上書き
        print(earth.common[0] + "って" + environment + "ですよね") #スーパークラスとの共通点はそのまま

earth = Earth('Earth') #子クラスをインスタンス化 引数を指定しなくても問題ないようにコンストラクタで設定してる
earth.common_info()
earth.environment() #オーバーライドしたメソッドの呼び出し

#コンストラクタのオーバーライド(class_10.pyに続く…)