import pymysql
print(pymysql.version_info)


config = {                  # MySQL데이터베이스를 사용하기 위해 환경변수를 딕셔너리로 생성함. 
'host' : '127.0.0.1',   # MySql 이 동작하는 ipv4주소 
'user' : 'user1',        # MySql 설치할 때 정한 계정 
'passwd' : '0000',  # MySql 설치할 때 정한 비밀번호
'database' : 'work', # MySql 설치할 때 처음 생성한 데이터베이스
'port' : 3306,          # MySql이 응용프로그램과 통신할 때 사용하는 포트번호 리터럴이 아닌 정수값으로 써야함
'charset' : 'utf8',     # 한글을 사용하겠다는 설정 
'use_unicode' : True    # 한글을 사용하겠다는 설정 
}


try :
    conn = pymysql.connect(**config)

    cursor = conn.cursor() 

    sql = "show tables"
    cursor.execute(sql)
    tables = cursor.fetchall()

    print(tables)


    if tables:
        print('table 있음')
    else:
        print('table 없음')

except Exception as e :
    print('db error :', e)

finally:
    cursor.close()
    conn.close()



