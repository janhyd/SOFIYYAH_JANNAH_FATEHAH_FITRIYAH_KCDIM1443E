-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 15, 2024 at 09:31 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cat_hotel`
--

-- --------------------------------------------------------

--
-- Table structure for table `boarding`
--

CREATE TABLE `boarding` (
  `SUITE` varchar(30) DEFAULT NULL,
  `BOARDING_TYPE` varchar(50) DEFAULT NULL,
  `DAY` int(10) DEFAULT NULL,
  `DAY_CHECK_IN` int(10) DEFAULT NULL,
  `TOTAL` int(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `grooming`
--

CREATE TABLE `grooming` (
  `PACKAGE` varchar(30) DEFAULT NULL,
  `HAIRCCUT` varchar(30) DEFAULT NULL,
  `TOTAL` int(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `registration`
--

CREATE TABLE `registration` (
  `ID` int(10) DEFAULT NULL,
  `NAME` varchar(30) DEFAULT NULL,
  `ADDRESS` text DEFAULT NULL,
  `PHONE_NO` int(11) DEFAULT NULL,
  `EMAIL` varchar(30) DEFAULT NULL,
  `CAT_NAME` varchar(10) DEFAULT NULL,
  `CAT_AGE` int(30) DEFAULT NULL,
  `CATE_BREED` varchar(30) DEFAULT NULL,
  `NOTES` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `treatment`
--

CREATE TABLE `treatment` (
  `TREATMENT_TYPE` varchar(10) DEFAULT NULL,
  `SESSION` int(10) DEFAULT NULL,
  `MEDICINE_TYPE` varchar(20) DEFAULT NULL,
  `TOTAL` int(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
