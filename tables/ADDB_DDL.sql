CREATE TABLE `Slot`
(
 `id`     integer NOT NULL ,
 `ad_num` integer NOT NULL ,

PRIMARY KEY (`id`)
);


CREATE TABLE `AD`
(
 `id`           integer NOT NULL ,
 `uri`          varchar(50) NOT NULL ,
 `size`         integer NOT NULL ,
 `target_link`  varchar(50) NOT NULL ,
 `content_type` varchar(20) NOT NULL ,
 `slot_id`      integer NOT NULL ,

PRIMARY KEY (`id`),
KEY `FK_1` (`slot_id`),
CONSTRAINT `FK_3` FOREIGN KEY `FK_1` (`slot_id`) REFERENCES `Slot` (`id`)
);

CREATE TABLE `Advertiser`
(
 `id`    integer NOT NULL ,
 `name`  varchar(20) NOT NULL ,
 `phone` varchar(20) NOT NULL ,

PRIMARY KEY (`id`)
);

CREATE TABLE `AD_contract`
(
 `ad_id`         integer NOT NULL ,
 `advertiser_id` integer NOT NULL ,
 `price`         integer NOT NULL ,
 `start_date`    timestamp NOT NULL ,
 `end_date`      timestamp NOT NULL ,

PRIMARY KEY (`ad_id`),
KEY `FK_4` (`advertiser_id`),
CONSTRAINT `FK_4` FOREIGN KEY `FK_4` (`advertiser_id`) REFERENCES `Advertiser` (`id`),
KEY `FK_2` (`ad_id`),
CONSTRAINT `FK_2` FOREIGN KEY `FK_2` (`ad_id`) REFERENCES `AD` (`id`)
);
