Dump of table user
# ------------------------------------------------------------
DROP TABLE IF EXISTS `RestaurantRegisterRequests`;

CREATE TABLE `RestaurantRegisterRequests` (
  `id` int NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `user_id` varchar(31) NOT NULL,
  `restaurant_info` JSON,
  FOREIGN KEY (`user_id`) REFERENCES `userinfo` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


INSERT INTO RestaurantRegisterRequests(user_id, restaurant_info)
VALUES('test', json_object(
"phoneNumber","010-0000-0000",
"address","multicampus",
"name","multicafe",
"branch","yeoksam"
));