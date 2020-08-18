
# -*- coding: utf-8 -*-
# ko_search = ['알밥','비빔밥','비빔면','보쌈','불고기','닭갈비', '닭볶음탕', '된장찌개', '돈까스', '두부김치', '갈비', '갈비찜', '갈치구이', '김밥', '김치볶음밥', '김치전', '김치찌개', '곱창', '계란후라이', '계란찜', '계란말이', '호박전', '후라이드치킨', '훈제오리', '잔치국수', '장어구이', '제육볶음', '짜장면', '짬뽕', '쫄면', '쭈구미볶음', '조개구이', '족발', '조기구이', '주먹밥', '칼국수', '콩국수', '콩나물국밥', '라면','막국수', '만두', '미역국', '물회', '물냉면','오징어튀김' ,'파스타','피자', '생선구이', '새우볶음밥', '새우튀김', '삼겹살', '삼계탕' ,'산낙지', '설렁탕','수제비','순대', '순대국밥', '탕수육', '떡볶이','떡국', '우동', '양념치킨','유부초밥', '육회'] 
# en_search = ['albab', 'bibimbab', 'bibimnaengmyeon', 'bossam', 'bulgogi', 'dalg-galbi', 'dalgbokk-eumtang', 'doenjangjjigae', 'donkkaseu', 'dubugimchi', 'galbi', 'galbijjim', 'galchigu-i', 'gimbab', 'gimchibokk-eumbab', 'gimchijeon', 'gimchijjigae', 'gobchang', 'gyelanhulai', 'gyelanjjim', 'gyelanmal-i', 'hobagjeon', 'hulaideuchikin', 'hunje-oli', 'janchigugsu', 'jang-eogu-i', 'jeyugbokk-eum', 'jjajangmyeon', 'jjamppong', 'jjolmyeon', 'jjukkumibokk-eum', 'jogaegu-i', 'jogbal', 'jogigu-i', 'jumeogbab', 'kalgugsu', 'kong-gugsu', 'kongnamulgug', 'lamyeon', 'maggugsu', 'mandu', 'miyeoggug', 'mulhoe', 'mulnaengmyeon', 'ojing-eotwigim', 'paseuta', 'pija', 'saengseonjeon', 'saeubokk-eumbab', 'saeutwigim', 'samgyeobsal', 'samgyetang', 'sannagji', 'seolleongtang', 'sujebi', 'sundae', 'sundaegugbab', 'tangsuyug', 'tteogbokk-i', 'tteoggug', 'udong', 'yangnyeomchikin', 'yubuchobab', 'yughoe']

# for row in ko_search:
#     print(row, end= " ")
# print()
# for row in en_search:
#     print(row, end= " ")
import mariadb
import sys
import json
# name = input('로드할 json 파일명을 작성해주세요: ')
# with open(name+'.json', 'r', encoding='UTF-8') as f:
#     data = json.load(f)
# Connect to MariaDB Platform

# DB와 python connect
uinstagramid = ""
try:
  conn = mariadb.connect(
      host = "i3a503.p.ssafy.io",
      user = "root", 
      password = "mariadb",
      database = "subpjt2",
      # port=3306,
    )
  # print(conn) # 연결 확인용
except mariadb.Error as e:
  print(f"Error connecting to MariaDB Platform: {e}")
  sys.exit(1)
# Get Cursor
cur = conn.cursor()

def SELECT():
  try:
    # ALTER TABLE TABLE_NAME CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    # sql = "SELECT * FROM userinfo WHERE uinstagramid ='" + ("%s" % uinstagramid) + "'"
    sql = "SELECT * FROM instagrampictures"
    # print(sql)
    cur.execute(sql)
    resultList = cur.fetchall()
    for res in resultList:
      print(res)
      
    # print(len(resultList))
    if len(resultList) > 0:
      return False
    else:
      return True
  except:
    print("SELECT 과정에서 에러 발생")

# insert information 
def INSERT(data):
    try: 
      for i in range(len(data)):
        add = tuple(data[i].values())
        # print(add)
        try:
          cur.execute("INSERT INTO instagrampictures (irid, rname, rbranch, instaid, iurl, likes, idate) VALUES (?,?,?,?,?,?,?)", add) 
        except:
          print('데이터 Insert중 Incorrect string value 발생')

    except mariadb.Error as e: 
        print(f"Error: {e}")
    # print(cur.rowcount, "record inserted")



