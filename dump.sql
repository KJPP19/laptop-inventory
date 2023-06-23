-- MariaDB dump 10.19  Distrib 10.4.28-MariaDB, for osx10.10 (x86_64)
--
-- Host: localhost    Database: inventory_management
-- ------------------------------------------------------
-- Server version	10.4.28-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `account_customaccount`
--

DROP TABLE IF EXISTS `account_customaccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_customaccount` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `name` varchar(100) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_customaccount`
--

LOCK TABLES `account_customaccount` WRITE;
/*!40000 ALTER TABLE `account_customaccount` DISABLE KEYS */;
INSERT INTO `account_customaccount` VALUES (5,'pbkdf2_sha256$600000$uUNQj1bSJQx3COmKOsBmEL$u1A3DQd4e94/EST4w2bM2jyjHT7PMtF+2/UUKZM3jtE=','2023-06-08 01:29:18.517195','kadmin@sample.com','kadmin',1,1,1),(8,'pbkdf2_sha256$600000$Ahbk6d4nIpqMM8kYoTEpbZ$Bxk69QP9FxYmHjV/UDoWscDyEuAZxnuGABcB6Wo8UbE=',NULL,'kuser@sample.com','kuser',1,1,0),(11,'pbkdf2_sha256$600000$NtjZm6DWuMba0wW4APhoWm$saFi+D1KoqnyqDlrMnYL14wojrawFeVdEPKza7HGOgg=',NULL,'kuserinas@sample.com','kuserina',1,1,0),(12,'pbkdf2_sha256$600000$MKzUvBLA6vGg3mgeXrBJj2$WDVJPnsaAKdhQcpVU6sPJUROI3SzxTd21exgU1OED/k=',NULL,'keanp@example.com','kean',1,1,0);
/*!40000 ALTER TABLE `account_customaccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_customaccount_groups`
--

DROP TABLE IF EXISTS `account_customaccount_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_customaccount_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `customaccount_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `account_customaccount_gr_customaccount_id_group_i_855a9c26_uniq` (`customaccount_id`,`group_id`),
  KEY `account_customaccount_groups_group_id_b2a7c841_fk_auth_group_id` (`group_id`),
  CONSTRAINT `account_customaccoun_customaccount_id_0041d606_fk_account_c` FOREIGN KEY (`customaccount_id`) REFERENCES `account_customaccount` (`id`),
  CONSTRAINT `account_customaccount_groups_group_id_b2a7c841_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_customaccount_groups`
--

LOCK TABLES `account_customaccount_groups` WRITE;
/*!40000 ALTER TABLE `account_customaccount_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_customaccount_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_customaccount_user_permissions`
--

DROP TABLE IF EXISTS `account_customaccount_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_customaccount_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `customaccount_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `account_customaccount_us_customaccount_id_permiss_e0c851a6_uniq` (`customaccount_id`,`permission_id`),
  KEY `account_customaccoun_permission_id_abf68993_fk_auth_perm` (`permission_id`),
  CONSTRAINT `account_customaccoun_customaccount_id_b10a3876_fk_account_c` FOREIGN KEY (`customaccount_id`) REFERENCES `account_customaccount` (`id`),
  CONSTRAINT `account_customaccoun_permission_id_abf68993_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_customaccount_user_permissions`
--

LOCK TABLES `account_customaccount_user_permissions` WRITE;
/*!40000 ALTER TABLE `account_customaccount_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_customaccount_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_login`
--

DROP TABLE IF EXISTS `account_login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_login` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_login`
--

