import os
import sys
import pymysql # MySQL데이터베이스를 사용하기 위한 라이브러리를 등록함


config = {                
'host' : '127.0.0.1',  
'user' : 'user1',     
'passwd' : '0000',  
'database' : 'test_db', 
'port' : 3306,       
'charset' : 'utf8',     
'use_unicode' : True    
}



class GoodsRead :

    def __init__(self,read_sel): # 생성자 : read_sel : 코드/상품명/all ,            
        self.read_sel = read_sel
        if read_sel == '과목코드' :  #  read_sql : "select * from goods where code =" / "select * from goods where name ="
            self.read_sql = "select * from course where courseID ="
        elif read_sel == '과목명' : 
            self.read_sql = "select * from course where CourseName ="
        else :
            self.read_sql = "select * from course"

    def goodsModify(self) :
        try :
            conn = pymysql.connect(**config)    # 딕셔너리 config를 인수로 사용하여 conn 객체를 만듬.
            cursor = conn.cursor()   # conn 객체로부터 cursor() 메소드를 호출하여 cursor 참조변수를 만듬.
            print("<<<과목코드를 입력하세요>>>")
            in_courseID = int(input('수정할 과목코드 입력 : '))
            sql = f"select * from course where courseID = {in_courseID}"
            cursor.execute(sql) # sql문 실행 
            rows = cursor.fetchall()
            

            if rows :
                print('<<과목코드 조회결과입니다>>>')
                sql = f"select * from course where courseID = {in_courseID}"
                print(rows)
                # os.system("pause")
                # print(f'{in_code}, ')
                YN = input("수정하시겠습니까?(y/n) :")
                if YN == 'y' or YN == 'Y':
                    in_CourseName = input("과목명을 입력하세요 : ") 
                    
  
                    sql = f"update course set CourseName = '{in_CourseName}' where courseID = {in_courseID}"
                    cursor.execute(sql) 
                    conn.commit()
                    print('수정을 완료했습니다.')
                    
                    print('<<<학생 수정 결과입니다>>>')
                    sql = f"select * from course where courseID = {in_courseID}"
                    cursor.execute(sql) 
                    rows = cursor.fetchall()
                    print(rows)

                elif YN == 'n' or YN == 'N':
                    print('수정을 거절하셨습니다.')

                else:
                    print("y나 n을 입력하세요.")

            else :
                print('수정할 과목코드가 없습니다.')
                os.system("pause")


        except Exception as e :
            print('db 연동 실패 : ', e)
            conn.rollback() # 실행 취소 
        finally:
            cursor.close()
            conn.close()


    def goodsDelete(self) :
        try :
            conn = pymysql.connect(**config)    # 딕셔너리 config를 인수로 사용하여 conn 객체를 만듬.
            cursor = conn.cursor()   # conn 객체로부터 cursor() 메소드를 호출하여 cursor 참조변수를 만듬.
            print("<<<삭제할 과목코드 입력하세요>>>")
            in_courseID = int(input('삭제할 코드 입력 : '))
            sql = f"select * from course where courseID = {in_courseID}"
            cursor.execute(sql) # sql문 실행 
            rows = cursor.fetchall()
            if rows :
                # 레코드 1개 출력 : index 이용
                print('삭제 성공했습니다.')
                os.system("pause")
                sql = f"delete from course where courseID = {in_courseID}"
                cursor.execute(sql) # sql문 실행
                conn.commit()
            else :
                print('삭제 실패했습니다.')
                os.system("pause")
        except Exception as e :
            print('db 연동 실패 : ', e)
            conn.rollback() # 실행 취소 
        finally:
            cursor.close()
            conn.close()


    def goodsReadOne(self) :
        try :
            # (1) db 연동 객체 
            conn = pymysql.connect(**config)    # 딕셔너리 config를 인수로 사용하여 conn 객체를 만듬.
            # sql 실행 객체 
            cursor = conn.cursor()     # conn 객체로부터 cursor() 메소드를 호출하여 cursor 참조변수를 만듬.
            # (3) 단일 레코드 조회  
            rows = []
            os.system('cls')
            
            if self.read_sel == '학번' :
                print("<<<과목 개별 조회({})입니다>>>".format(self.read_sel))
                in_coursedID = int(input("조회할"+self.read_sel+"를 입력하세요 : "))
                sql = self.read_sql + f"'{in_courseID}'"
            elif self.read_sel == '학생이름' : 
                print("<<<과목 개별 조회({})입니다>>>".format(self.read_sel))
                in_courseID = input("조회할"+self.read_sel+"를 입력하세요 : ")
                sql = self.read_sql + f"'{in_courseID}'"
            else :
                #print("<<<상품 목록 조회결과입니다>>>")
                in_courseID = ''
                sql = self.read_sql
            
            cursor.execute(sql)
            rows = cursor.fetchall()
            
            if self.read_sel == '과목코드' or self.read_sel == '과목명' :
                if len(rows) > 0 :
                    print("===과목테이블 조회2({})===".format(self.read_sel))
                    for row in rows :
                        print("조회결과는 과목코드:{}, 과목명:{}  입니다.".format(int(row[0]),row[1]))
                else:
                    print("조회결과 입력한 {}에 맞는 상품이 없습니다".format(self.read_sel))
            else: # self.read_sel == 'all'일때
                if len(rows) > 0 :
                    print("<<<과목명 목록 조회결과입니다>>>")
                    for row in rows :
                        print("{} {}".format(int(row[0]),row[1]))
                else:
                    print("조회결과 없습니다")           
        except Exception as e :
            print('db 연동 실패 : ', e)
            conn.rollback() # 실행 취소 
        finally:
            cursor.close()
            conn.close()
        


