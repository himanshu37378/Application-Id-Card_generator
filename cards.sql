-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:4306
-- Generation Time: Dec 17, 2023 at 01:33 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 7.3.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `id_card`
--

-- --------------------------------------------------------

--
-- Table structure for table `cards`
--

CREATE TABLE `cards` (
  `sno` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `fname` varchar(50) DEFAULT NULL,
  `program` varchar(15) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL,
  `phone` varchar(12) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `crn` varchar(20) DEFAULT NULL,
  `urn` varchar(20) DEFAULT NULL,
  `exp_date` varchar(20) DEFAULT NULL,
  `image` varchar(255) NOT NULL,
  `scans` int(10) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cards`
--

INSERT INTO `cards` (`sno`, `name`, `fname`, `program`, `email`, `phone`, `address`, `crn`, `urn`, `exp_date`, `image`, `scans`) VALUES
(72946, 'Neelam Sharma', 'Rajesh Sharma', 'B.Tech(IT)', 'sejalsharma3918@gmail.com', '7626920311', 'Shaheed karnail singh nagar, Ludhiana, Punjab', '2021083', '2004962', '30.06.2023', 'assets/uploads/neelam.jpeg', 0),
(72945, 'Lakshmi Singh', 'Bhola Singh', 'B.Tech(IT)', 'lakshmisingh4112@gmail.com', '9463863117', '#4321/5, st no. 4 , SAS Nagar, Ludhiana, Punjab', '2021070', '2004949', '30.06.2023', 'assets/uploads/lakshmi.jpg', 10),
(72944, 'Himanshu Mahajan', 'Yogesh Mahajan', 'B.Tech(IT)', 'himanshumahajan3737@gmail.com', '6283403019', '#6248,street no.5, Hargobind nagar, near hanuman mandir, Ludhiana', '2021150', '2104587', '30.06.2023', 'assets/uploads/himanshu.jpeg', 7),
(78914, 'Mandeep kaur', 'Rupinder singh', 'Btech(IT)', 'mandeepkaur@gmail.com', '9876543210', 'house no-6248 street no-5', '2021072', '2004952', '2023-06-30', 'assets/uploads/', 0),
(78945, 'Chahat Mahajan', 'Yogesh mahajan', 'Btech(IT)', 'chahatmahajan3737@gmail.com', '09872264062', 'house no-6248 street no-5', '2021080', '2104555', '2023-06-30', 'assets/uploads/WhatsApp Image 2021-11-28 at 10.30.07 AM.jpeg', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cards`
--
ALTER TABLE `cards`
  ADD PRIMARY KEY (`sno`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
