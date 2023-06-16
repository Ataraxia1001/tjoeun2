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




def register_code():
    try:
        conn = pymysql.connect(**config)
        cursor = conn.cursor() 
        sql = 'create table if not exists goods(code int primary key, name varchar(30) not null, su int default 0, dan int default 0)'
        cursor.execute(sql)
        print("<<<상품 등록입니다>>>")
        in_code = int(input("상품코드 입력하세요 : "))
        if in_code:
            sql = f"select * from goods where CODE = {in_code}"
            cursor.execute(sql)
            rows = cursor.fetchall()
            if len(rows) > 0:
                print("이미 존재하는 상품명입니다. 다른 이름을 입력하세요.")

            else:
                in_name = input("상품명을 입력하세요 : ")
                in_su = int(input("수량을 입력하세요 : "))
                in_dan = int(input("단가 입력하세요 : "))
                sql = f"insert into goods values({in_code}, '{in_name}', {in_su}, {in_dan})"
                cursor.execute(sql)
                rows = cursor.fetchall()
                conn.commit()
                print("상품등록을 성공했습니다.") 
        
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
        sql = "select * from goods"
        cursor.execute(sql)
        rows = cursor.fetchall()
        print('<<<상품 목록 조회결과입니다>>>')
        print('(code, name, su, dan)')
        
        for r in rows :
            #print(r)

# %d is a placeholder for an integer value.
# %s is a placeholder for a string value.
#In the line print('%d %s %d %d'%r), the %d and %s placeholders are replaced 
#by the values in the tuple r.
            print('%d     %s     %d     %d'%r)
                  
        #print('검색 레코드 수 : ', len(rows))

    except Exception as e :
        print('db 연동 error :', e)
        conn.rollback()

    finally:
        cursor.close()
        conn.close()


class Search():

    def search_code(self):
        try:
           conn = pymysql.connect(**config)
           cursor = conn.cursor() 

           #요구사항 3
           print('<<<상품 개별 조회(코드)입니다>>>')
           in_code = input("\n조회할 코드 입력 : ")
           sql = f"select * from goods where code like '%{in_code}%' "
           cursor.execute(sql)
           rows = cursor.fetchall()
           print('===goods 테이블조회2(코드)===')

           if rows :
               for r in rows :
                  print("조회결과는 코드:",r[0], "품명:",r[1],"수량:", r[2],"단가:", r[3])
           else :
               print('해당 상품 없음 ') 
    
        except Exception as e :
            print('db 연동 error :', e)
            conn.rollback()

        finally:
           cursor.close()
           conn.close()

    
    def search_name(self):
        try:
           conn = pymysql.connect(**config)
           cursor = conn.cursor() 

           #요구사항 3
           print('<<<상품 개별 조회(상품명)입니다>>>')
           name = input("\n조회할 상품명 입력 : ")
           sql = f"select * from goods where name like  '%{name}%' "
           cursor.execute(sql)
           rows = cursor.fetchall()
        
           print('===goods 테이블조회2(상품명)===')
           if rows :
               for r in rows :
                    print("조회결과는 코드:",r[0], "품명:",r[1],"수량:", r[2],"단가:", r[3])
           else :
                print('해당 상품 없음 ') 
    
        except Exception as e :
            print('db 연동 error :', e)
            conn.rollback()

        finally:
            cursor.close()
            conn.close()
    

def delete_code():
    conn = pymysql.connect(**config)
    cursor = conn.cursor() 
    
    code = int(input('삭제할 코드 입력 :'))
    sql = f"select * from goods where code = {code}"
    cursor.execute(sql)
    rows = cursor.fetchall()

    if rows :
        sql = f"delete from goods where code = {code}"
        cursor.execute(sql)
        conn.commit()
        print('삭제 성공했습니다')
    else:
        print('삭제 실패했습니다')



if __name__ == "__main__":

    while True:
        os.system('cls')
        print("-----상품관리-----")
        print("상품 등록 : 1 ")
        print("상품목록조회: 2 ")
        print("코드별조회 : 3 ")
        print("상품명별조회 : 4 ")
        print("상품 수정 : 5 ")
        print("상품 삭제 : 6 ")
        print("상품관리종료 : 9 ")
        
        num = int(input("작업을 선택하세요 : "))
        if num == 1 : 
            register_code()
            os.system("pause")
        elif num == 2 : 
            search_all()
            os.system("pause")
        elif num == 3 :
            r1 = Search()
            r1.search_code()
            os.system("pause")    
        elif num == 4 :
            r2 = Search()
            r2.search_name()
            os.system("pause")
        elif num == 5 :
            print("상품수정기능은 준비중입니다. ")
            os.system("pause")
        elif num == 6 :
            search_all()
            delete_code()
            search_all()

            os.system("pause")
        elif num == 9 :
            break
        else:
            print("없는 기능입니다.")
            os.system("pause")