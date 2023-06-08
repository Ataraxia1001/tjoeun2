class calc_class :
 
    # num1 = num2 = 0
    
    def __init__(self, x, y):
        print('~~객체 생성~~')
        self.num1 = x 
        self.num2 = y 
    
    def div(self): 
        p = self.num1/self.num2
        return p 
    
    def squ(self):
        m = self.num1**(self.num2)
        return m


obj1 = calc_class(0, 0)
obj1.num1 = int(input("정수를 입력하세요: "))
obj1.num2 = int(input("정수를 입력하세요: "))

print('나눗셈', obj1.div())
print('제곱', obj1.squ())







