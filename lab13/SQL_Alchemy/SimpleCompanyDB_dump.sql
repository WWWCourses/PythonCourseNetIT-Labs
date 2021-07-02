/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;

DROP DATABASE IF EXISTS SimpleCompanyDB;
CREATE DATABASE SimpleCompanyDB;

use SimpleCompanyDB;

CREATE TABLE `company` (
  `company_id` int(11) NOT NULL AUTO_INCREMENT,
  `company_name` varchar(300) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;
INSERT INTO `company` VALUES (1,'Google');
INSERT INTO `company` VALUES (2,'Facebook');

INSERT INTO `company` VALUES (3,'Microsoft');
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;

CREATE TABLE `employee` (
  `employee_id` int(11) NOT NULL AUTO_INCREMENT,
  `employee_name` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;
INSERT INTO `employee` VALUES (1,'Ivan Petrov');
INSERT INTO `employee` VALUES (2,'Maria Popova');
INSERT INTO `employee` VALUES (3,'Asen Asenov');

CREATE TABLE `company_employee` (
  `employee_id` int(11) NOT NULL,
  `company_id` int(11) NOT NULL,
  PRIMARY KEY (`employee_id`,`company_id`),
  KEY `company_id` (`company_id`),
  CONSTRAINT `company_employee_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`employee_id`) ON UPDATE CASCADE,
  CONSTRAINT `company_employee_ibfk_2` FOREIGN KEY (`company_id`) REFERENCES `company` (`company_id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;
INSERT INTO `company_employee` VALUES (1,2);
INSERT INTO `company_employee` VALUES (2,1);
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;

