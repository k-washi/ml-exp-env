# 生成に関するパターン
# 1. 一般的なクラス
# 2. Singleton (クラスのインスタンスオブジェクトをアプリケーション内で常に一つしか存在しないということを保証) [データベースへのコネクション部分など]

from typing_extensions import Self

"""
# この実装の場合、継承した先のインスタンスも同じインスタンスになる。
class Singleton:
    _instance = None
    def __new__(cls: type[Self], *args, **kwargs) -> Self:
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
"""


class Singleton():
    @classmethod
    def get_instance(cls, input):
        #
        if not hasattr(cls, "_instance"):
            cls._instance = cls(input)
        else:
            cls._instance.input = input
        return cls._instance

if __name__ == "__main__":
    
    class ConcreteClass(Singleton):
        def __init__(self, input) -> None:
            self.input = input
    class SubConcreteClass(Singleton):
        def __init__(self, input) -> None:
            self.input = input

    print(id(ConcreteClass.get_instance(1)) == id(ConcreteClass.get_instance(2)))
    print(id(SubConcreteClass.get_instance(1)) == id(ConcreteClass.get_instance(2)))
    print(id(SubConcreteClass.get_instance(1)) == id(SubConcreteClass.get_instance(2)))

    one = ConcreteClass.get_instance(1)
    print(one.input)
    two = ConcreteClass.get_instance(2)
    print(one.input, two.input)




