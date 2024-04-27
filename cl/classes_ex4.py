class Employee:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self._salary = None

    def set_salary(self, salary):
        if salary >= 0.0 and isinstance(salary, (float, int)):
            self._salary = salary


e1 = Employee(1, 'John', 'Smith')
e1.set_salary(100)
print(e1.id, e1.first_name, e1.last_name, e1._salary)