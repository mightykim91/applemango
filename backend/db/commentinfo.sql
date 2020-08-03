Dump of table user
# ------------------------------------------------------------
DROP TABLE IF EXISTS `commentinfo`;

CREATE TABLE `commentinfo` (
  `cmid` INT NOT NULL AUTO_INCREMENT,
  `cmreid` INT NOT NULL,
  `cmuid` varchar(31) NOT NULL,
  `cmcontent` varchar(200) DEFAULT NULL,
  `cmcreateddate` DATETIME DEFAULT current_timestamp(),
  `cmmodifieddate` DATETIME DEFAULT current_timestamp(),
  PRIMARY KEY (`cmid`),
  FOREIGN KEY (`cmreid`) REFERENCES `reviewinfo` (`reid`),
  FOREIGN KEY (`cmuid`) REFERENCES `userinfo` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into commentinfo(cmreid, cmuid, cmcontent) values (1,'test','test comment');