def goodsCreate() :
    try :
        # (1) db 연동 객체 
        conn = pymysql.connect(**config)    # 딕셔너리 config를 인수로 사용하여 conn 객체를 만듬.
        # sql 실행 객체 
        cursor = conn.cursor()       # conn 객체로부터 cursor() 메소드를 호출하여 cursor 참조변수를 만듬.
        os.system('cls')
        print("<<<과목 등록입니다>>>")
        in_courseID = int(input("과목코드을 입력하세요 : "))  #
        if in_courseID > 0 :
            #print("------>>>>")
            sql = f"select * from course where courseID= {in_courseID}"
            cursor.execute(sql)
            rows = cursor.fetchall()  # rows = [ (선풍기, 25, 14) ]
            if len(rows) > 0 :
                print("이미 존재하고 있습니다. 다른 코드를 입력하세요")
            else :
                in_CourseName = input("과목명을 입력하세요 : ") 

                sql = f"insert into course(courseID, CourseName) values({in_courseID},'{in_CourseName}')" 
                cursor.execute(sql)
                rows = cursor.fetchall()
                conn.commit()
                print("과목등록을 성공했습니다.")
                print()
        else :
            print("과목 등록을 위해 과목코드를 입력해 주세요")
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
        print("<<<과목 목록 조회입니다>>>")
        cursor.execute("select * from course")
        rows = cursor.fetchall()
        print("===과목 테이블 조회1===")
        print("(courseID, CourseName)")
        for row in rows :
            print(row)
    except Exception as e :
        print('db 연동 실패 : ', e)
        conn.rollback() # 실행 취소 
    finally:
        cursor.close()
        conn.close()




if __name__ == "__main__" :
    #tableCreate()
    while True:
        os.system('cls')
        print("---과목관리---")
        print("과목    등록 : 1 ")
        print("과목    조회 : 2 ")
        print("과목코드 조회 : 3 ")
        print("과목명  조회 : 4 ")
        print("과목    수정 : 5 ")
        print("과목    삭제 : 6 ")
        print("과목관리종료 : 9 ")
        sel = int(input("작업을 선택하세요 : "))
        if sel == 1 :
            goodsCreate()
            os.system("pause")
        elif sel == 2 :
            goodsReadAll()
            os.system("pause")
        elif sel == 3 :
            r1 = GoodsRead('학번')
            r1.goodsReadOne()
            os.system("pause")
        elif sel == 4 :
            r2 = GoodsRead('학생이름')
            r2.goodsReadOne()
            os.system("pause")
        elif sel == 5 :
            r3 = GoodsRead('all')
            r3.goodsModify()
            os.system("pause")
        elif sel == 6 :
            #print("상품삭제기능은 준비중입니다. ")
            r4 = GoodsRead('all')
            r4.goodsReadOne()
            r4.goodsDelete()
            r4.goodsReadOne()
            os.system("pause")
        elif sel == 9 :
            print("과목관리를 종료합니다. ")
            os.system("pause")
            os.system('cls')
            sys.exit(0)
        else :
            print("잘못 선택했습니다. ")
            os.system("pause")