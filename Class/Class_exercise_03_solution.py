# 066일차-실습-0-5-해답
class Calc_class14:
    num1 = num2 = 0
    def __init__ (self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def div1(self):
        if self.num1 == 0 or self.num2 == 0:
            return "나눗셈연산은 0으로 나누기가 불가능합니다. 다시 입력하세요."
        else:
            return self.num1 / self.num2

#    def div2(self):
#        if g_num1 == 0 or g_num2 == 0:
#            return "div2()나눗셈연산은 0으로 나누기가 불가능합니다. 다시 입력하세요."
#        else:
#            return g_num1 / g_num2    

    def squ(self):
        return self.num1 ** self.num2

    @classmethod      #클래스 메소드의 시작을 알리는 데코레이터 
    def filter(cls, str):   #클래스 매소드 시작 
        print ('19%s년 %s월 %s일에 출생한 %s입니다.' 
        %(str[:2], str[2:4], str[4:6], "남성" if int(str[7]) % 4 == 1 or int(str[7]) % 4 == 3 else "여성"  ))


g_num1 = int(input('숫자입력 : '))
g_num2 = int(input('숫자입력 : '))
g_jumin = input('주민번호입력 : ') # 990101-2222222
c1 = Calc_class14(g_num1, g_num2)
print ("나눗셈 :",c1.div1())
#print ("나눗셈2 :",c1.div2())
print ("제곱 :",c1.squ())

# filter is with class name. (not with instance!)
Calc_class14.filter(g_jumin)