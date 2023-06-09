# 예제-01 : 다형성(polymorphism)
class Flight: # (1) 부모 클래스
    def fly(self): # 부모 원형 메소드 
        print('날다, fly 원형 메서드')

class Airplane(Flight) : # (2) 자식 클래스 : 비행기
    def fly(self): #  메소드 재정의
        print('비행기가 날다.')
class Bird(Flight) : # (2) 자식 클래스 : 새
    def fly(self): #  메소드 재정의
        print('새가 날다.')
class PaperAirplane(Flight) : # (2) 자식 클래스 : 종이비행기
    def fly(self): #  메소드 재정의
        print('종이 비행기가 날다.')

class Ufo(Flight):
    def fly(self):
        print('UFO가 날아다닙니다.')

# (3) 객체 생성
# 부모 객체 = 자식 객체(자식1, 자식2)
flight = Flight()   # 부모 클래스로부터 객체를 생성하고 
                    # 그 주소를 flight참조변수에 할당함

air = Airplane()    # 자식1 클래스 객체
bird = Bird()       # 자식2 클래스 객체
paper = PaperAirplane() # 자식3 클래스 객체
u = Ufo()

# (4) 다형성
flight.fly() # '날다, fly 원형 메서드' 라고 출력됨 
#
flight = air # 23라인에서 Airplane클래스로부터 만들어진 
             # 객체의 주소를 저장한 것이 air 참조변수이다. 
             # air참조변수에 저장된 객체의 주소값을 flight참조변수에
             # 할당한다는 개념이다.
flight.fly() # '비행기가 날다.' 라고 출력됨 
#
flight = bird
flight.fly() # '새가 날다.' 라고 출력됨 
#
flight = paper
flight.fly() # '종이 비행기가 날다.' 라고 출력됨 
print(u)
print(flight)


flight = u
flight.fly()
print(u)
print(flight)