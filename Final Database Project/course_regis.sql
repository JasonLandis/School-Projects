-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 14, 2022 at 08:28 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
DROP DATABASE IF EXISTS `course_regis`;
--
-- Database: `course_regis`
--
CREATE DATABASE `course_regis` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `course_regis`;

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
  `courseid` int(11) NOT NULL,
  `roomid` int(11) NOT NULL,
  `subject` varchar(30) NOT NULL,
  `day` enum('M','T','W','R','F') DEFAULT NULL,
  `start_time` time DEFAULT NULL,
  `end_time` time DEFAULT NULL,
  `credits` int(11) NOT NULL DEFAULT 0,
  `price` int(11) NOT NULL DEFAULT 0,
  `start_date` date NOT NULL DEFAULT '0000-00-00',
  `end_date` date NOT NULL DEFAULT '0000-00-00'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`courseid`, `roomid`, `subject`, `day`, `start_time`, `end_time`, `credits`, `price`, `start_date`, `end_date`) VALUES
(1000, 1, 'Biology', 'M', '11:30:00', '13:30:00', 3, 1275, '2022-09-01', '2022-12-13'),
(1010, 1, 'Chemistry', 'M', '13:45:00', '15:45:00', 4, 1456, '2022-09-01', '2022-12-13'),
(1100, 5, 'English', 'F', '13:45:00', '15:45:00', 4, 1456, '2022-09-01', '2022-12-13'),
(1200, 2, 'Art', 'M', '09:15:00', '10:30:00', 3, 1092, '2022-09-01', '2022-12-13'),
(2000, 1, 'Physics', 'W', '09:30:00', '12:30:00', 4, 1543, '2022-09-01', '2022-12-13'),
(2400, 2, 'History', 'R', '13:45:00', '14:45:00', 3, 965, '2022-09-01', '2022-12-13'),
(2800, 3, 'Algebra', 'T', '12:00:00', '02:00:00', 4, 1321, '2022-09-01', '2022-12-13'),
(3000, 4, 'Spanish', 'R', '08:45:00', '10:45:00', 4, 1532, '2022-09-01', '2022-12-13'),
(3010, 4, 'French', 'W', '11:30:00', '13:00:00', 3, 1123, '2022-09-01', '2022-12-13'),
(4000, 3, 'Calculus', 'T', '02:30:00', '05:00:00', 4, 1432, '2022-09-01', '2022-12-13');

-- --------------------------------------------------------

--
-- Table structure for table `grades`
--

CREATE TABLE `grades` (
  `gradeid` int(11) NOT NULL,
  `studentid` int(11) DEFAULT NULL,
  `courseid` int(11) DEFAULT NULL,
  `grade` enum('A','B','C','D','E','O') NOT NULL DEFAULT 'O'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `grades`
--

INSERT INTO `grades` (`gradeid`, `studentid`, `courseid`, `grade`) VALUES
(1, 1, 1000, 'A'),
(2, 2, 1010, 'B'),
(3, 3, 1000, 'A'),
(4, 3, 2000, 'B'),
(5, 4, 1010, 'A'),
(6, 4, 1100, 'B'),
(7, 4, 2800, 'A'),
(8, 4, 4000, 'C'),
(9, 5, 1000, 'B'),
(10, 6, 1010, 'A'),
(11, 7, 1100, 'A'),
(12, 7, 2800, 'E'),
(13, 7, 2000, 'A'),
(14, 7, 3000, 'C'),
(15, 8, 1100, 'C'),
(16, 8, 2000, 'C'),
(17, 8, 3010, 'C'),
(18, 9, 1200, 'D'),
(19, 9, 2400, 'A'),
(20, 9, 3010, 'B'),
(21, 10, 1000, 'A'),
(22, 10, 1200, 'B');

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE `room` (
  `roomid` int(11) NOT NULL,
  `staffid` int(11) DEFAULT NULL,
  `studentid` int(11) DEFAULT NULL,
  `location` varchar(30) NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `room`
--

INSERT INTO `room` (`roomid`, `staffid`, `studentid`, `location`) VALUES
(1, 1, 4, 'Rood Hall'),
(2, 2, 2, 'Chemistry Building'),
(3, 3, 7, 'Schneider Hall'),
(4, 4, 8, 'Wood Hall'),
(5, 5, 9, 'Moore Hall');

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `staffid` int(11) NOT NULL,
  `email` varchar(30) NOT NULL DEFAULT '',
  `password` varchar(30) NOT NULL,
  `full_name` varchar(30) NOT NULL DEFAULT '',
  `profession` varchar(30) NOT NULL DEFAULT '',
  `salary` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`staffid`, `email`, `password`, `full_name`, `profession`, `salary`) VALUES
(1, 'alfreddaniels@gmail.com', 'science100', 'Alfred Daniels', 'Science Teacher', 45000),
(2, 'jerrysmith@gmail.com', 'historian123', 'Jerry Smith', 'Social Studies Teacher', 40000),
(3, 'joycehickman@gmail.com', 'mathisawesome', 'Joyce Hickman', 'Math Teacher', 50000),
(4, 'mariahjohnson@gmail.com', 'spain456', 'Mariah Johnson', 'Foreign Language Teacher', 55000),
(5, 'johnthorpe@gmail.com', 'english101', 'John Thorpe', 'English Teacher', 40000);

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `studentid` int(11) NOT NULL,
  `email` varchar(30) NOT NULL DEFAULT '',
  `password` varchar(30) NOT NULL,
  `full_name` varchar(30) NOT NULL DEFAULT '',
  `year` enum('FR','SO','JR','SR','XX') NOT NULL DEFAULT 'XX',
  `gpa` decimal(2,1) NOT NULL DEFAULT 0.0,
  `total_credits` int(11) NOT NULL,
  `balance` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`studentid`, `email`, `password`, `full_name`, `year`, `gpa`, `total_credits`, `balance`) VALUES
