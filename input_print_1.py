# codeing: shift-JIS #日本語認識
#文字を入力して出力したい

print("こんにちは!python勉強会にようこそ\nここでpythonの基礎を一緒に学んでいきましょう!\n") #\nで改行 もしくは\r\n

print("文字を入力してください-->", end= '' )  #end = ' ' が置かれているとprint関数による出力後、改行は行われない
char = input() #charという変数に入力された文字を格納
print(2*char) #文字を倍にして出力

num = input("数値を入力してください-->") #numという変数に入力された文字を格納
print(2*num) #文字を倍にして出力

#数値は数字として扱いたい(input?print_2.pyに続く…)