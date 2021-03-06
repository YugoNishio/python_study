#属性
"""用語
属性(attribute):特定のオブジェクトの状態(形/性質/概念)を表現する要素


〇〇属性:〇〇変数の性質を表現する用語(全てをひっくるめて[データ属性])
"""

class Planet:
    AD = 2021 #[AD]がクラス属性(クラス変数は[AD])
    def __init__(self): #コンストラクタ
        self.celsius = None #[celsius]がインスタンス属性(インスタンス変数は[celsius])
        #インスタンス変数はコンストラクタが呼び出されると参照して初期化をする
    def anno_domini(self):
        print("今は西暦%s!!!" % Planet.AD) #クラス属性(AD)の参照をしている


earth = Planet() #インスタンス生成(インスタンス化)
earth.celsius = 15 #[celsius]はインスタンス属性. インスタンス属性の参照をしている

mars = Planet()
mars.celsius = -55 #[celsius]はインスタンス属性. インスタンス属性の参照をしている

print("地球の平均%s[℃ ]" % earth.celsius)
print("火星の平均%s[℃ ]" % mars.celsius) #インスタンスが違うため参照先が異なる(今回はmarsのインスタンス属性)
earth.anno_domini() #[anno_domini()]はメソッド属性. メソッド属性の参照をしている

#属性の参照"プロパティ"の存在(class_7.pyに続く…)