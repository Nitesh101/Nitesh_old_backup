-- MySQL dump 10.13  Distrib 5.7.18, for Linux (x86_64)
--
-- Host: localhost    Database: DM_Testing
-- ------------------------------------------------------
-- Server version	5.7.18-0ubuntu0.16.04.1

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
-- Table structure for table `DM_Discover`
--

DROP TABLE IF EXISTS `DM_Discover`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DM_Discover` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `R_Name` varchar(200) DEFAULT NULL,
  `Handle` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DM_Discover`
--

LOCK TABLES `DM_Discover` WRITE;
/*!40000 ALTER TABLE `DM_Discover` DISABLE KEYS */;
/*!40000 ALTER TABLE `DM_Discover` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DM_GET`
--

DROP TABLE IF EXISTS `DM_GET`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DM_GET` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Resource_Name` varchar(100) DEFAULT NULL,
  `Handle` varchar(200) DEFAULT NULL,
  `Key1` varchar(100) DEFAULT NULL,
  `Value` varchar(600) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DM_GET`
--

LOCK TABLES `DM_GET` WRITE;
/*!40000 ALTER TABLE `DM_GET` DISABLE KEYS */;
/*!40000 ALTER TABLE `DM_GET` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DM_Observe`
--

DROP TABLE IF EXISTS `DM_Observe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DM_Observe` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Resource_Name` varchar(100) DEFAULT NULL,
  `Handle` varchar(200) DEFAULT NULL,
  `Key1` varchar(100) DEFAULT NULL,
  `Value` varchar(600) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DM_Observe`
--

LOCK TABLES `DM_Observe` WRITE;
/*!40000 ALTER TABLE `DM_Observe` DISABLE KEYS */;
/*!40000 ALTER TABLE `DM_Observe` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-07-03 18:36:58