(1, 'johnsmith@gmail.com', 'football123', 'John Smith', 'FR', '4.0', 3, 4300),
(2, 'jamesrodgers@gmail.com', '12345', 'James Rodgers', 'FR', '3.0', 4, 2000),
(3, 'matthewstanton@gmail.com', 'happy100', 'Matthew Stanton', 'SO', '3.5', 7, 8390),
(4, 'derrickcousins@gmail.com', 'derr456', 'Derrick Cousins', 'SR', '3.3', 16, 3290),
(5, 'Sophiasmith@gmail.com', 'algebra101', 'Sophia Smith', 'FR', '3.0', 3, 2967),
(6, 'Ashleycook@gmail.com', 'cook000', 'Ashley Cook', 'FR', '4.0', 4, 4343),
(7, 'Alyssakidd@gmail.com', '111999222', 'Alyssa Cook', 'JR', '2.5', 12, 1921),
(8, 'alexhenry@gmail.com', 'basketball1', 'Alex Henry', 'JR', '2.0', 12, 2390),
(9, 'jamesduncan@gmail.com', 'soccer246', 'James Duncan', 'JR', '2.7', 10, 4290),
(10, 'elliotsharp@gmail.com', 'sharp555', 'Elliot Sharp', 'SO', '4.0', 6, 1734);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`courseid`),
  ADD KEY `roomid` (`roomid`);

--
-- Indexes for table `grades`
--
ALTER TABLE `grades`
  ADD PRIMARY KEY (`gradeid`),
  ADD KEY `studentid` (`studentid`),
  ADD KEY `courseid` (`courseid`);

--
-- Indexes for table `room`
--
ALTER TABLE `room`
  ADD PRIMARY KEY (`roomid`),
  ADD KEY `staffid` (`staffid`),
  ADD KEY `studentid` (`studentid`);

--
-- Indexes for table `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`staffid`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`studentid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `grades`
--
ALTER TABLE `grades`
  MODIFY `gradeid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=123503;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `studentid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `course`
--
ALTER TABLE `course`
  ADD CONSTRAINT `course_ibfk_1` FOREIGN KEY (`roomid`) REFERENCES `room` (`roomid`);

--
-- Constraints for table `grades`
--
ALTER TABLE `grades`
  ADD CONSTRAINT `grades_ibfk_1` FOREIGN KEY (`studentid`) REFERENCES `student` (`studentid`),
  ADD CONSTRAINT `grades_ibfk_2` FOREIGN KEY (`courseid`) REFERENCES `course` (`courseid`);

--
-- Constraints for table `room`
--
ALTER TABLE `room`
  ADD CONSTRAINT `room_ibfk_1` FOREIGN KEY (`staffid`) REFERENCES `staff` (`staffid`),
  ADD CONSTRAINT `room_ibfk_2` FOREIGN KEY (`studentid`) REFERENCES `student` (`studentid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
