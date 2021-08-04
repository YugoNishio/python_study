#classの定義
"""
class クラス名:
   def __init__(self,引数2,引数3): #初期化メソッド
       self.変数名1 = 初期値 #インスタンス変数の初期化
       self.変数名2 = 初期値 #インスタンス変数の初期化
"""
#インスタンス変数にアクセスする
"""
インスタンス名.変数名
"""

class GunkenKun:
    def __init__(self, strategy = "attacker"): #初期化メソッド
        self.strategy = strategy #引数で受け取ったstrategyの値を代入
robot = GunkenKun() #変数robotにGunkenKunのインスタンスを代入(インスタンスの作成)
print(robot.strategy)
print("\n")

robot.strategy = "defender" #インスタンス変数の値をdefenderに更新
print(robot.strategy)

#class内に関数を宣言する(クラス内の関数をメソッドと呼びます)(class_2.pyに続く…)