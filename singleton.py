class Singleton:
    # Классовое поле хранит единственный экземпляр класса
    _instance = None

    # Вызывается при создании объекта, до __init__
    def __new__(cls) -> "Singleton":
        # Если экземпляр ещё не создан — создаём
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        # Возвращаем уже существующий экземпляр
        return cls._instance


if __name__ == "__main__":
    # Оба вызова возвращают один и тот же объект
    s1 = Singleton()
    s2 = Singleton()

    # Проверяем, что это действительно один объект
    print(f"s1 is s2: {s1 is s2}")
