Dump of table user
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

insert into menu (mrid, missig, mname, mprice) values (1, false, 'kimbab',2500);

