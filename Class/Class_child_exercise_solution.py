# 067일차-실습-0-5-해답*
class Employee: # (1) 부모클래스
    name = None; pay = 0
    def __init__(self, name):
        self.name = name
    def pay_calc(self):
        pass
class Permanent(Employee): # (2) 자식클래스 : 정규직
    def __init__(self, name):
        super().__init__(name)  # 부모 생성자 호출
    def pay_calc(self, base, bonus): # 메소드 오버라이드
        self.pay = base + bonus  # 급여 = 기본급+상여금
        print('총 수령액 : ', format(self.pay, '3,d'),'원')
class Temporary(Employee): # (3) 자식클래스 : 임시직
    def __init__(self, name):
        super().__init__(name)  # 부모 생성자 호출
    def pay_calc(self, tpay, time):  # 메소드 오버라이드
        self.pay = tpay * time # 급여 = 작업시간*시급
        print('총 수령액 : ', format(self.pay, '3,d'),'원')
class Alba(Employee): # (3) 자식클래스 : 알바
    def __init__(self, name):
        super().__init__(name)  # 부모 생성자 호출
    def pay_calc(self, tpay, time):  # 메소드 오버라이드
        if time >= 160 :
            self.pay = tpay * time + (tpay * 8) # 급여 = 작업시간*시급 +(수당)
        elif time < 160 :
            self.pay = tpay * time              # 급여 = 작업시간*시급
        print('총 수령액 : ', format(self.pay, '3,d'),'원')
# (4) 객체 생성
p = Permanent("이순신")
p.pay_calc(3000000, 200000)
t = Temporary("홍길동")
t.pay_calc(15000, 80)
a = Alba("알바")
a.pay_calc(20000,160)