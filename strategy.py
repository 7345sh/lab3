from abc import ABC, abstractmethod


# Абстрактная стратегия расчёта цены
class PriceStrategy(ABC):
    @abstractmethod
    def calculate(self, price: float) -> float:
        pass


# Обычная цена — без скидки
class RegularPrice(PriceStrategy):
    def calculate(self, price: float) -> float:
        return price


# Цена со скидкой в процентах
class DiscountPrice(PriceStrategy):
    def __init__(self, discount_percent: float) -> None:
        # Проверяем, что скидка в диапазоне от 0 до 100
        if not 0 <= discount_percent < 100:
            raise ValueError("Скидка должна быть в диапазоне [0, 100)")

        # Переводим проценты в долю
        self.discount = discount_percent / 100

    def calculate(self, price: float) -> float:
        # Возвращаем цену за вычетом скидки
        return price * (1 - self.discount)


class VIPPrice(PriceStrategy):
    def calculate(self, price: float) -> float:
        return price * 0.7


# Контекст — использует выбранную стратегию
class PriceCalculator:
    def __init__(self, strategy: PriceStrategy) -> None:
        # Сохраняем переданную стратегию
        self._strategy = strategy

    # Геттер: позволяет читать текущую стратегию
    @property
    def strategy(self) -> PriceStrategy:
        return self._strategy

    # Сеттер: позволяет менять стратегию на лету
    @strategy.setter
    def strategy(self, new_strategy: PriceStrategy) -> None:
        self._strategy = new_strategy

    # Делегируем расчёт стратегии
    def calculate(self, price: float) -> float:
        return self._strategy.calculate(price)


if __name__ == "__main__":
    # Создаём калькулятор с обычной стратегией
    calculator = PriceCalculator(RegularPrice())
    print(f"Обычная цена: {calculator.calculate(1000)}")

    # Меняем стратегию на скидку 10%
    calculator.strategy = DiscountPrice(10)
    print(f"Со скидкой 10%: {calculator.calculate(1000)}")

    # Меняем на скидку 25%
    calculator.strategy = DiscountPrice(25)
    print(f"Со скидкой 25%: {calculator.calculate(1000)}")

    # Меняем на скидку 30% (условный VIP)
    calculator.strategy = VIPPrice()
    print(f"VIP (30%): {calculator.calculate(1000)}")
