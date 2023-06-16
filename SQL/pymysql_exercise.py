import pymysql
# print(pymysql.version_info)


config = {                
'host' : '127.0.0.1',  
'user' : 'user1',     
'passwd' : '0000',  
'database' : 'test_db', 
'port' : 3306,       
'charset' : 'utf8',     
'use_unicode' : True    
}

# 요구사항별로 하나씩 실행. 사용안할 요구사항은 주석처리후 run
try:
    conn = pymysql.connect(**config)
    cursor = conn.cursor() 

    sql = 'create table if not exists tb1(name varchar(20), age int, num int)'
    cursor.execute(sql)

    #요구사항 1
    name = input('이름 입력 : ') 
    age = int(input('나이 입력 : '))
    num = int(input('수량 입력 : '))
    sql = f"insert into tb1 values('{name}', {age}, {num})"
    cursor.execute(sql)
    conn.commit()
    print('===회원등록===')
    print(f"이름 입력: {name}\n나이 입력: {age}\n수량 입력: {num}")
    print('회원등록을 성공했습니다.')


    #요구사항 2
    sql = "select * from tb1"
    cursor.execute(sql)
    rows = cursor.fetchall()
    print('---tb1 테이블 조회---')
    print('NAME, AGE, NUM')
    for row in rows :
        print(row[0], row[1], row[2])


    
    #요구사항 3
    name = input("조회할 이름 입력하세요 : ")
    sql = f"select * from tb1 where name like  '%{name}%' "
    cursor.execute(sql)
    rows = cursor.fetchall()
    print('===회원조회2===')
    #print(f'조회할 이름 입력하세요 : {name}')
    if rows :
        for row in rows :
            print('조회결과는 이름 :', row[0], '나이 :', row[1],
                  '수량 :', row[2])
    else :
        print('조회결과 입력한 코드에 맞는 회원이 없습니다.') 


except Exception as e :
    print('db 연동 error :', e)
    conn.rollback()

finally:
    cursor.close()
    conn.close()