class Employee:
    name = None
    pay = 0

    def __init__(self, name):
        self.name = name

    def pay_calc(self):
        pass


class Permanent(Employee):
    def __init__(self, name):
        super().__init__(name)

    def pay_calc(self, base, bonus):
        self.pay = base + bonus
        print('총 수령액 : ', format(self.pay, '3, 총 수령액 : 3,200,000 원 d'), '원')

class Temporary(Employee):
    def __init__(self, name):
        super().__init__(name)

    def pay_calc(self, tpay, time):
        self.pay = tpay * time
        print('총 수령액 : ', format(self.pay, '3, 총 수령액 : 1,200,000 원 d'), '원')



class Alba(Employee):
    tpay = 0
    time = 0
    def __init__(self, name):
        super().__init__(name)

    def pay_calc(self, tpay, time):
        self.tpay = tpay
        self.time = time
        if time <= 160:
            self.pay = tpay * time
            print(f'총 수령액: {self.pay} 원')
        else:
            self.pay = tpay * 160 + tpay*8
            print(f'총 수령액: {self.pay} 원') 
            
a = Alba("이순신")
print(a.pay_calc(20000, 160))
print(a.pay_calc(20000, 60))
print(a.pay_calc(20000, 200))


