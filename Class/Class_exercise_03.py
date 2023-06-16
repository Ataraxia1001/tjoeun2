class calc_class14 :
    
    num1 = num2 = 0
    jumin = 0
    year = 0
    month = 0
    day = 0
    
    def __init__(self, x, y):
        self.num1 = x 
        self.num2 = y 
             
    def div(self):
        if self.num2 == 0:
            print("나눗셈 연산은 0으로 나누기가 불가능합니다. 다시 입력하세요.") 
            return None
        else:
            p = self.num1/self.num2
            return p 
    
    def squ(self):
        m = self.num1**(self.num2)
        return m
    
    def member_clear(self, x , y):
        self.num1 = x 
        self.num2 = y 
    
    @classmethod
    def filter(cls, str):
        year = str[:2]
        month = str[2:4]
        day = str[4:6]
        print(f"19{year}년 {month}월 {day}일에 출생한 여자입니다.")
    

    
obj1 = calc_class14(0, 0)
obj1.num1 = int(input("정수를 입력하세요: "))
obj1.num2 = int(input("정수를 입력하세요: "))
obj1.jumin = input("주민번호입력 : ")
obj1.member_clear(obj1.num1, obj1.num2)

print('나눗셈', obj1.div())
print('제곱', obj1.squ())
print(obj1.filter(obj1.jumin))



