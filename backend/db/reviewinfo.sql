DROP TABLE IF EXISTS `reviewinfo`;

CREATE TABLE `reviewinfo` (
  `reid` INT NOT NULL AUTO_INCREMENT,
  `reuid` varchar(31) NOT NULL, 
  `rerid` INT(11) NOT NULL, 
  `recreateddate` datetime DEFAULT current_timestamp(),
  `remodifieddate` datetime DEFAULT current_timestamp(),
  `rerating` Integer NOT NULL,
  `retitle` varchar(31) NOT NULL,
  `redescription` varchar(200) NOT NULL,
  PRIMARY KEY (`reid`),
  FOREIGN KEY (`rerid`) REFERENCES `restaurantinfo` (`rid`),
  FOREIGN KEY (`reuid`) REFERENCES `userinfo` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into reviewinfo(reuid, rerid, rerating, retitle, redescription) values('test',1,5,'test title','test description');

