

class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.__balance = balance


    def deposit(self, amount):
        try:
            # проверяем сумму на пополнение, по аналитике она должна быть положительной
            if amount <= 0:
                raise ValueError("Сумма пополнения должна быть положительной.")
            # осуществляем пополнение, если сумма положительная
            self.__balance += amount
            print(f"Пополнение прошло успешно на сумму: {amount}. Оставшийся доступный баланс {self.__balance}")
        # если словили error, то выводим тест ошибки
        except ValueError as error:
            print(error)

#Test
# account = BankAccount("Илюха",50)
# account.deposit(100)
# print(account.deposit)


    def withdraw(self, amount):
        try:
            # проверяем, что средств на снятие достаточно
            if amount > self.__balance:
                raise ValueError("Запрашиваемая сумма на снятие больше доступного баланса")

            # проверяем, что сумма снятия положительная
            if amount <= 0:
                raise ValueError("Сумма снятия должна быть больше 0")

            self.__balance -= amount
            print(f"Снятие на сумму {amount} прошло успешно. Оставшийся доступный баланс {self.__balance}")

        except ValueError as error:
            print(error)

#Test
# account = BankAccount("Илюха",100)
# account.withdraw(10)
# print(account.withdraw)

    def get_balance(self):
        # print(f"Текущий баланс: {self.__balance}")
        return self.__balance


# Тест
# my_balance = BankAccount("Mark", 100)
# my_balance.get_balance()
# print(my_balance.get_balance)


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        balance = self._BankAccount__balance
        if balance > 0:
            interest = balance * self.interest_rate
            self._BankAccount__balance += interest
            print(f"Начислены проценты на остаток {self.interest_rate * 100}. Остаток на балансе {self._BankAccount__balance}")
        else:
            print("Остаток на балансе равен 0 или отрицательный. Проценты не начисляются")

# Тест
# interest_account = SavingsAccount("Mark",100,0.05)
# print(f"Начальный баланс: {interest_account.get_balance()}")
# interest_account.apply_interest()

class CheckingAccount(BankAccount):
    def __init__(self, owner, balance = 0):
        super().__init__(owner, balance)

    def withdraw(self, amount):
        self._BankAccount__balance -= amount
        print(f"Снятие на сумму {amount} прошло успешно. Оставшийся доступный баланс {self.get_balance()}")

# account = CheckingAccount("Olya", 1000)
# account.withdraw(1200)

account = SavingsAccount("Mary",2000,0.05)
account.deposit(500)
account.withdraw(100)
account.apply_interest()

def test_account():
    assert account.get_balance() > 0, "Баланс меньше 0"
    print("Тест пройден успешно")

















