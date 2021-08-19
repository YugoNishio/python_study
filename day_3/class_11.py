#ポリモフィズム
"""用語
ポリモフィズム:
"""
class Earth(object): #[object]はスーパークラスだと分かりやすいように置いてる(無くても良い)
    def __init__(self, situation = None): #コンストラクタ
        self.situation = situation #インスタンス変数の初期化(共通した処理はスーパークラスに任せる)

    def yabai(self): #サブクラスでこの名前を使用しているから分かりやすいように入れておく
        pass

    def hero(self):
        print("私が来た!!") #※ヒ〇アカ

class GlobalWarming(Earth): #サブクラス
    def yabai(self): #ヤバい内容の定義
        print("現在 " + self.situation) #スーパークラスのインスタンス変数値の受取
        print("地球寒冷化作戦を実行します") #※ガ〇ダム

class HugeMeteorite(Earth): #サブクラス
    def yabai(self): #ヤバい内容の定義
        print("現在 " + self.situation)
        print("どなたか石ころ一つ押し返してください") #※ガ〇ダム

earth = GlobalWarming("地球温暖化") #インスタンス生成 引数の処理(インスタンス変数の初期化)はスーパークラスで行う
earth.yabai() #地球温暖化はヤバい
earth = HugeMeteorite("巨大隕石")
earth.yabai() #隕石落下もヤバい
earth.hero() #この例は継承のシステムを利用しているのでスーパークラスのメソッドも実行できる