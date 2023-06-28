-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jun 28, 2023 at 07:56 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `StudentMarks`
--

-- --------------------------------------------------------

--
-- Table structure for table `StudentInfo`
--

CREATE TABLE `StudentInfo` (
  `StId` int(11) NOT NULL,
  `FName` varchar(255) NOT NULL,
  `LName` varchar(255) NOT NULL,
  `Grade` int(11) NOT NULL,
  `BirthDate` varchar(255) NOT NULL,
  `PName` varchar(255) NOT NULL,
  `City` varchar(255) NOT NULL,
  `Phone` bigint(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `StudentInfo`
--

INSERT INTO `StudentInfo` (`StId`, `FName`, `LName`, `Grade`, `BirthDate`, `PName`, `City`, `Phone`) VALUES
(1, 'Naman', 'MAthur', 2, '23/2/1999', 'Om', 'Mumbai', 8359833434),
(2, 'Vijay', 'Chauhan', 3, '2/2/1323', 'Dinanath', 'Mandwa', 2342342343),
(3, 'Hritik', 'Roshan', 1, '1/1/1222', 'K', 'Mumbai', 2323232323),
(4, 'Sanjay', 'Patil', 1, '12/12/2444', 'Ok', 'Pune', 9879879879);

-- --------------------------------------------------------

--
-- Table structure for table `StudentMark`
--

CREATE TABLE `StudentMark` (
  `StId` int(11) NOT NULL,
  `Mathematics` int(11) NOT NULL,
  `Science` int(11) NOT NULL,
  `History` int(11) NOT NULL,
  `Percentage` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `StudentMark`
--

INSERT INTO `StudentMark` (`StId`, `Mathematics`, `Science`, `History`, `Percentage`) VALUES
(4, 78, 88, 68, 78),
(3, 55, 55, 68, 59),
(2, 60, 55, 68, 61),
(2, 40, 55, 68, 54),
(1, 40, 55, 68, 54);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `StudentInfo`
--
ALTER TABLE `StudentInfo`
  ADD PRIMARY KEY (`StId`),
  ADD KEY `StId` (`StId`) USING BTREE;

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `StudentInfo`
--
ALTER TABLE `StudentInfo`
  MODIFY `StId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
