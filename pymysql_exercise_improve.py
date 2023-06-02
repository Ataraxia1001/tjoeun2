import pymysql
import os


config = {                
'host' : '127.0.0.1',  
'user' : 'user1',     
'passwd' : '0000',  
'database' : 'test_db', 
'port' : 3306,       
'charset' : 'utf8',     
'use_unicode' : True    
}


def sign_up():
    try:
        conn = pymysql.connect(**config)
        cursor = conn.cursor() 
        sql = 'create table if not exists tb1(name varchar(20), age int, num int)'
        cursor.execute(sql)

        in_name = input("회원 성명을 입력하세요 : ")
        if in_name:
            sql = f"select * from tb1 where NAME = '{in_name}'"
            cursor.execute(sql)
            rows = cursor.fetchall()
            if len(rows) > 0:
                print("이미 존재하는 이름입니다. 다른 이름을 입력하세요.")

            else:
                in_age = int(input("나이를 입력하세요 : "))
                in_num = int(input("수량을 입력하세요 : "))
                sql = f"insert into tb1(name,age,num) values('{in_name}', {in_age}, {in_num})"
                cursor.execute(sql)
                rows = cursor.fetchall()
                conn.commit()
                print("회원등록을 성공했습니다.") 
        
    except Exception as e :
        print('db 연동 error :', e)
        conn.rollback()

    finally:
        cursor.close()
        conn.close()



def search_all():
    try:
        conn = pymysql.connect(**config)
        cursor = conn.cursor() 
        
        #요구사항 2
        sql = "select * from tb1"
        cursor.execute(sql)
        rows = cursor.fetchall()
        print('---tb1 테이블 조회---')
        print("NAME, AGE, NUM")
        
        for row in rows :
            print(f"('{row[0]}', {row[1]}, {row[2]})")

    except Exception as e :
        print('db 연동 error :', e)
        conn.rollback()

    finally:
        cursor.close()
        conn.close()




def search_input():
    try:
        conn = pymysql.connect(**config)
        cursor = conn.cursor() 

        #요구사항 3
        name = input("조회할 이름 입력하세요 : ")
        sql = f"select * from tb1 where name like  '%{name}%' "
        cursor.execute(sql)
        rows = cursor.fetchall()
        print('===회원조회2===')

        if rows :
            for row in rows :
                print('조회결과는 이름 :', row[0], '나이 :', row[1],
                  '수량 :', row[2])
        else :
            print('조회결과 입력한 이름에 맞는 회원이 없습니다.') 
    
    except Exception as e :
        print('db 연동 error :', e)
        conn.rollback()

    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    while True:
        os.system('cls')
        print("-----회원관리-----")
        print("회원 등록 : 1 ")
        print("전체회원목록: 2 ")
        print("개별회원조회 : 3 ")
        print("회원 수정 : 4 ")
        print("회원 삭제 : 5 ")
        print("종료 : 6 ")
    
        num = int(input("작업을 선택하세요 : "))
        if num == 1 : 
            sign_up()
            os.system("pause")
        elif num == 2 : 
            search_all()
            os.system("pause")
        elif num == 3 :
            search_input()
            os.system("pause")
        elif num == 4 :
            print("회원수정기능은 준비중입니다. ")
            os.system("pause")
        elif num == 5 :
            print("회원삭제기능은 준비중입니다. ")
            os.system("pause")
        elif num == 6 :
            break
        else:
            print("없는 기능입니다.")
            os.system("pause")





