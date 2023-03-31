class ATM:
    last_id = 0 # атрибут класса
    all_atms = []

    @classmethod
    def count_atms(cls):
        print("всего банкоматов" ,len(cls.all_atms))

    def __init__(self): # метод экземпляра
        self.id = ATM.last_id # атрибут экземпляра
        self._total = 0 # защищённый атрибут экземпляра
        self.__test = 0 # приватныйы атрибут экземпляра
        ATM.last_id += 1
        ATM.all_atms.append(self)

    def deposit(self, money):
        self._total += money
        print(f"Внесли {money}, на счёте {self._total}")

    def withdraw(self, money):
        print("карта опознана")
        print("пин-код принят")
        self._total -= money
        print(f"Сняли {money}, на счёте {self._total}")


atm1 = ATM()
atm2 = ATM()
atm3 = ATM()

print(atm1.id)
print(atm2.id)
print(atm3.id)

ATM.count_atms()
