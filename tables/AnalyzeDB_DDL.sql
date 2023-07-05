CREATE TABLE `Event`
(
 `start_time`   timestamp NOT NULL ,
 `user_ip`      varchar NOT NULL ,
 `type`         varchar NOT NULL ,
 `cursor_x_pos` integer NOT NULL ,
 `cursor_y_pos` integer NOT NULL ,
 `end_time`     timestamp NOT NULL ,

PRIMARY KEY (`start_time`, `user_ip`),
KEY `FK_1` (`user_ip`),
CONSTRAINT `FK_2` FOREIGN KEY `FK_1` (`user_ip`) REFERENCES `User` (`ip`)
);

CREATE TABLE `User`
(
 `ip`       varchar(20) NOT NULL ,
 `agent`    varchar(50) NOT NULL ,
 `location` varchar(50) NOT NULL ,

PRIMARY KEY (`ip`)
);
