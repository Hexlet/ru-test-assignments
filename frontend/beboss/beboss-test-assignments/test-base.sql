SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

CREATE TABLE IF NOT EXISTS `groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_parent` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=11 ;

INSERT INTO `groups` (`id`, `id_parent`, `name`) VALUES
(1, 0, 'Телевизоры'),
(2, 0, 'Мультимедиа'),
(3, 1, 'ЖК телевизоры'),
(4, 1, 'Плазменные телевизоры'),
(5, 3, 'Диагональю до 45 дюймов'),
(6, 3, 'Диагональю более 40 дюймов'),
(7, 4, 'Диагональю до 45 дюймов'),
(8, 4, 'Диагональю более 40 дюймов'),
(9, 2, 'DVD-плееры'),
(10, 2, 'Blu-Ray плееры');

CREATE TABLE IF NOT EXISTS `products` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_group` int(11) NOT NULL DEFAULT '0',
  `name` varchar(250) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_group` (`id_group`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=18 ;

INSERT INTO `products` (`id`, `id_group`, `name`) VALUES
(1, 9, 'DVD-плеер BBK DVP 753HD'),
(2, 9, 'DVD-плеер BBK DVP 953HD'),
(3, 9, 'DVD-плеер BBK DMP1024HD (+ 3 DVD диска)'),
(4, 2, 'Магнитола HYUNDAI H-1404'),
(5, 10, 'Blu-ray плеер PHILIPS DVP3700 (51)'),
(6, 8, 'Плазменный телевизор LG 50PZ250 (3D)'),
(7, 8, 'Плазменный телевизор Samsung PS51D450'),
(8, 7, 'Плазменный телевизор LG 42PT250'),
(9, 7, 'Плазменный телевизор LG 42PW451 (3D)'),
(10, 4, 'Плазменный телевизор LG 50PZ551 (3D)'),
(11, 5, 'Телевизор-ЖК LG 26LK330'),
(12, 5, 'Телевизор-ЖК Fusion FLTV-16W7'),
(13, 6, 'Телевизор-ЖК LG 42LK530'),
(14, 6, 'Телевизор-ЖК LG 42LK551'),
(15, 6, 'Телевизор-ЖК LG 47LK530'),
(16, 3, 'Телевизор-ЖК Samsung LE32D403'),
(17, 1, 'Телевизор Erisson 1435');
