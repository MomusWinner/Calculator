from backend.interface import Calculator


class CalculatorImpl(Calculator):
    def sum(self, a: int, b: int) -> int:
        return a + b

    def minus(self, a: int, b: int) -> int:
        return a - b