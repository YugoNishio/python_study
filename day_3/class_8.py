#継承
"""用語
継承(inheritance):クラス機能を再利用/追加する機能
                  あたかもそのクラスで定義したかのようにメソッド/メンバ変数を扱える
親クラス(別名:スーパークラス/基底クラス):継承元. ここで他クラスオブジェクトの共通点を挙げて見通しを良くする
子クラス(別名:サブクラス/派生クラス):継承先.
※注意:共通して使用するメソッドだからと言って全て一つの親クラスに定義するとスパゲッティコードになる
"""
"""継承機能
class 子クラス名(親クラス名):
    pass
"""
class Planet: #親クラス
    def common(self, name, orbital_plane = 'same', orbit = 'circle'):
        print("名前:" + name, "軌道面:" + orbital_plane, "軌道:" + orbit)

class Earth(Planet): #子クラス
    pass #親クラスの内容をそのまま実行するなら子クラス内に何も書かない

earth = Earth() #子クラスをインスタンス化してみる
earth.common('Earth', 'same', 'circle') #Earthクラスのcommonメソッドの呼び出し


class Mars(Planet): #子クラス
    def environment(self, name): #子クラス内で新しく定義してみる
        environment = '寒い'
        print(name + "って" + environment + "ですよね")
mars = Mars()
mars.common('Mars') #Marsクラスのcommonメソッドの呼び出し
mars.environment('Mars') #追加した定義の呼び出しもできる