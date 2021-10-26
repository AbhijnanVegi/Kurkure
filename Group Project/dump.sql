-- MySQL dump 10.13  Distrib 5.7.35, for Linux (x86_64)
--
-- Host: localhost    Database: db
-- ------------------------------------------------------
-- Server version	5.7.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ADDRESS`
--

DROP TABLE IF EXISTS `ADDRESS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ADDRESS` (
  `UserEmailAddress` varchar(128) NOT NULL,
  `Line1` varchar(128) NOT NULL,
  `Line2` varchar(128) NOT NULL,
  `City` varchar(64) NOT NULL,
  `State` varchar(64) NOT NULL,
  `Zipcode` varchar(6) NOT NULL,
  PRIMARY KEY (`UserEmailAddress`,`Line1`,`Line2`),
  CONSTRAINT `ADDRESS_ibfk_1` FOREIGN KEY (`UserEmailAddress`) REFERENCES `USER` (`EmailAddress`) ON DELETE CASCADE ON UPDATE CASCADE 
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ADDRESS`
--

LOCK TABLES `ADDRESS` WRITE;
/*!40000 ALTER TABLE `ADDRESS` DISABLE KEYS */;
INSERT INTO `ADDRESS` VALUES ('Kurkure@iiit.ac.in','IIITH','Gachibowli','Hyderabad','Telangana','500075');
/*!40000 ALTER TABLE `ADDRESS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CARD`
--

DROP TABLE IF EXISTS `CARD`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CARD` (
  `UserEmailAddress` varchar(128) NOT NULL,
  `Name` varchar(64) NOT NULL,
  `CardNumber` varchar(20) NOT NULL,
  `ExpiryDate` varchar(5) NOT NULL,
  `NameOfCardHolder` varchar(64) NOT NULL,
  `BillingAddress` varchar(512) NOT NULL,
  PRIMARY KEY (`UserEmailAddress`,`Name`),
  CONSTRAINT `CARD_ibfk_1` FOREIGN KEY (`UserEmailAddress`, `Name`) REFERENCES `PAYMENT_METHOD` (`UserEmailAddress`, `Name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CARD`
--

LOCK TABLES `CARD` WRITE;
/*!40000 ALTER TABLE `CARD` DISABLE KEYS */;
INSERT INTO `CARD` VALUES ('Kurkure@iiit.ac.in','SBI Card','3004200280081010','12/22','Lays','IIITH Gachibowli');
/*!40000 ALTER TABLE `CARD` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CATEGORY`
--

DROP TABLE IF EXISTS `CATEGORY`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CATEGORY` (
  `ProductID` int(11) NOT NULL,
  `Category` varchar(64) NOT NULL,
  KEY `ProductID` (`ProductID`),
  CONSTRAINT `CATEGORY_ibfk_1` FOREIGN KEY (`ProductID`) REFERENCES `PRODUCT` (`ProductId`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CATEGORY`
--

LOCK TABLES `CATEGORY` WRITE;
/*!40000 ALTER TABLE `CATEGORY` DISABLE KEYS */;
INSERT INTO `CATEGORY` VALUES (1,'Snacks'),(2,'Snacks'),(2,'Breakfast');
/*!40000 ALTER TABLE `CATEGORY` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CONTAINS`
--

DROP TABLE IF EXISTS `CONTAINS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CONTAINS` (
  `OrderId` int(11) NOT NULL,
  `ProductId` int(11) NOT NULL,
  `Quantity` int(11) NOT NULL DEFAULT '1',
  KEY `FK_Order` (`OrderId`),
  KEY `FK_Product` (`ProductId`),
  CONSTRAINT `FK_Order` FOREIGN KEY (`OrderId`) REFERENCES `ORDERS` (`OrderId`) ON DELETE CASCADE,
  CONSTRAINT `FK_Product` FOREIGN KEY (`ProductId`) REFERENCES `PRODUCT` (`ProductId`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CONTAINS`
--

LOCK TABLES `CONTAINS` WRITE;
/*!40000 ALTER TABLE `CONTAINS` DISABLE KEYS */;
INSERT INTO `CONTAINS` VALUES (1,1,10),(1,2,5);
/*!40000 ALTER TABLE `CONTAINS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DELIVERY_AVAILABILITY`
--

DROP TABLE IF EXISTS `DELIVERY_AVAILABILITY`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DELIVERY_AVAILABILITY` (
  `ProductID` int(11) NOT NULL,
  `Location` varchar(64) NOT NULL,
  KEY `ProductID` (`ProductID`),
  CONSTRAINT `DELIVERY_AVAILABILITY_ibfk_1` FOREIGN KEY (`ProductID`) REFERENCES `PRODUCT` (`ProductId`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DELIVERY_AVAILABILITY`
--

LOCK TABLES `DELIVERY_AVAILABILITY` WRITE;
/*!40000 ALTER TABLE `DELIVERY_AVAILABILITY` DISABLE KEYS */;
INSERT INTO `DELIVERY_AVAILABILITY` VALUES (1,'Hyderabad'),(1,'Delhi'),(2,'Bangalore'),(2,'Chennai');
/*!40000 ALTER TABLE `DELIVERY_AVAILABILITY` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ORDERS`
--

DROP TABLE IF EXISTS `ORDERS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ORDERS` (
  `OrderId` int(11) NOT NULL AUTO_INCREMENT,
  `UserEmailAddress` varchar(128) NOT NULL,
  `AddressLine1` varchar(128) NOT NULL,
  `AddressLine2` varchar(128) NOT NULL,
  `PaymentName` varchar(64) NOT NULL,
  `OrderStatus` varchar(10) NOT NULL,
  `OrderDate` date NOT NULL,
  PRIMARY KEY (`OrderId`),
  KEY `FK_Address` (`UserEmailAddress`,`AddressLine1`,`AddressLine2`),
  KEY `FK_Payment` (`UserEmailAddress`,`PaymentName`),
  CONSTRAINT `FK_Address` FOREIGN KEY (`UserEmailAddress`, `AddressLine1`, `AddressLine2`) REFERENCES `ADDRESS` (`UserEmailAddress`, `Line1`, `Line2`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_Payment` FOREIGN KEY (`UserEmailAddress`, `PaymentName`) REFERENCES `PAYMENT_METHOD` (`UserEmailAddress`, `Name`) ON DELETE CASCADE,
  CONSTRAINT `FK_User` FOREIGN KEY (`UserEmailAddress`) REFERENCES `USER` (`EmailAddress`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ORDERS`
--

LOCK TABLES `ORDERS` WRITE;
/*!40000 ALTER TABLE `ORDERS` DISABLE KEYS */;
INSERT INTO `ORDERS` VALUES (1,'Kurkure@iiit.ac.in','IIITH','Gachibowli','SBI card','Placed','2021-10-19');
/*!40000 ALTER TABLE `ORDERS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PAYMENT_METHOD`
--

DROP TABLE IF EXISTS `PAYMENT_METHOD`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PAYMENT_METHOD` (
  `UserEmailAddress` varchar(128) NOT NULL,
  `Name` varchar(64) NOT NULL,
  `IsDefault` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`UserEmailAddress`,`Name`),
  CONSTRAINT `PAYMENT_METHOD_ibfk_1` FOREIGN KEY (`UserEmailAddress`) REFERENCES `USER` (`EmailAddress`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PAYMENT_METHOD`
--

LOCK TABLES `PAYMENT_METHOD` WRITE;
/*!40000 ALTER TABLE `PAYMENT_METHOD` DISABLE KEYS */;
INSERT INTO `PAYMENT_METHOD` VALUES ('JohnDoe@jd.com','JDPay',0),('Kurkure@iiit.ac.in','SBI Card',1);
/*!40000 ALTER TABLE `PAYMENT_METHOD` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PRODUCT`
--

DROP TABLE IF EXISTS `PRODUCT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PRODUCT` (
  `ProductId` int(11) NOT NULL,
  `Name` varchar(64) NOT NULL,
  `TotalQuantity` int(11) NOT NULL DEFAULT '0',
  `Price` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`ProductId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PRODUCT`
--

LOCK TABLES `PRODUCT` WRITE;
/*!40000 ALTER TABLE `PRODUCT` DISABLE KEYS */;
INSERT INTO `PRODUCT` VALUES (1,'Kurkure',10,10),(2,'Lays',20,30);
/*!40000 ALTER TABLE `PRODUCT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `REVIEW`
--

DROP TABLE IF EXISTS `REVIEW`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `REVIEW` (
  `ReviewId` int(11) NOT NULL AUTO_INCREMENT,
  `Review` varchar(512) DEFAULT NULL,
  `Rating` int(11) NOT NULL,
  PRIMARY KEY (`ReviewId`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `REVIEW`
--

LOCK TABLES `REVIEW` WRITE;
/*!40000 ALTER TABLE `REVIEW` DISABLE KEYS */;
INSERT INTO `REVIEW` VALUES (2,'Very nice snack',5);
/*!40000 ALTER TABLE `REVIEW` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `REVIEWSREL`
--

DROP TABLE IF EXISTS `REVIEWSREL`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `REVIEWSREL` (
  `UserEmailAddress` varchar(128) NOT NULL,
  `ProductId` int(11) NOT NULL,
  `OrderId` int(11) NOT NULL,
  `ReviewId` int(11) NOT NULL,
  KEY `fk_userrev` (`UserEmailAddress`),
  KEY `fk_productrev` (`ProductId`),
  KEY `fk_orderrev` (`OrderId`),
  KEY `fk_reviewrev` (`ReviewId`),
  CONSTRAINT `fk_orderrev` FOREIGN KEY (`OrderId`) REFERENCES `ORDERS` (`OrderId`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `fk_productrev` FOREIGN KEY (`ProductId`) REFERENCES `PRODUCT` (`ProductId`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `fk_reviewrev` FOREIGN KEY (`ReviewId`) REFERENCES `REVIEW` (`ReviewId`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `fk_userrev` FOREIGN KEY (`UserEmailAddress`) REFERENCES `USER` (`EmailAddress`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `REVIEWSREL`
--

LOCK TABLES `REVIEWSREL` WRITE;
/*!40000 ALTER TABLE `REVIEWSREL` DISABLE KEYS */;
INSERT INTO `REVIEWSREL` VALUES ('Kurkure@iiit.ac.in',1,1,2);
/*!40000 ALTER TABLE `REVIEWSREL` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `USER`
--

DROP TABLE IF EXISTS `USER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `USER` (
  `EmailAddress` varchar(128) NOT NULL,
  `FirstName` varchar(64) NOT NULL,
  `MiddleName` varchar(64) NOT NULL,
  `LastName` varchar(64) NOT NULL,
  `SubscriptionStatus` tinyint(1) NOT NULL DEFAULT '0',
  `MobileNumber` varchar(10) NOT NULL,
  PRIMARY KEY (`EmailAddress`),
  UNIQUE KEY `MobileNumber` (`MobileNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `USER`
--

LOCK TABLES `USER` WRITE;
/*!40000 ALTER TABLE `USER` DISABLE KEYS */;
INSERT INTO `USER` VALUES ('JohnDoe@jd.com','John','B','Doe',0,'1234567890'),('Kurkure@iiit.ac.in','Kurkure','Lays','Bingo',1,'1230985674');
/*!40000 ALTER TABLE `USER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `WALLET`
--

DROP TABLE IF EXISTS `WALLET`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `WALLET` (
  `UserEmailAddress` varchar(128) NOT NULL,
  `Name` varchar(64) NOT NULL,
  `Provider` varchar(64) NOT NULL,
  `AuthToken` varchar(128) NOT NULL,
  `Balance` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`UserEmailAddress`,`Name`),
  CONSTRAINT `WALLET_ibfk_1` FOREIGN KEY (`UserEmailAddress`, `Name`) REFERENCES `PAYMENT_METHOD` (`UserEmailAddress`, `Name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `WALLET`
--

LOCK TABLES `WALLET` WRITE;
/*!40000 ALTER TABLE `WALLET` DISABLE KEYS */;
INSERT INTO `WALLET` VALUES ('JohnDoe@jd.com','JDPay','Paytm','NkAxpzaQZaHjEuEA3InxsqqzoQBO20gWsQcC5rer6FR3Vl576mzHdm1YbzCMiX1HTNS6hyso0PFlLLcD4Hz2h93zddnB9LupyHh1dESs7wczNTEB6QvJo7RMc5cFGWY3',20388);
/*!40000 ALTER TABLE `WALLET` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-19 12:26:01
