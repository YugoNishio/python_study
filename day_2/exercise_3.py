class Bread:
    def __init__(self):
        self.__taste = 'ブドウ味'
        self.__shape = '十二面体'
bread = Bread()
#print("私のオリジナルのパンは" + bread.taste + "で" + bread.shape + "な形をしている") #パブリック変数ならアクセス可能
print("私のオリジナルのパンは" + bread.__taste + "で" + bread.__shape + "な形をしている") #変数名がそのままだとアクセスできない

#print("私のオリジナルのパンは" + bread._Bread__taste + "で" + bread._Bread__shape + "な形をしている") #プライベート変数にアクセス可能