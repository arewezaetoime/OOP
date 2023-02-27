class Employee:
    MONTHS = 12

    def __init__(self, employee_id: int, first_name: str, last_name: str, salary: int):
        self.id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_annual_salary(self) -> int:
        return self.salary * Employee.MONTHS

    def raise_salary(self, amount) -> int:
        self.salary += amount
        return self.salary
