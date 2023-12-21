l = input()

zeroList = l.split('0')
oneList = l.split('1')

zeroCnt = 0
oneCnt = 0

for i in zeroList:
    if i != "":
        zeroCnt += 1
for i in oneList:
    if i != "":
        oneCnt += 1

print(min(zeroCnt, oneCnt))