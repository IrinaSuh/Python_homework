# вариант 3
# О каждом учащемся класса известны его пол, год рождения, рост и вес.
# Определить, сколько в классе мальчиков и сколько девочек.
# Найти средний возраст мальчиков и девочек.
# Определить, верно ли, что самый высокий мальчик весит больше всех в классе,
# а самая маленькая девочка является самой юной среди девочек.
import datetime

Stud = [["Вася","m",2011,160,45],
        ["Оля","f",2012,165,50],
        ["Ира","f",2010,158,38],
        ["Саша","m",2010,163,63],
        ["Таня","f",2011,150,35],
        ["Света","f",2012,155,40]]
sumF=0
sumM=0
sumAge=0

# Определить, сколько в классе мальчиков и сколько девочек
for i in range(len(Stud)):
    for j in range(len(Stud[i])):
        if j==1:
            if Stud[i][j]=='f':
                sumF=int(sumF+1)
            else:
                sumM=int(sumM+1)
print("Девочек "+str(sumF),"   Мальчиков "+str(sumM))

# Найти средний возраст мальчиков и девочек
a = datetime.datetime.today()
for i in range(len(Stud)):
    for j in range(len(Stud[i])):
        if j==2:
            sumAge=sumAge+int(a.year-Stud[i][j])
print("Средний возраст = "+ str(sumAge/len(Stud)))

# верно ли, что самый высокий мальчик весит больше всех в классе
maxMass = 0
maxHeight = 0
for i in range(len(Stud)):
    for j in range(len(Stud[i])):
        if Stud[i][1] == 'm':
            if Stud[i][3] >maxMass:
                maxMass = Stud[i][3]
                k=i
            if Stud[i][4] >maxHeight:
                maxHeight = Stud[i][4]
                m=i
if k==m:
    print ("Верно. Самый высокий мальчик весит больше всех в классе")
else:
    print("Неверно. Самый высокий мальчик Не весит больше всех в классе")

# Верно ли, что самая маленькая девочка является самой юной среди девочек
minAge = 100
minHeight = 300
for i in range(len(Stud)):
    for j in range(len(Stud[i])):
        if Stud[i][1] == 'f':
            if Stud[i][2] > minAge:
                minAge = Stud[i][2]
                k=i
            if Stud[i][4] < minHeight:
                minHeight = Stud[i][4]
                m=i
if k==m:
    print ("Верно. Самая маленькая девочка является самой юной среди девочек")
else:
    print("Неверно. Cамая маленькая девочка НЕ является самой юной среди девочек")
