# 064일차-실습-0-4-해답
import os
import sys
import pymysql # MySQL데이터베이스를 사용하기 위한 라이브러리를 등록함
config = {                  # MySQL데이터베이스를 사용하기 위해 환경변수를 딕셔너리로 생성함. 
    'host' : '127.0.0.1',   # MySql 이 동작하는 ipv4주소 
    'user' : 'root',        # MySql 설치할 때 정한 계정 
    'passwd' : 'root1234',  # MySql 설치할 때 정한 비밀번호
    'database' : 'test_db', # MySql 설치할 때 처음 생성한 데이터베이스
    'port' : 3306,  # MySql이 응용프로그램과 통신할 때 사용하는 포트번호 리터럴이 아닌 정수값으로 써야함
    'charset' : 'utf8',     # 한글을 사용하겠다는 설정 
    'use_unicode' : True    # 한글을 사용하겠다는 설정 
    }
class GoodsRead :
    def __init__(self,read_sel): # 생성자 : read_sel : 코드/상품명 ,            
        self.read_sel = read_sel
        if read_sel == '코드' :  #  read_sql : "select * from goods where code =" / "select * from goods where name ="
            self.read_sql = "select * from goods where code ="
        else :
            self.read_sql = "select * from goods where name ="
    def goodsReadOne(self) :
        try :
            # (1) db 연동 객체 
            conn = pymysql.connect(**config)    # 딕셔너리 config를 인수로 사용하여 conn 객체를 만듬.
            # sql 실행 객체 
            cursor = conn.cursor()     # conn 객체로부터 cursor() 메소드를 호출하여 cursor 참조변수를 만듬.
            # (3) 단일 레코드 조회  
            rows = []
            os.system('cls')
            print("<<<상품 개별 조회({})입니다>>>".format(self.read_sel))
            if self.read_sel == '코드' :
                in_code = int(input("조회할"+self.read_sel+"를 입력하세요 : "))
            else :
                in_code = input("조회할"+self.read_sel+"를 입력하세요 : ")
            sql = self.read_sql + f"'{in_code}'"
            cursor.execute(sql)
            rows = cursor.fetchall()
            if len(rows) > 0 :
                print("===goods 테이블 조회2({})===".format(self.read_sel))
                for row in rows :
                    print("조회결과는 코드:{}, 품명:{}, 수량:{}, 단가:{}  입니다.".format(int(row[0]),row[1],int(row[2]),int(row[3])    ))
            else:
                print("조회결과 입력한 {}에 맞는 상품이 없습니다".format(self.read_sel))
        except Exception as e :
            print('db 연동 실패 : ', e)
            conn.rollback() # 실행 취소 
        finally:
            cursor.close()
            conn.close()
def tableCreate() :
    try :
        print("----->")
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        sql = """create table goods(
            code int primary key,
            name varchar(30) not null,
            su int default 0,
            dan int default 0
            )"""
        cursor.execute(sql)
        conn.commit()
    except Exception as e :
        print("오류 : ",e)
        conn.rollback()
    finally :
        conn.close()
        cursor.close()
def goodsCreate() :
    try :
        # (1) db 연동 객체 
        conn = pymysql.connect(**config)    # 딕셔너리 config를 인수로 사용하여 conn 객체를 만듬.
        # sql 실행 객체 
        cursor = conn.cursor()     # conn 객체로부터 cursor() 메소드를 호출하여 cursor 참조변수를 만듬.
        os.system('cls')
        print("<<<상품 등록입니다>>>")
        in_code = int(input("상품 코드를 입력하세요 : "))  #
        if in_code > 0 :
            #print("------>>>>")
            sql = f"select * from goods where code = '{in_code}'"
            cursor.execute(sql)
            rows = cursor.fetchall()  # rows = [ (선풍기, 25, 14) ]
            if len(rows) > 0 :
                print("이미 존재하고 있습니다. 다른 코드를 입력하세요")
            else :
                in_name = input("상품명을 입력하세요 : ") 
                in_su = int(input("수량을 입력하세요 : ")) 
                in_dan = int(input("단가를 입력하세요 : "))
                sql = f"insert into goods(code,name,su,dan) values({in_code},'{in_name}', {in_su},{in_dan})" 
                cursor.execute(sql)
                rows = cursor.fetchall()
                conn.commit()
                print("상품등록을 성공했습니다.")
                print()
        else :
            print("상품 등록을 위해 코드를 입력해 주세요")
    except Exception as e :
        print('오류 : ', e)
        conn.rollback() # 실행 취소 
    finally:
        cursor.close()
        conn.close()
def goodsReadAll() :
    try :
        # (1) db 연동 객체 
        conn = pymysql.connect(**config)    # 딕셔너리 config를 인수로 사용하여 conn 객체를 만듬.
        # sql 실행 객체 
        cursor = conn.cursor()     # conn 객체로부터 cursor() 메소드를 호출하여 cursor 참조변수를 만듬.
        # (2) 모든 레코드 조회
        os.system('cls')
        print("<<<상품 목록 조회입니다>>>")
        cursor.execute("select * from goods")
        rows = cursor.fetchall()
        print("===goods 테이블 조회1===")
        print("(code, name, su, dan)")
        for row in rows :
            print(row)
    except Exception as e :
        print('db 연동 실패 : ', e)
        conn.rollback() # 실행 취소 
    finally:
        cursor.close()
        conn.close()
if __name__ == "__main__" :
    tableCreate()
    while True:
        os.system('cls')
        print("---상품관리---")
        print("상품    등록 : 1 ")
        print("상품목록조회 : 2 ")
        print("코드별  조회 : 3 ")
        print("상품명별조회 : 4 ")
        print("상품    수정 : 5 ")
        print("상품    삭제 : 6 ")
        print("상품관리종료 : 9 ")
        sel = int(input("작업을 선택하세요 : "))
        if sel == 1 :
            goodsCreate()
            os.system("pause")
        elif sel == 2 :
            goodsReadAll()
            os.system("pause")
        elif sel == 3 :
            r1 = GoodsRead('코드')
            r1.goodsReadOne()
            os.system("pause")
        elif sel == 4 :
            r1 = GoodsRead('상품명')
            r1.goodsReadOne()
            os.system("pause")
        elif sel == 5 :
            print("상품수정기능은 준비중입니다. ")
            os.system("pause")
        elif sel == 6 :
            print("상품삭제기능은 준비중입니다. ")
            os.system("pause")
        elif sel == 9 :
            print("상품관리를 종료합니다. ")
            os.system("pause")
            os.system('cls')
            sys.exit(0)
        else :
            print("잘못 선택했습니다. ")
            os.system("pause")