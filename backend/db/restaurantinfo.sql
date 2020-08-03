Dump of table user
# ------------------------------------------------------------
DROP TABLE IF EXISTS `restaurantInfo`;

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


insert into restaurantinfo (rid,ruid,rphone,raddr) values ('testrid','test',021234567,'testaddr');