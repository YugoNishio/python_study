#条件分岐によるbreak(終了)とcontinue(スキップ)

for num in range(10): #0～10未満(9まで)の値を順にnumに代入
    if num == 1: #numが1の時、
        continue #これより下の処理をスキップし、繰り返し処理に戻る(printもスキップされる)
    if num == 5: #numが5の時、
        break #終了
    print(num)

#for文の組み合わせ(for_4.pyに続く…)