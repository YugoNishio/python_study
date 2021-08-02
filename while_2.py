#whileの終了時に実行処理

con = 0 #初期化
while con < 5: #ループ条件
    print(con)
    con += 1
else:
    print("ループ条件がFalseになったため、終了します") #whileのループ条件から外れるとelse節内が実行
print("終了")

print("\n") #見やすいように改行

con = 0 #代入
while con < 5: #ループ条件
    print(con)
    con += 1
    if con == 3:
        break
else:
    print("ループ条件がFalseになったため、終了します") #break文が実行されるとelse節内の処理はされない
print("終了")

#break文が使えるということはcontinue文も使える?...(while_3.pyに続く…)