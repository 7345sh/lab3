class Animal:
    # Базовый класс: имя и общий метод speak
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        return f"{self.name} издаёт звук"


class Dog(Animal):
    # Класс-наследник Animal
    # Наследник переопределяет speak
    def speak(self) -> str:
        return f"{self.name} лает"


if __name__ == "__main__":
    animals = [Animal("Животное"), Dog("Шарик")]

    for animal in animals:
        print(animal.speak())
