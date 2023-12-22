score = {'A+' : 4.5, 'A0': 4.0, 'B+' : 3.5, 'B0':3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F": 0.0}

totalCredit = 0.0
creditMultiScore = 0.0
for i in range(20):
    subject = input().split(' ')
    if subject[2] == "P":
        continue
    totalCredit += float(subject[1])
    creditMultiScore += float(subject[1]) * float(score[subject[2]])

print("%.6f" %(creditMultiScore/totalCredit))