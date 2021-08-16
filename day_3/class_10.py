#継承(コンストラクタ(初期化メソッド)のオーバーライド)
"""
def __init__(self, name, orbital_plane, orbit):
        super().__init__(name, orbital_plane, orbit)


class Planet: #親クラス
    def __init__(self, name, orbital_plane, orbit):
        self.name = name
        self.orbital_plane = orbital_plane
        self.orbit = orbit

    @property
    def common(self):
        return self.name, self.orbital_plane, self.orbit      

class Earth(Planet): #子クラス
    pass #親クラスの内容をそのまま実行するなら子クラス内に何も書かない

earth = Earth('Earth', 'same', 'circle') #子クラスをインスタンス化してみる
print("名前:" + earth.common[0], "軌道面:" + earth.common[1], "軌道:" + earth.common[2]) #親クラス(Planet)が反映
"""