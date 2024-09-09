# cards.py
class NumberCard:
    def __init__(self, color, value, points):
        self.color = color
        self.value = value
        self.points = points

    def __str__(self):
        return f'{self.color}: {self.value}'

class SpecialColorCard:
    def __init__(self, color, effect, points=20):
        self.color = color
        self.effect = effect
        self.points = points

    def __str__(self):
        return f'{self.color}: {self.effect}'

class SpecialCard:
    def __init__(self, effect, points=50):
        self.effect = effect
        self.points = points

    def __str__(self):
        return f'{self.effect}'
