import time
#inisialisasi
digit = [i for i in range(10)]
letter = []
summ = []
firstLetter = []
dummy = []

def permutXDigit(arrray,X):
    if (X == 0) : return [[]]
    if (len(arrray) == 0) : return []
    if (len(arrray) == 1) : return [arrray]
    l = []
    for i in range (len(arrray)):
        j = arrray[i]
        k = arrray[:i] + arrray[i+1:]
        for m in permutXDigit(k,X-1):
            l.append([j] + m)
    return l
def checkLet(x):
    i = 0
    found = False
    while (i < len(letter) and not found):
        if (x == letter[i]) : found = True
        i += 1
    return found
def checkFirstLet(x):
    i = 0
    found = False
    while (i < len(firstLetter) and not found):
        if (x == firstLetter[i]) : found = True
        i += 1
    return found
def getPosition(x):
    for i in range(len(letter)):
        if (x == letter[i]) : return i
print("Inputkan nama file uji di folder test : ", end="")
name = input()
name = "../test/" + name
with open(name, 'r') as fd :
    operand = fd.read().splitlines()

start = time.time()
for i in range (len(operand)):
    
    operand[i] = operand[i].replace(' ', '')
    operand[i] = operand[i].replace('+', '')
    dummy.append(operand[i])

for i in range(len(operand)-2):
    for j in range(len(operand[i])):
        if not checkLet(operand[i][j]):
            letter.append(operand[i][j])
            summ.append(0)
        if j == 0 and not checkFirstLet(getPosition(operand[i][j])):
            firstLetter.append(getPosition(operand[i][j]))
        summ[getPosition(operand[i][j])] += 10**(len(operand[i])-j-1)
dum = len(operand)-1
for j in range(len(operand[dum])):
    if not checkLet(operand[dum][j]):
        letter.append(operand[dum][j])
        summ.append(0)
    if j == 0 and not checkFirstLet(getPosition(operand[dum][j])):
        firstLetter.append(getPosition(operand[dum][j]))
    summ[getPosition(operand[dum][j])] -= 10**(len(operand[dum])-j-1)
permutation = permutXDigit(digit,len(letter))
dum = 0
result = [0 for i in range(len(letter))]
counter = 0
dum = 0
found = False

while dum != len(permutation) and not found:
    
    i = 0
    zero = False
    while i != len(firstLetter) and not zero:
        if permutation[dum][firstLetter[i]] == 0:
            zero = True
        i += 1
    if not zero :
        check = 0
        for j in range(len(result)):
            result[j] = permutation[dum][j]
            check += result[j] * summ[j]
        if check == 0 :
            found = True
            
    counter += 1
    dum += 1

for i in range(len(dummy)):
    for j in range(len(letter)):
        dummy[i] = dummy[i].replace(letter[j],str(result[j]))

for i in range(len(dummy)):
    if (i == len(dummy)-3):
        print((operand[i]+ "+").ljust(12) + dummy[i] + "+" )
    else:
        print(operand[i].ljust(12) + dummy[i])	

end = time.time()
print("jumlah tes yang dilakukan " + str(counter))
print("waktu yang dihabiskan " + str(end-start))
