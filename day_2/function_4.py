#yeild(イールド)
"""
関数の処理を一時停止(returnは処理を終了させる)
値を返す
"""
#使用用途
#メモリの使用量を抑える

def one_GB():
    Cap = 1024
    data = 230
    RemCap = Cap - data
    yield data, RemCap

    data = 370
    RemCap -= data
    yield data, RemCap

    data = 424
    RemCap -= data
    yield data, RemCap

#try:
for _ in range(3):
    data_MB, Remaining_Capacity, n = one_GB()
    print("使用したデータ量は" + str(data_MB[0]) + "[MB]です")
    print("残りタスクは" + str(Remaining_Capacity[1]) + "[MB]です")
    print(n)
#except: