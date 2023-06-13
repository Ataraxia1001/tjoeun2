CREATE TABLE IF NOT EXISTS stud (
  studID CHAR(8),
  name VARCHAR(20),
  jumin1 CHAR(6),
  jumin2 CHAR(7),
  addr1 VARCHAR(20),
  addr2 VARCHAR(20)
);


INSERT INTO stud VALUES
('20180101', '홍길동', '200229', '3234567', '서울시', '서대1구'),
('20180102', '이순신', '720229', '1234567', '수원시', '서대2구'),
('20180103', '강감찬', '781212', '1328399', '강릉시', '서대3구'),
('20190101', '이성계', '790307', '2262722', '부산시', '서대4구'),
('20190102', '을지문덕', '780618', '2258211', '대구시', '서대5구'),
('20190103', '연개소문', '771009', '2215327', '울산시', '서대6구'),
('20190104', '안중근', '780209', '1573216', '이천시', '서대7구'),
('20200101', '김구', '770515', '2024213', '동두천시', '서대8구'),
('20200102', '정도전', '800613', '1078166', '대전시', '서대9구'),
('20200103', '이황', '720711', '2024219', '세종시', '서대10구');




CREATE TABLE IF NOT EXISTS course (
  courseID CHAR(2),
  CourseName VARCHAR(10)
);

INSERT INTO course VALUES ('01', '국어');
INSERT INTO course VALUES ('02', '영어');
INSERT INTO course VALUES ('03', '수학');




CREATE TABLE IF NOT EXISTS score (
  studID CHAR(8),
  CourseID VARCHAR(10),
  score INT(03)
);


DELETE FROM score;

INSERT INTO score (studID)
SELECT studID
FROM stud;



INSERT INTO score (CourseID)
SELECT courseID
FROM course;





