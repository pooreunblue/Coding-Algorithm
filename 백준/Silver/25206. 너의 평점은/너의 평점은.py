import sys

s = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
score = 0
credit = 0
while True:
    try:
        r = sys.stdin.readline().split()
        if r[2] == 'P':
            continue
        score += float(r[1]) * s[r[2]]
        credit += float(r[1])
    except:
        break
        
if credit == 0:
    print(0.0)
else:
    print(score / credit)