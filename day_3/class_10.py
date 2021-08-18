#継承(コンストラクタ(初期化メソッド)のオーバーライド)

"""super()の書き方
def __init__(self):
        super().__init__(value_1, value_2, value_3)
"""

class Planet: #スーパークラス
    def __init__(self, name = 'Earth', orbital_plane = 'same', orbit = 'circle'):
        self.name = name
        self.orbital_plane = orbital_plane
        self.orbit = orbit

    @property
    def common(self):
        return self.name, self.orbital_plane, self.orbit      

class Mars(Planet): #サブクラス
    def __init__(self):
        super().__init__('Mars') #インスタンス変数の再設定 引数[name]にMarsを代入

earth = Mars() #子クラスをインスタンス化してみる
print("名前:" + earth.common[0], "軌道面:" + earth.common[1], "軌道:" + earth.common[2]) #親クラス(Planet)が反映