from temperature import Temperature


class Calories:

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        return 10 * self.weight + 6.5 * self.height + 5 - 10 * self.temperature


if __name__ == '__main__':
    temperature = Temperature(country='Italy', city='Firenze').get()
    calorie = Calories(weight=80, height=180, age=28, temperature=temperature)
    print(calorie.calculate())
