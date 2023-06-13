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
        if read_sel == '학번' :  #  read_sql : "select * from goods where code =" / "select * from goods where name ="
            self.read_sql = "select * from stud where studID ="
        elif read_sel == '학생이름' : 
            self.read_sql = "select * from stud where name ="
        else :
            self.read_sql = "select * from stud"

    def goodsModify(self) :
        try :
            conn = pymysql.connect(**config)    # 딕셔너리 config를 인수로 사용하여 conn 객체를 만듬.
            cursor = conn.cursor()   # conn 객체로부터 cursor() 메소드를 호출하여 cursor 참조변수를 만듬.
            print("<<<학번을 입력하세요>>>")
            in_studID = int(input('수정할 학번 입력 : '))
            sql = f"select * from stud where studID = {in_studID}"
            cursor.execute(sql) # sql문 실행 
            rows = cursor.fetchall()
            

            if rows :
                print('<<학번 조회결과입니다>>>')
                sql = f"select * from stud where studID = {in_studID}"
                print(rows)
                # os.system("pause")
                # print(f'{in_code}, ')
                YN = input("수정하시겠습니까?(y/n) :")
                if YN == 'y' or YN == 'Y':
                    in_name = input("학생이름을 입력하세요 : ") 
                    in_jumin1 = input("주민번호 앞자리를 입력하세요 : ")
                    in_jumin2 = input("주민번호 뒷자리를 입력하세요 : ")
  
                    sql = f"update stud set name = '{in_name}', jumin1 = {in_jumin1}, jumin2 = {in_jumin2} where studID = {in_studID}"
                    cursor.execute(sql) 
                    conn.commit()
                    print('수정을 완료했습니다.')
                    
                    print('<<<학생 수정 결과입니다>>>')
                    sql = f"select * from stud where studID = {in_studID}"
                    cursor.execute(sql) 
                    rows = cursor.fetchall()
                    print(rows)

                elif YN == 'n' or YN == 'N':
                    print('수정을 거절하셨습니다.')

                else:
                    print("y나 n을 입력하세요.")

            else :
                print('수정할 코드가 없습니다.')
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
            print("<<<삭제할 학번을 입력하세요>>>")
            in_studID = int(input('삭제할 코드 입력 : '))
            sql = f"select * from stud where studID = {in_studID}"
            cursor.execute(sql) # sql문 실행 
            rows = cursor.fetchall()
            if rows :
                # 레코드 1개 출력 : index 이용
                print('삭제 성공했습니다.')
                os.system("pause")
                sql = f"delete from stud where studID = {in_studID}"
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
                print("<<<학생 개별 조회({})입니다>>>".format(self.read_sel))
                in_studID = int(input("조회할"+self.read_sel+"를 입력하세요 : "))
                sql = self.read_sql + f"'{in_studID}'"
            elif self.read_sel == '학생이름' : 
                print("<<<학생 개별 조회({})입니다>>>".format(self.read_sel))
                in_studID = input("조회할"+self.read_sel+"를 입력하세요 : ")
                sql = self.read_sql + f"'{in_studID}'"
            else :
                #print("<<<상품 목록 조회결과입니다>>>")
                in_studID = ''
                sql = self.read_sql
            
            cursor.execute(sql)
            rows = cursor.fetchall()
            
            if self.read_sel == '학번' or self.read_sel == '학생이름' :
                if len(rows) > 0 :
                    print("===학생테이블 조회2({})===".format(self.read_sel))
                    for row in rows :
                        print("조회결과는 코드:{}, 품명:{}, 수량:{}, 단가:{}  입니다.".format(int(row[0]),row[1],int(row[2]),int(row[3])))
                else:
                    print("조회결과 입력한 {}에 맞는 상품이 없습니다".format(self.read_sel))
            else: # self.read_sel == 'all'일때
                if len(rows) > 0 :
                    print("<<<학생 목록 조회결과입니다>>>")
                    for row in rows :
                        print("{} {} {} {} ".format(int(row[0]),row[1],int(row[2]),int(row[3])))
                else:
                    print("조회결과 없습니다")           
        except Exception as e :
            print('db 연동 실패 : ', e)
            conn.rollback() # 실행 취소 
        finally:
            cursor.close()
            conn.close()
        


  

