#

class GunkenKun:
    def __init__(self, strategy = "attacker"): #初期化メソッド
        self.strategy = strategy #引数で受け取ったstrategyの値を代入
robot = GunkenKun() #変数robotにGunkenKunのインスタンスを代入(インスタンスの作成)
print(robot.strategy)
print("\n")

robot.strategy = "defender" #インスタンス変数の値をdefenderに更新
print(robot.strategy)