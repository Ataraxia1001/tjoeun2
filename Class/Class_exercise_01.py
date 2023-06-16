# 예제-02
# 클래스 정의
class calc_class :
    # 변수 선언
    x = y = 0
    # 생성자 : 객체 생성 + [멤버변수 초기화] 
    def __init__(self, a, b):
        print('~~객체 생성~~')
        self.x = a 
        self.y = b 
    # 멤버 함수(기능)
    def plus(self): # self : 멤버(변수+함수) 참조 객체 
        p = self.x + self.y
        '''
        p : 지역변수 
        self.x, self.y : 전역변수  
        '''
        return p 
    def minus(self):
        m = self.x - self.y
        return m
# class(1) -> object(n) 생성 
obj1 = calc_class(10, 20) # 생성자 -> 객체1  
# object.member()  
print('plus = ', obj1.plus()) # plus =  30
print('minus =', obj1.minus()) # minus = -10


obj3 = calc_class(70, 90)
print('plus = ', obj3.plus())
print('minus = ', obj3.minus())


obj2 = calc_class(0, 0)
obj2.x = 200
obj2.y = 50

print('plus = ', obj2.plus())
print('minus = ', obj2.minus())







