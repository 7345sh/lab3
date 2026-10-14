class BankAccount:
    # Инициализация счёта с владельцем и начальным балансом
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self._balance = balance

    # Баланс счёта защищён, доступен только для чтения
    @property
    def balance(self) -> float:
        return self._balance

    # Вывод данных о счёте
    def __str__(self) -> str:
        return f"{self.owner}, баланс — {self.balance}"

    # Метод для пополнения счёта
    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self._balance += amount

    # Метод для снятия со счёта
    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self._balance:
            raise ValueError("Недостаточно средств на счёте")
        self._balance -= amount


if __name__ == "__main__":
    account = BankAccount("Лосева Елизавета", 10000)

    print(f"Владелец: {account.owner}")
    print(f"Начальный баланс: {account.balance}")

    account.deposit(2500)
    print(f"Пополнение счёта... \nБаланс: {account.balance}")

    account.withdraw(1000)
    print(f"Снятие со счёта... \nБаланс: {account.balance}")

    try:
        account.withdraw(20000)
    except ValueError as e:
        print(f"Ошибка снятия: {e}")

    print(account)
