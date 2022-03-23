"""インターフェイス
- インターフェイスの名前の接頭辞にIを使う
- メソッドでselfは使わない
- 空のメソッドのみで構成（pass, NontImplementedEddor, docstringはOK）
- Attributeクラスを用いて、必要な属性を明示

利点：基本的にクラスのメソッドなどは、実行時にしか検証できないが、事前に検証が行える。
"""

from zope.interface import Interface, Attribute, implementer
from zope.interface.verify import verifyClass, verifyObject

class IRectangle(Interface):
    width = Attribute("長方形の幅")
    height = Attribute("長方形の高さ")
    
    def area():
        """長方形の面積を返す
        """

    def perimeter():
        """長方形の周の長さを返す
        """

@implementer(IRectangle)
class Square:
    def __init__(self, size) -> None:
        self.size = size
    
    @property
    def width(self):
        return self.size
    @property
    def height(self):
        return self.size
    def area(self):
        return self.size ** 2
    def perimeter(self):
        return 4 * self.size

@implementer(IRectangle)
class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    #def perimeter(self):
    #    return (self.width + self.height) * 2

if __name__ == "__main__":
    print(verifyObject(IRectangle, Square(2)))
    print(verifyClass(IRectangle, Square))
    print(verifyObject(IRectangle, Rectangle(2, 2)))
    print(verifyClass(IRectangle, Rectangle))