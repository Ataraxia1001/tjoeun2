# 63일차-실습-0-5-해답 
import os
import sys
import pymysql # MySQL데이터베이스를 사용하기 위한 라이브러리를 등록함
config = {                  # MySQL데이터베이스를 사용하기 위해 환경변수를 딕셔너리로 생성함. 
    'host' : '127.0.0.1',   # MySql 이 동작하는 ipv4주소 
    'user' : 'root',        # MySql 설치할 때 정한 계정 
    'passwd' : 'root1234',  # MySql 설치할 때 정한 비밀번호
    'database' : 'test_db', # 생성한 데이터베이스
    'port' : 3306,          # MySql이 응용프로그램과 통신할 때 사용하는 포트번호 리터럴이 아닌 정수값으로 써야함
    'charset' : 'utf8',     # 한글을 사용하겠다는 설정 
    'use_unicode' : True    # 한글을 사용하겠다는 설정 
    }
def mem_create() :
    try :
        # (1) db 연동 객체 
        conn = pymysql.connect(**config)    # 딕셔너리 config를 인수로 사용하여 conn 객체를 만듬.
        # sql 실행 객체 
        cursor = conn.cursor()    # conn 객체로부터 cursor() 메소드를 호출하여 cursor 참조변수를 만듬.
        in_name = input("회원 성명을 입력하세요 : ")
        if in_name :
            #print("------>>>>")
            sql = f"select * from tb1 where NAME = '{in_name}'"
            cursor.execute(sql)
            rows = cursor.fetchall()
            if len(rows) > 0 :
                print("이미 존재하고 있습니다. 다른 코드를 입력하세요")
            else :
                in_age = int(input("나이를 입력하세요 : ")) 
                in_num = int(input("수량을 입력하세요 : "))
                sql = f"insert into tb1(name,age,num) values('{in_name}',{in_age},{in_num})" 
                cursor.execute(sql)
                rows = cursor.fetchall()
                conn.commit()
                print("회원등록을 성공했습니다.")
                print()
        else :
            print("회원번호 등록을 위해 이름을 입력해 주세요")
    except Exception as e :
        print('db 연동 실패 : ', e)
        conn.rollback() # 실행 취소 
    finally:
        cursor.close()
        conn.close()

def mem_read1() :
    try :
        # (1) db 연동 객체 
        conn = pymysql.connect(**config)    # 딕셔너리 config를 인수로 사용하여 conn 객체를 만듬.
        # sql 실행 객체 
        cursor = conn.cursor()   # conn 객체로부터 cursor() 메소드를 호출하여 cursor 참조변수를 만듬.

        # (2) 모든 레코드 조회
        cursor.execute("select * from tb1")
        rows = cursor.fetchall()
        print("===tb1 테이블 조회1===")
        print("(name, age, num)")
        for row in rows :
            print(row)
            
    except Exception as e :
        print('db 연동 실패 : ', e)
        conn.rollback() # 실행 취소 
    finally:
        cursor.close()
        conn.close()

def mem_read2() :
    try :
        # (1) db 연동 객체 
        conn = pymysql.connect(**config)    # 딕셔너리 config를 인수로 사용하여 conn 객체를 만듬.
        # sql 실행 객체 
        cursor = conn.cursor()   # conn 객체로부터 cursor() 메소드를 호출하여 cursor 참조변수를 만듬.

        # (3) 단일 레코드 조회  
        in_code = input("조회할 성명을 입력하세요 : ")
        sql = f"select * from tb1 where NAME = '{in_code}'"
        cursor.execute(sql)
        rows = cursor.fetchall()
        if len(rows) > 0 :
            print("===tb1 테이블 조회2===")
            for row in rows :
                print("조회결과는 성명:{}, 나이:{}, 수량:{} 입니다.".format(row[0],int(row[1]),int(row[2])))
        else:
            print("조회결과 입력한 이름에 맞는 회원이 없습니다")
    except Exception as e :
        print('db 연동 실패 : ', e)
        conn.rollback() # 실행 취소 
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__" :
    while True:
        os.system('cls')
        print("---회원관리---")
        print("회원    등록 : 1 ")
        print("회원목록조회 : 2 ")
        print("회원개별조회 : 3 ")
        print("회원    수정 : 4 ")
        print("회원    삭제 : 5 ")
        sel = int(input("작업을 선택하세요 : "))
        if sel == 1 :
            mem_create()
            os.system("pause")
        elif sel == 2 :
            mem_read1()
            os.system("pause")
        elif sel == 3 :
            mem_read2()
            os.system("pause")
        elif sel == 4 :
            print("회원수정기능은 준비중입니다. ")
            os.system("pause")
        elif sel == 5 :
            print("회원삭제기능은 준비중입니다. ")
            os.system("pause")
        else :
            print("잘못 선택했습니다. ")
            os.system("pause")