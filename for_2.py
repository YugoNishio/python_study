#range関数の使い方_1
for num_1 in range(5): #0～5未満(4まで)の5つの数字を指定
    print(num_1)
print("\n") #使い方ごとの区切り用

#range関数の使い方_2
for num_2 in range(10, 15): #10～15未満(14まで)の5つの数字を指定,初期値を指定できる(今回は10を指定)
    print(num_2)
print("\n")

#range関数の使い方_3
for num_3 in range(0, 10, 2): #0～10未満(9まで)を2ずつ増加させた値を指定
    print(num_3)

#for文中の条件分岐について(for_3.pyに続く…)