from math import sqrt


class Triangle(object):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        return a+b > c and b+c > a and a+c > b

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self.a) * (half - self.b) * (half - self.c))


def main():
    a, b, c = 3, 4, 5
    if Triangle.is_valid(a, b, c):
        tri = Triangle(a, b, c)
        print(tri.perimeter())  # 周长
        print(tri.area())  # 面积
    else:
        print("无法构成三角形")


if __name__ == '__main__':
    main()
