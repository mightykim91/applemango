Dump of table user
# ------------------------------------------------------------
DROP TABLE IF EXISTS `restaurantInfo`;

CREATE TABLE `restaurantinfo` (
  `rid` int NOT NULL AUTO_INCREMENT,
  `ruid` varchar(31) NOT NULL,
  `rphone` varchar(31) NOT NULL,
  `raddr` varchar(124) DEFAULT NULL,
  `rimage` text DEFAULT NULL,
  `rname` varchar(31) NOT NULL,        
  `rbranch` varchar(31) DEFAULT NULL,
  `rdescription` varchar(124) DEFAULT NULL,
  `rcreatedate` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`rid`),
  FOREIGN KEY (`ruid`) REFERENCES `userinfo` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


insert into restaurantinfo (rid,ruid,rname,rphone,raddr) values (1,'test', 'testname','021234567','testaddr');
insert into restaurantinfo (rlat, rlng) values (37.525682, 127.027399) where restaurantinfo.rid = 1;