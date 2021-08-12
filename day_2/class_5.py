#カプセル化について
"""用語
カプセル化: プログラムの外部からの操作を制御、独立性を保つ仕組み
            ユーザーが使える機能を制限することでプログラムの干渉を抑えられる
メンバ: クラス内で使用する変数. つまりインスタンス変数もクラス変数もメンバ
プライベート変数: 特定の方法でのみアクセスできる変数. 不慮の事故を防げる
"""

#例
class Planet:
    description = '惑星について' #publicなクラス変数を宣言
    def __init__(self): #コンストラクタ
        self.__name = 'Earth' #インスタンスの初期化 private(とする)なインスタンス変数を宣言
        self.__half_size = 6371
        self.__mass = 5.9e24
        self.__surface_tenperature = 288
planet = Planet()
print('planet_name:{0}, half_size:{1}[km], mass:{2}[kg], surface_temperature:{3}[K]'\
            .format(planet.__name, planet.__half_size, planet.__mass, planet.__surface_tenperature))
            #AttributeError(Planetオブジェクトは__name属性を持っていないというエラー)が出る
            #マングルの効果で変数の名前が変わっているため、そんな名前は存在しないと言われる


"""実は…
Pythonにデータを隠蔽する機能はなく,その気になれば参照できてしまう(デバッグ的には便利)
名前マングリング(name mangling):メンバの名前の衝突を避けるサポート機構
マングル(mangle):難号化.メンバの先頭に"アンダースコア"を2つ置くことで変数名が変わる
"""
#print(planet._Planet__name) #マングル化した後の変数名でアクセスすると参照出来てしまう
#planet._Planet__name = 'Mars' #もちろん値の変更も可能