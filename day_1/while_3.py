#無限ループとbreak/continue

while True: #無限ループ(条件式がずっとTrue)
    let = input("入力してください-->")
    if let: #letに文字が入っていればTrue
        print(let + "<--入力された値")
        char = input("続けますか? Y/n\n")
        if (char == chr(121)) or (char == chr(13)) or (char == chr(89)): #ASCIIコード 121「y」 13「Enter」 89「Y」
            print(char)
        elif char == chr(110): #ASCIIコード　110「n」
            break
    else: #何も入力されたかった場合、
        continue #ループの始めに戻る
print("while内でbreakが実行されたのでループを終了します")