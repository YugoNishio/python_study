#10回数字を入力し、小数点を切り捨てた平均値を出す
import math

value = 0
for i in range(10):
    num = int(input("整数を入力してください-->"))
    value = value + num

answer = math.floor(value / 10)
print(answer)