# def tableCreate() :
#     try :
#         print("----->")
#         conn = pymysql.connect(**config)
#         cursor = conn.cursor()
#         sql = """create table stud(
#             studID int primary key,
#             name varchar(30) not null,
#             su int default 0,
#             dan int default 0
#             )"""
#         cursor.execute(sql)
#         conn.commit()
#     except Exception as e :
#         print("오류 : ",e)
#         conn.rollback()
#     finally :
#         conn.close()
#         cursor.close()
def goodsCreate() :
    try :
        # (1) db 연동 객체 
        conn = pymysql.connect(**config)    # 딕셔너리 config를 인수로 사용하여 conn 객체를 만듬.
        # sql 실행 객체 
        cursor = conn.cursor()       # conn 객체로부터 cursor() 메소드를 호출하여 cursor 참조변수를 만듬.
        os.system('cls')
        print("<<<학생 등록입니다>>>")
        in_studID = int(input("학번을 입력하세요 : "))  #
        if in_studID > 0 :
            #print("------>>>>")
            sql = f"select * from stud where studID= {in_studID}"
            cursor.execute(sql)
            rows = cursor.fetchall()  # rows = [ (선풍기, 25, 14) ]
            if len(rows) > 0 :
                print("이미 존재하고 있습니다. 다른 코드를 입력하세요")
            else :
                in_name = input("학생이름을 입력하세요 : ") 
                in_jumin1 = input("주민번호 앞자리를 입력하세요 : ")
                in_jumin2 = input("주민번호 뒷자리를 입력하세요 : ")

                sql = f"insert into stud(studID,name) values({in_studID},'{in_name}', {in_jumin1}, {in_jumin2})" 
                cursor.execute(sql)
                rows = cursor.fetchall()
                conn.commit()
                print("학생등록을 성공했습니다.")
                print()
        else :
            print("학생 등록을 위해 학번을 입력해 주세요")
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
        print("<<<학생 목록 조회입니다>>>")
        cursor.execute("select * from stud")
        rows = cursor.fetchall()
        print("===학생 테이블 조회1===")
        print("(studID, name)")
        for row in rows :
            print(row)
    except Exception as e :
        print('db 연동 실패 : ', e)
        conn.rollback() # 실행 취소 
    finally:
        cursor.close()
        conn.close()




class filter :
    
    def filter_stud(self, studID):
        flag1_txt, flag2_txt = '', ''
        result = match('[0-9]{8}', studID)
        if len(studID[0:]) > 8 :
            flag1 = False  
            flag1_txt = '학번 길이오류/'
        else:
            flag1 = True
    #
        if 1900 <= int(studID[0:4]) <= 2023 :
            flag2 = True
        else:
            flag2 = False
            flag2_txt = '학번 입학년도 오류/'
    #
        if 1 <= int(studID[4:6]) <= 99 :
            flag2 = True
        else:
            flag2 = False
            flag2_txt = '학번 입학월 오류/'

        if 1 <= int(studID[6:]) <= 99 :
            flag2 = True
        else:
            flag2 = False
            flag2_txt = '학번 입학날짜 오류/'


    #
        # if flag2 == True and year_st == '평년':
        #     if month[int(studID[2:4])-1] < int(studID[4:6]):
        #         flag4 = False
        #         flag4_txt = '주민번호 앞자리 월 오류/'
        #     else:
        #         flag4 = True
           
        # if flag2 == True and year_st == '윤년':
        #     if month[int(studID[2:4])-1] < int(studID[4:6]):
        #         flag4 = False
        #         flag4_txt = '주민번호 앞자리 월 오류/'
        #     else:
        #         flag4 = True
    #
    # 함수의 역할을 끝내고 리턴할 값을 만듬
        return_txt = ''
        if result and flag1 and flag2 :
            return studID+'-->','정상적인 학번'
        else :
            return_txt += flag1_txt + flag2_txt 
            return studID+'-->', '비정상적인 학번 : '+ return_txt



def jumin_chk(jumin) :
    #
    flag1_txt, flag2_txt, flag3_txt = '', '', ''
    result = match('[0-9]{6}-[1-4][0-9]{6}', jumin)
    if len(jumin[0:]) > 14 :
        flag1 = False  
        flag1_txt = '주민번호 길이오류/'
    else:
        flag1 = True
    #
    if 1 <= int(jumin[2:4]) <= 12 :
        flag2 = True
    else:
        flag2 = False
        flag2_txt = '주민번호 앞자리 월 오류/'
    #
    if len(jumin[7:]) > 7 :
        flag3 = False
        flag3_txt = '주민번호 뒷자리 길이오류/'
    else:
        flag3 = True
    # 함수의 역할을 끝내고 리턴할 값을 만듬
    return_txt = ''
    if result and flag1 and flag2 and flag3 :
        return jumin+'-->' + '정상적인 주민번호'
    else :
        return_txt += flag1_txt + flag2_txt + flag3_txt 
        return jumin+'-->' + '비정상적인 주민번호 : '+ return_txt



if __name__ == "__main__" :
    #tableCreate()
    while True:
        os.system('cls')
        print("---학생관리---")
        print("학생    등록 : 1 ")
        print("학생    조회 : 2 ")
        print("학반별  조회 : 3 ")
        print("학생이름별조회 : 4 ")
        print("학생    수정 : 5 ")
        print("학생    삭제 : 6 ")
        print("학생관리종료 : 9 ")
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
            print("상품관리를 종료합니다. ")
            os.system("pause")
            os.system('cls')
            sys.exit(0)
        else :
            print("잘못 선택했습니다. ")
            os.system("pause")