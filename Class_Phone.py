""" вариант 9
Создать класс Phone: id, Фамилия, Имя, Отчество, Адрес,
Номер кредитной  карточки, Дебет, Кредит, 
Время городских и междугородных разговоров. 
Функции- члены реализуют запись и считывание полей (проверка корректности), 
расчет баланса на текущий момент.
Создать список объектов. Вывести:
a)	сведения об абонентах, у которых время внутригородских разговоров превышает заданное;
b)	сведения об абонентах, которые пользовались междугородной связью;
"""
tarif1=1    # тариф город
tarif2=10   # тариф межгород
class Phone:
    id=0
    fio=''
    __debet=0
    __kredit=0
    __balanse=0
    gorod_time=0
    mezhgorod_time=0
    def __init__(self,new_id,new_fio):  # конструктор
        self.id=new_id
        self.fio=new_fio
    def __str__(self):      # для вызова print()
        return 'тел номер '+ str(self.id) +' владелец '+ self.fio
    def setDebet(self):
        new_debet=input('пополните счет ')
        if new_debet.isdigit():
            self.__debet+=int(new_debet)
            print("пополнение счета на "+str(new_debet))

    def getDebet(self):
        return self.__debet

    def setKredit(self,new_kredit):
        self.__kredit+=new_kredit
        print("списание со счета " + str(new_kredit))
    def getKredit(self):
        return self.__kredit
    def setBalanse(self):
        self.__balanse=self.__debet-self.__kredit
        self.__balanse-=self.gorod_time*tarif1
        self.__balanse-=self.mezhgorod_time*tarif2
    def getBalanse(self):
        self.setBalanse()
        return self.__balanse
    def timeGorod(self,min1):
        self.gorod_time+=min1
        print(self.fio+' '+str(min1)+' минут по городу')
    def timeMezhgorod(self,min2):
        self.mezhgorod_time+=min2
        print(self.fio+' '+str(min2) + ' минут по межгороду')



phone1=Phone(625625,'Иванов АП')
phone2=Phone(625626,'Петров ВС')
phone3=Phone(625627,'Кротов АВ')
phone4=Phone(625628,'Смирнов СС')
phone5=Phone(625629,'Еремин ЕВ')
phone6=Phone(625630,'Хвастун КК')
print(phone1)         # def __str__(self)
phone1.setDebet()
print(phone1.fio+'  дебет='+str(phone1.getDebet())+'руб')
phone1.setKredit(30)
phone1.setKredit(30)

print(phone1.fio+"  всего начислено "+str(phone1.getDebet()))
print(phone1.fio+"  всего списано "+str(phone1.getKredit()))
print(phone1.fio+"  балланс= "+str(phone1.getBalanse()))
phone1.timeGorod(5)
print(phone1.fio+"  балланс= "+str(phone1.getBalanse()))
phone1.timeMezhgorod(5)
print(phone1.fio+"  балланс= "+str(phone1.getBalanse()))

'''
надо бы список абонентов сделать классом с методами
но уже лень((
'''
listAbonent=[phone1,phone2,phone3,phone4,phone5,phone6]
phone2.timeMezhgorod(8)
phone4.timeMezhgorod(6)
phone4.timeGorod(400)
phone5.timeGorod(600)
phone3.timeGorod(9)
print('--- список абонентов с превышением лимита по городу ---')
for i in listAbonent:
    if i.gorod_time>300:
        print(i)
print('--- список абонентов с междугородней связью ---')
for i in listAbonent:
    if i.mezhgorod_time>0:
        print(i)




