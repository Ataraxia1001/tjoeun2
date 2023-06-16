# 166 ~ 167 : super()
# (1) 부모클래스 정의
class Parent :

    # 생성자 : 객체 + 초기화 
    def __init__(self, name, job):
        self.name = name
        self.job = job
        
    # 멤버 함수(method)
    def display(self):
        print('name : {}, job : {}'.format(self.name, self.job))

# 부모 클래스 객체 생성
p = Parent('홍길동', '회사원')
p.display()
        
# (2) 자식 클래스 
class Children(Parent):    # Parent(member) -> Childen1(member)
    gender = None # 자식클래스의 맴버변수 추가
    
    # (3) 자식 클래스생성자
    def __init__(self, name, job, gender):
        # 부모 생성자 호출 
        super().__init__(name, job) # name, job 초기화
        #
        # self.name = name    # if super().__init__(name, job) is used, it is not needed.
        # self.job = job
        self.gender = gender # 자식 멤버

    # 멤버 함수(method) 
    def display(self): # 함수 재정의
        print('name : {}, job : {}, gender : {}' .format(self.name, self.job, self.gender))

# 자식 클래스 객체 생성
chil = Children("이순신", "해군 장군", "남자")
chil.display()