LOCK TABLES `account_login` WRITE;
/*!40000 ALTER TABLE `account_login` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add damaged unit',6,'add_damagedunit'),(22,'Can change damaged unit',6,'change_damagedunit'),(23,'Can delete damaged unit',6,'delete_damagedunit'),(24,'Can view damaged unit',6,'view_damagedunit'),(25,'Can add laptop',7,'add_laptop'),(26,'Can change laptop',7,'change_laptop'),(27,'Can delete laptop',7,'delete_laptop'),(28,'Can view laptop',7,'view_laptop'),(29,'Can add user info',8,'add_userinfo'),(30,'Can change user info',8,'change_userinfo'),(31,'Can delete user info',8,'delete_userinfo'),(32,'Can view user info',8,'view_userinfo'),(33,'Can add custom account',9,'add_customaccount'),(34,'Can change custom account',9,'change_customaccount'),(35,'Can delete custom account',9,'delete_customaccount'),(36,'Can view custom account',9,'view_customaccount'),(37,'Can add log in',10,'add_login'),(38,'Can change log in',10,'change_login'),(39,'Can delete log in',10,'delete_login'),(40,'Can view log in',10,'view_login'),(41,'Can add Token',11,'add_token'),(42,'Can change Token',11,'change_token'),(43,'Can delete Token',11,'delete_token'),(44,'Can view Token',11,'view_token'),(45,'Can add token',12,'add_tokenproxy'),(46,'Can change token',12,'change_tokenproxy'),(47,'Can delete token',12,'delete_tokenproxy'),(48,'Can view token',12,'view_tokenproxy');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authtoken_token`
--

DROP TABLE IF EXISTS `authtoken_token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_account_customaccount_id` FOREIGN KEY (`user_id`) REFERENCES `account_customaccount` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authtoken_token`
--

LOCK TABLES `authtoken_token` WRITE;
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;
INSERT INTO `authtoken_token` VALUES ('a9433551a73175f3ce0a243daebc9875968688ad','2023-06-06 02:42:45.145263',12),('cd9e9adcff403b14f129fb4c8c54d21405bb54f2','2023-05-31 06:55:22.049405',8);
/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_account_customaccount_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_account_customaccount_id` FOREIGN KEY (`user_id`) REFERENCES `account_customaccount` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (9,'account','customaccount'),(10,'account','login'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(11,'authtoken','token'),(12,'authtoken','tokenproxy'),(4,'contenttypes','contenttype'),(6,'laptop','damagedunit'),(7,'laptop','laptop'),(8,'laptop','userinfo'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'account','0001_initial','2023-05-30 03:32:40.686173'),(2,'contenttypes','0001_initial','2023-05-30 03:32:40.771180'),(3,'admin','0001_initial','2023-05-30 03:32:40.973460'),(4,'admin','0002_logentry_remove_auto_add','2023-05-30 03:32:40.986011'),(5,'admin','0003_logentry_add_action_flag_choices','2023-05-30 03:32:40.997577'),(6,'contenttypes','0002_remove_content_type_name','2023-05-30 03:32:41.088699'),(7,'auth','0001_initial','2023-05-30 03:32:41.452039'),(8,'auth','0002_alter_permission_name_max_length','2023-05-30 03:32:41.526222'),(9,'auth','0003_alter_user_email_max_length','2023-05-30 03:32:41.534027'),(10,'auth','0004_alter_user_username_opts','2023-05-30 03:32:41.543126'),(11,'auth','0005_alter_user_last_login_null','2023-05-30 03:32:41.554503'),(12,'auth','0006_require_contenttypes_0002','2023-05-30 03:32:41.559326'),(13,'auth','0007_alter_validators_add_error_messages','2023-05-30 03:32:41.569057'),(14,'auth','0008_alter_user_username_max_length','2023-05-30 03:32:41.587226'),(15,'auth','0009_alter_user_last_name_max_length','2023-05-30 03:32:41.603210'),(16,'auth','0010_alter_group_name_max_length','2023-05-30 03:32:41.634766'),(17,'auth','0011_update_proxy_permissions','2023-05-30 03:32:41.650313'),(18,'auth','0012_alter_user_first_name_max_length','2023-05-30 03:32:41.662466'),(19,'laptop','0001_initial','2023-05-30 03:32:41.695251'),(20,'laptop','0002_damagedunit_laptop_userinfo_delete_user_and_more','2023-05-30 03:32:42.114503'),(21,'laptop','0003_alter_userinfo_contact_number_alter_userinfo_email','2023-05-30 03:32:42.212643'),(22,'sessions','0001_initial','2023-05-30 03:32:42.258169'),(23,'authtoken','0001_initial','2023-05-31 02:18:46.081666'),(24,'authtoken','0002_auto_20160226_1747','2023-05-31 02:18:46.112953'),(25,'authtoken','0003_tokenproxy','2023-05-31 02:18:46.119644'),(26,'account','0002_customaccount_groups_customaccount_is_superuser_and_more','2023-05-31 04:28:48.317792'),(27,'account','0003_alter_customaccount_is_active','2023-05-31 04:59:24.644646'),(28,'account','0004_alter_customaccount_is_active_and_more','2023-05-31 05:25:22.764363');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('9d50xgux7m5e6rvqlvj4sujpb5ttmtxn','.eJxVjMsOwiAQRf-FtSHlDS7d-w1kBgapGkhKuzL-uzbpQrf3nHNfLMK21rgNWuKc2ZkZdvrdENKD2g7yHdqt89TbuszId4UfdPBrz_S8HO7fQYVRv7UoSnnKJRiTpE5yQp_AOUQxBaFkyApDCQRWCPBaITirSGrywYEF6dj7A-ONN6o:1q74Sk:X47952C9kJlCHPM6koGUoyuitkGTllKFtW6XtF6ttnM','2023-06-22 01:29:18.531287');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `laptop_damagedunit`
--

DROP TABLE IF EXISTS `laptop_damagedunit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `laptop_damagedunit` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `damage_type` varchar(20) NOT NULL,
  `description` longtext NOT NULL,
  `added_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `laptop_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `laptop_damagedunit_laptop_id_4126b849_fk_laptop_laptop_id` (`laptop_id`),
  KEY `laptop_damagedunit_user_id_2164e500_fk_laptop_userinfo_id` (`user_id`),
  CONSTRAINT `laptop_damagedunit_laptop_id_4126b849_fk_laptop_laptop_id` FOREIGN KEY (`laptop_id`) REFERENCES `laptop_laptop` (`id`),
  CONSTRAINT `laptop_damagedunit_user_id_2164e500_fk_laptop_userinfo_id` FOREIGN KEY (`user_id`) REFERENCES `laptop_userinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `laptop_damagedunit`
--

LOCK TABLES `laptop_damagedunit` WRITE;
/*!40000 ALTER TABLE `laptop_damagedunit` DISABLE KEYS */;
INSERT INTO `laptop_damagedunit` VALUES (1,'minor','few scratches','2023-06-23 02:37:17.709083','2023-06-23 02:37:17.709125',1,1),(2,'minor','few scratches and dents','2023-06-23 02:37:48.711442','2023-06-23 02:37:48.711503',1,1);
/*!40000 ALTER TABLE `laptop_damagedunit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `laptop_laptop`
--

DROP TABLE IF EXISTS `laptop_laptop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `laptop_laptop` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `brand` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  `serial_number` varchar(100) NOT NULL,
  `PO_number` varchar(100) DEFAULT NULL,
  `status` varchar(20) NOT NULL,
  `added_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `current_user_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `serial_number` (`serial_number`),
  UNIQUE KEY `PO_number` (`PO_number`),
  KEY `laptop_laptop_current_user_id_15aab651_fk_laptop_userinfo_id` (`current_user_id`),
  CONSTRAINT `laptop_laptop_current_user_id_15aab651_fk_laptop_userinfo_id` FOREIGN KEY (`current_user_id`) REFERENCES `laptop_userinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `laptop_laptop`
--

LOCK TABLES `laptop_laptop` WRITE;
/*!40000 ALTER TABLE `laptop_laptop` DISABLE KEYS */;
INSERT INTO `laptop_laptop` VALUES (1,'Apple','Macbook air M1','XXXXXY123','133224','assigned','2023-06-01 15:23:53.552491','2023-06-01 15:23:53.552529',1),(2,'Apple','MacBook pro M2 chip','XXXXXX1XXX','1114432','assigned','2023-06-03 07:37:35.867013','2023-06-03 07:39:39.294203',3);
/*!40000 ALTER TABLE `laptop_laptop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `laptop_userinfo`
--

DROP TABLE IF EXISTS `laptop_userinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `laptop_userinfo` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `contact_number` varchar(20) NOT NULL,
  `added_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `laptop_userinfo_contact_number_5c4cb59c_uniq` (`contact_number`),
  UNIQUE KEY `laptop_userinfo_email_f4af2061_uniq` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `laptop_userinfo`
--

LOCK TABLES `laptop_userinfo` WRITE;
/*!40000 ALTER TABLE `laptop_userinfo` DISABLE KEYS */;
INSERT INTO `laptop_userinfo` VALUES (1,'john doe','johndoe@example.com','09197862543','2023-06-01 02:46:22.826068','2023-06-01 02:46:22.826109'),(3,'johnny','johnny@example.com','09158631111','2023-06-01 03:37:55.901662','2023-06-01 03:37:55.901740'),(4,'johnny yes','papa@example.com','09158631122','2023-06-01 03:38:37.357436','2023-06-01 03:38:37.357501'),(5,'kenneth','ken@example.com','09113448531','2023-06-01 03:45:53.015008','2023-06-01 03:45:53.015053'),(6,'kennethp','kenp@example.com','09111111111','2023-06-01 04:00:20.572943','2023-06-01 04:00:20.572988');
/*!40000 ALTER TABLE `laptop_userinfo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-23 11:07:10
