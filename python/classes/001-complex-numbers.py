""" 
For this challenge, you are given two complex numbers, and you have to print the result of their addition, subtraction, multiplication, division and modulus operations.
The real and imaginary precision part should be correct up to two decimal places.

Input Format
One line of input: The real and imaginary part of a number separated by a space.

Output Format
For two complex numbers C and D, the output should be in the following sequence on separate lines:
→ C + D
→ C - D
→ C * D
→ C / D
→ mod(C)
→ mod(D)

For complex numbers with non-zero real(A) and complex part (B), the output should be in the following format:
A + Bi
Replace the plus (+) symbol with a (-) minus symbol when B < 0.

For complex numbers with a zero complex part i.e. real numbers, the output should be:
A + 0.00i
For complex numbers where the real part is zero and the complex part (B) is non-zero, the output should be:
0.00 + Bi

Sample Input:
2 1
5 6

Sample Output:
7.00+7.00i
-3.00-5.00i
4.00+17.00i
0.26-0.11i
2.24+0.00i
7.81+0.00i
 """




# Solution:
import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        a = self.real
        b = self.imaginary
        c = no.real
        d = no.imaginary
        return Complex(a + c, b + d)
        
    def __sub__(self, no):
        a = self.real
        b = self.imaginary
        c = no.real
        d = no.imaginary
        return Complex(a - c, b - d)
        
    def __mul__(self, no):
        a = self.real
        b = self.imaginary
        c = no.real
        d = no.imaginary
        real_mul = (a * c) - (b * d)
        imag_mul = (a * d) + (b * c)
        return Complex(real_mul, imag_mul)

    def __truediv__(self, no):
        a = self.real
        b = self.imaginary
        c = no.real
        d = no.imaginary
        real_numer = a * c + b * d
        imag_numer = b * c - a * d
        denom = c * c + d * d
        real_div = real_numer / denom
        imag_div = imag_numer / denom
        return Complex(real_div, imag_div)

    def mod(self):
        a = self.real
        b = self.imaginary
        return Complex(math.sqrt( a ** 2 + b ** 2), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