# select information 
SELECT()

# insert information 
# INSERT()

# conn.close()


'''

CREATE TABLE `userinfo` (
  `uid` varchar(31) NOT NULL,
  `upw` varchar(31) NOT NULL,
  `ukind` Integer DEFAULT 0,
  `uname` varchar(31) NOT NULL,
  `uemail` varchar(31) DEFAULT NULL,
  `uphone` varchar(31) DEFAULT NULL,
  `uaddr` varchar(100) DEFAULT NULL,
  `uinstagramid` varchar(31) DEFAULT NULL,
  `ucreatedate` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`uid`),
  UNIQUE KEY `user_idx_unique_email` (`uemail`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into userinfo (uid,upw,ukind,uname,uemail) values ('test','test',0,'test','test@test');




# ------------------------------------------------------------
DROP TABLE IF EXISTS `restaurantinfo`;

CREATE TABLE `restaurantinfo` (
  `rid` int NOT NULL AUTO_INCREMENT,
  `ruid` varchar(31) NOT NULL,
  `rphone` varchar(31) NOT NULL,
  `raddr` varchar(124) DEFAULT NULL,
  `rname` varchar(31) NOT NULL,        ## 해시태그 가게 이름 매칭
  `rbranch` varchar(31) DEFAULT NULL, ## 해시태그 가게 지점(ex강남점) 매칭
  `rlat` DECIMAL(13,10) DEFAULT NULL,
  `rlng` DECIMAL(13,10) DEFAULT NULL,
  `rdescription` varchar(124) DEFAULT NULL,
  `rcreatedate` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`rid`),
  FOREIGN KEY (`ruid`) REFERENCES `userinfo` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into restaurantinfo (ruid,rphone,raddr,rname,rbranch) values ('test','testphone','testraddr','testrname','testrbranch');




# ------------------------------------------------------------
DROP TABLE IF EXISTS `instagrampictures`;

CREATE TABLE `instagrampictures` (
  `iid`   int NOT NULL AUTO_INCREMENT,
  `irid` int NOT NULL ,
  `rname` varchar(31) NOT NULL,        ## 해시태그 가게 이름 매칭
  `rbranch` varchar(31) DEFAULT NULL, ## 해시태그 가게 지점(ex강남점) 매칭
  `instaid` varchar(31) NOT NULL,
  `iurl` text DEFAULT NULL,
  `likes` int DEFAULT NULL,
  `idate`  datetime,             ## 시간정보 삭제하고 날짜정보만
  PRIMARY KEY (`iid`),
  FOREIGN KEY (`irid`) REFERENCES `restaurantinfo` (`rid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into instagrampictures (irid,rname,rbranch,instaid,iurl,likes,idate) values (1,'testrname','testrbranch','testinstaid','https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-15/e35/s1080x1080/107396930_1589599847869482_8655103234598366724_n.jpg?_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_cat=106&_nc_ohc=ylWRqtJ0NRgAX_2TwEw&oh=829d3921e44510367bfcac23fcff962b&oe=5F4AEC7B',15,now());

insert into instagrampictures (irid,rname,rbranch,instaid,iurl,likes,idate) values (1,'testrname','testrbranch','testinstaid2','https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDAyMDFfMjA5%2FMDAxNTgwNTQwOTY2Mjcz.LMyCyyj37xjvk5LSwd8mTXid4Ecn2pBNzCSXkHDrhSEg.EWaazjkNAlFNnVk6q5rxPLtqKqcX7fuPsCGgrhselv4g.JPEG.jdw124%2F0O0A9579.jpg&type=b400
',6,now());

# ------------------------------------------------------------
DROP TABLE IF EXISTS `menu`;

CREATE TABLE `menu` (
  `mid` int NOT NULL AUTO_INCREMENT,
  `mrid` int NOT NULL,
  `missig` boolean DEFAULT NULL,
  `mname` varchar(31) NOT NULL,
  `mprice` Integer NOT NULL,
  `mimage` text DEFAULT NULL,
  PRIMARY KEY (`mid`),
  FOREIGN KEY (`mrid`) REFERENCES `restaurantinfo` (`rid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into menu (mrid,missig,mname,mprice) values (1,true,'kimbab',2500);
insert into menu (mrid,missig,mname,mprice) values (1,false,'testmname',15500);


'''