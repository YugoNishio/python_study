class Car:
    def __init__(self, colour, displacement):
        #インスタンス変数の初期化
        self.colour = colour
        self.displacement = displacement
    def car_info(self):
        #出力コード
        print("色:{0}  排気量:{1}[cc]" .format(self.colour, self.displacement))
#オブジェクト/インスタンス生成
car_w = Car('White', 1250)
car_r = Car('Red', 2500)
#メソッドの呼び出し
car_w.car_info()
car_r.car_info()