def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class Fraction:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __add__(self, other):
        try:
            if self.b == other.b:
                a = self.a + other.a
                b = self.b
            else:    
                b = self.b * other.b
                self.a = b / self.b * self.a
                other.a = b / other.b * other.a
                a = self.a + other.a
                self.b, other.b = b, b
            
            k = gcd(a, b)

            a //= k
            b //= k
                
            return (int(a), int(b))
        except ZeroDivisionError:
            return "The denominator can't be zero"
    
    def __sub__(self, other):
        try:
            if self.b == other.b:
                a = self.a - other.a
                b = self.b
            else:    
                b = self.b * other.b
                self.a = b / self.b
                other.a = b / other.b
                a = self.a - other.a
                self.b, other.b = b, b
            
            k = gcd(a, b)

            a //= k
            b //= k
                    
            return (int(a), int(b))
        except ZeroDivisionError:
            return "The denominator can't be zero"
    
    def __mul__(self, other):
        if self.b == 0 or other.b == 0:
            raise ZeroDivisionError("The denominator can't be zero")
        
        a = self.a * other.a
        b = self.b * other.b
        
        k = gcd(a, b)

        a //= k
        b //= k
        
        return (int(a), int(b))
    
    def __truediv__(self, other):
        if self.b == 0 or other.b == 0:
            raise ZeroDivisionError("The denominator can't be zero")
        
        a = self.a * other.b
        b = self.b * other.a
        
        k = gcd(a, b)

        a //= k
        b //= k
        
        return (int(a), int(b))
    
    def __eq__(self, other):
        if self.b == 0 or other.b == 0:
            raise ZeroDivisionError("The denominator can't be zero")
        
        if self.a / self.b == other.a / other.b:
            return True
        return False
    
    def __ne__(self, other):
        if self.b == 0 or other.b == 0:
            raise ZeroDivisionError("The denominator can't be zero")
        
        if self.a / self.b == other.a / other.b:
            return False
        return True
        
    def __lt__(self, other):
        if self.b == 0 or other.b == 0:
            raise ZeroDivisionError("The denominator can't be zero")
        
        if self.a / self.b < other.a / other.b:
            return True
        return False
    
    def __gt__(self, other):
        if self.b == 0 or other.b == 0:
            raise ZeroDivisionError("The denominator can't be zero")
        
        if self.a / self.b > other.a / other.b:
            return True
        return False
    
    def __le__(self, other):
        if self.b == 0 or other.b == 0:
            raise ZeroDivisionError("The denominator can't be zero")
        
        if self.a / self.b <= other.a / other.b:
            return True
        return False
    
    def __ge__(self, other):
        if self.b == 0 or other.b == 0:
            raise ZeroDivisionError("The denominator can't be zero")
        
        if self.a / self.b >= other.a / other.b:
            return True
        return False
        

x = Fraction(1, 2)
y = Fraction(1, 4)

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x == y)
print(x > y)
print(x < y)