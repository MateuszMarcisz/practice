class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b if b != 0 else "Don't do that!"


class LoggingCalculator(Calculator):
    def __init__(self):
        super().__init__()
        self.history = []

    def add(self, a, b):
        result = super().add(a, b)
        self.history.append(f"{a} + {b} = {result}")
        return result

    def sub(self, a, b):
        result = super().sub(a, b)
        self.history.append(f"{a} - {b} = {result}")
        return result

    def mul(self, a, b):
        result = super().mul(a, b)
        self.history.append(f"{a} * {b} = {result}")
        return result

    def div(self, a, b):
        result = super().div(a, b)
        self.history.append(f"{a} / {b} = {result}")
        return result


calc = LoggingCalculator()
print(calc.add(1, 2))
print(calc.sub(1, 2))
print(calc.mul(1, 2))
print(calc.div(1, 2))
print(calc.history)
