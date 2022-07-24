import math
from numbers import Number

class Complex:
    real = 0
    img = 0
    def __init__(self, _real=0, _img=0):
        self.real = _real
        self.img = _img

    def __eq__(self, other):
        if isinstance(other, Complex):
            return self.real == other.real and self.img == other.img

    def __neg__(self):
        return Complex(-self.real, -self.img)

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.img + other.img)
        elif isinstance(other,Number):
            return Complex( other + self.real,  self.img)
        else :
            raise ValueError("Cannot carryout operation due to mismatched datatype")


    def __radd__(self, other):
        if isinstance(other,Number):
            return Complex( other + self.real,  self.img)
        else :
            raise ValueError("Cannot carryout operation due to mismatched datatype")


    def __sub__(self, other):
        if isinstance(other, Complex):
            return self + (-other)
        elif isinstance(other,Number):
            return Complex( self.real -other , self.img)
        else :
            raise ValueError("Cannot carryout operation due to mismatched datatype")
    
    def __rsub__(self, other):
        if isinstance(other, Complex):
            return (-self) + other
        elif isinstance(other,Number):
            return Complex( other - self.real, - self.img)
        else :
            raise ValueError("Cannot carryout operation due to mismatched datatype")

    def __mul__(self, other):
        if isinstance(other, Complex):
            a = self.real * other.real - self.img * other.img
            b = self.real * other.img + self.img * other.real
            return Complex(a, b)
        elif isinstance(other, Number):
            return Complex(self.real * other, self.img * other)
        else :
            raise ValueError("Cannot carryout operation due to mismatched datatype")

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        
        if isinstance(other, Complex):
            if self.real == 0 and self.img == 0:
                return Complex(0, 0)

            if other.real == 0 and other.img == 0:
                raise ValueError("Division by Zero ")
            return (self * other.conj()) / (other.real * other.real + other.img * other.img)
        elif isinstance(other, Number):
            return Complex(self.real / other, self.img / other)
        else :
            raise ValueError("Cannot carryout operation due to mismatched datatype")


    def __rtruediv__(self, other):
        if isinstance(other, Complex):
            if other.real == 0 and other.img == 0:
                return Complex(0, 0)

            if self.real == 0 and self.img == 0:
                raise ValueError("Division by Zero ")

            return (other * self.conj()) / self.mod_squared()
        elif isinstance(other, Number):
            return Complex(other, 0) / self
        else :
            raise ValueError("Cannot carryout operation due to mismatched datatype")


    def __abs__(self):
        return math.sqrt(self.real*self.real+self.img*self.img)

    def __pow__(self):
        raise NotImplementedError("Power of complex nummer not implemented")

    def conj(self):
        return Complex(self.real, -self.img)

    def real(self):
        return self.real

    def imag(self):
        return self.img

    def arg(self):
        return math.atan2(self.img, self.real)

    def __str__(self):
        
        if self.img >= 0:
            op = "+"
        else :
            op = "-"
        return "{} {} {}i".format(self.real, op, abs(self.img))

def main():
        
    a = Complex(3,4)
    b = Complex(0,1)

    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print("__")
    print(a+0.5)
    print(a-0.5)
    print(a*0.5)
    print(a/0.5)
    print("__")
    print(5+0.5*b)
    print(5-0.5*b)
    print(5*0.5*b)
    print(5/0.5*b)

if __name__ =="__main__":
    main()

