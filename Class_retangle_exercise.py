class Rectangle:
    width = 0
    height = 0
    area = 0
    circum = 0

    def __init__(self):
        pass

    def area_calc(self, a, b):
        self.width = a
        self.height = b
        self.area = self.width * self.height
        return self.area

    def circum_calc(self, x ,y):
        self.width = x
        self.height = y
        self.circum = (self.width + self.height)*2
        return self.circum
    
    
print("사각형의 넓이와 둘레를 계산합니다.")
width = int(input("사각형의 가로 입력: "))
height = int(input("사각형의 세로 입력: "))

obj = Rectangle()
print('사각형의 넓이 : ', obj.area_calc(width, height))
print('사각형의 둘레 : ', obj.circum_calc(width, height))










