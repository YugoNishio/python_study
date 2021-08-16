#継承(メソッドのオーバーライド)
"""用語
オーバーライド:親クラスのメソッドを子クラスで再定義する行為(要はメソッドの上書き)
"""
class Planet: #親クラス
    def __init__(self, name, orbital_plane = 'same', orbit = 'circle'):
        self.name = name
        self.orbital_plane = orbital_plane
        self.orbit = orbit

    @property
    def common(self):
        return self.name, self.orbital_plane, self.orbit

    def common_info(self):
        print("名前:" + earth.common[0], "軌道面:" + earth.common[1], "軌道:" + earth.common[2])

    def environment(self): #親クラス内でメソッドを用意してる
        environment = "----"
        print(earth.common[0] + "って" + environment + "ですよね")
    
class Earth(Planet): #子クラス
    def environment(self): #オーバーライドしたメソッド
        environment = "過ごしやすい"
        print(earth.common[0] + "って" + environment + "ですよね")

earth = Earth('Earth') #子クラスをインスタンス化
earth.common_info()
earth.environment() #オーバーライドしたメソッドの呼び出し
