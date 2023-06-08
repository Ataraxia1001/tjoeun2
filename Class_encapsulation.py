#161 수정버전 
class Account:  # outer -> class
    # (1) 은닉 멤버 변수
    __balance = 0       # 잔액
    __accName = None    # 예금주
    __accNo = None      # 계좌번호

    # (2) 생성자 : 초기화
    def __init__(self, bal, name, no):
        self.__balance = bal    # 잔액 초기화
        self.__accName = name   # 예금주
        self.__accNo = no       # 계좌번호

    # (3) 계좌정보 확인 : Getter메서드 -> 메서드를 실행하는 입장에서 겟한다(얻어낸다)의 뜻 
    def getBalance(self):
        return self.__balance, self.__accName, self.__accNo

    # (4) 입금하기 : Setter메서드 -> 메서드를 실행하는 입장에서 세팅한다(할당한다)의 뜻 
    def setDeposit(self, money):
        if money < 0:
            print('금액 확인')
            return  # 함수 종료(exit)
        self.__balance += money

    # 출금하기 : setter
    def setWithdraw(self, money):
        if self.balance < money:
            print('잔액 부족')
            return  # 함수 종료(exit)
        self.__balance -= money

# (6) object 생성
acc = Account(1000, '홍길동', '125-152-4125-41') # 생성자 실행 

# (7) Getter 호출 : object.member()
#acc.__balance # error ---> 은닉변수는 클래스의 밖에서 직접 참조할 수 없음/ 주석을 풀고 실행해 볼것 
bal = acc.getBalance()
print('계좌정보 : ', bal) # 계좌정보 :  (1000, '홍길동', '125-152-4125-41')

#  (8) Setter 호출  10,000원 입금
acc.setDeposit(10000)
#acc.setDeposit(-10000)  # 마이너스 금액으로 입금하려고 한 경우 42라인 문장과 번갈아가면서 실행 해 볼것 
bal = acc.getBalance()      # getBalance() 매서드는 리턴값이 복수이므로 bal은 튜플
print('계좌정보 : ', bal)
