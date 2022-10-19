import abc

class Calculator(abc.ABC):
    @abc.abstractmethod
    def sum(self, a: int, b: int) -> int:
        """Returns the sum of the arguments"""
        pass
    @abc.abstractmethod
    def minus(self, a: int, b: int) -> int:
        """Returns the difference of the arguments"""
        pass


