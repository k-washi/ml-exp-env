"""
抽象クラス
"""

from abc import ABC, ABCMeta, abstractmethod

class Pushable1(ABC):
    @abstractmethod
    def push(self, x):
        """引数がなんであろうとpush
        """
    @classmethod
    def __subclasshook__(cls, C):
        

class Pushable2(metaclass=ABCMeta):
    @abstractmethod
    def push(self, x):
        """引数がなんであろうとpush
        """
    
class DummyPushable1(Pushable1):
    def push(self, x):
        return

class IncompletePushable1(Pushable1):
    pass

class DummyPushable2(Pushable2):
    def push(self, x):
        return

class IncompletePushable2(Pushable2):
    pass

if __name__ == "__main__":
    print(DummyPushable1())
    print(DummyPushable2())
    print(IncompletePushable1())
    """
    Traceback (most recent call last):
    File "/workspace/src/sample/designpattern/abstract_base_class.py", line 37, in <module>
        print(IncompletePushable1())
    TypeError: Can't instantiate abstract class IncompletePushable1 with abstract method push
    """
    print(IncompletePushable2())
    