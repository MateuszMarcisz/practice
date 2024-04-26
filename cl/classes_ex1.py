class Calculator:
    def __init__(self):
        self.lst = []

    def add(self, num1, num2):
        result = num1 + num2
        self.lst.append(f"added {num1} to {num2} got {result}")
        return result
    def multiply(self, num1, num2):
        result = num1 * num2
        self.lst.append(f"multiplied {num1} with {num2} got {result}")
        return result

    def print_operations(self):
        for operation in self.lst:
            print(operation)


hahaa = Calculator()
print(hahaa.add(num1=5, num2=7))
print(hahaa.multiply(num1=5, num2=7))
hahaa.print_operations()
