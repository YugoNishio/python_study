#インスタンス変数の性質
#インスタンスごとに別々の値を保持できる

#例
class Planet:
    def __init__(self, name = 'Saturn', half_size = 58230, mass = 5.7e26, surface_temperature = 88): #コンストラクタ
        self.name = name #インスタンスの初期化
        self.half_size = half_size
        self.mass = mass
        self.surface_tenperature = surface_temperature
    
    def planet_info(self): #メソッド
        print('planet_name:{0}, half_size:{1}[km], mass:{2}[kg], surface_temperature:{3}[K]'\
            .format(self.name, self.half_size, self.mass, self.surface_tenperature)) #\でコードの改行

planet_e = Planet('Earth', 6371, 5.9e24, 288) #この引数でインスタンス生成/オブジェクトの生成とも言う
planet_m = Planet('Mars', 3389, 6.4e23, 217) #この引数でインスタンス生成
planet_v = Planet('Venus', 6052, 4.9e24, 733)
planet_s = Planet() #インスタンス生成 引数を省略しているのでデフォルト値で生成される

planet_e.planet_info() #メソッドの呼び出し(インスタンス(オブジェクト)の変数名が違うためすみ分けが出来ている)
planet_m.planet_info()
planet_v.planet_info()
planet_s.planet_info()

#クラス変数の性質について(class_4.pyに続く…)