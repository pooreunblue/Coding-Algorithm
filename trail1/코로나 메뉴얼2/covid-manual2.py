count = 0
patients = [0]*4
for i in range(3):
    patient = input().split()
    symp = patient[0]
    heat = int(patient[1])
    if symp == 'Y':
        if heat >= 37:
            patients[0] += 1
        else:
            patients[2] += 1
    else:
        if heat >= 37:
            patients[1] += 1
        else:
            patients[3] += 1
for i in range(len(patients)):
    print(patients[i], end = ' ')
if patients[0] >= 2:
    print('E')