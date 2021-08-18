#ポリモフィズム

class Earth:
    def __init__(self, situation = None):
        self.situation = situation

    def yabai(self):
        print(self.situation + "分かりましたヒーローを向かわせます")

    def hero(self):
        print("私が来たっ!!もう大丈夫!!")

class GlobalWarming:
    def __init__(self, situation):
        Earth.__init__("地球温暖化")

class HugeMeteorite:
    def yabai(self):
        print("巨大隕石衝突です")

def Yabai(Earth):

GW = GlobalWarming()
yabai(GW)