-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 25, 2020 at 06:07 PM
-- Server version: 10.1.40-MariaDB
-- PHP Version: 7.3.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `proyeksoa`
--

-- --------------------------------------------------------

--
-- Table structure for table `group`
--

CREATE TABLE `group` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `status` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `group`
--

INSERT INTO `group` (`id`, `name`, `status`, `created_at`, `last_update`) VALUES
(1, 'wasd', 1, '2020-06-14 12:22:50', '2020-06-14 12:26:55'),
(2, 'asd', 1, '2020-06-14 12:27:40', '2020-06-14 12:27:40'),
(3, 'asd', 1, '2020-06-14 12:56:08', '2020-06-14 12:56:08'),
(5, 'group_lama', 1, '2020-06-23 08:50:48', '2020-06-23 08:51:07'),
(6, 'andhika', 1, '2020-06-24 07:40:37', '2020-06-24 07:40:37'),
(7, 'andhika2', 1, '2020-06-24 07:41:19', '2020-06-24 07:41:19'),
(8, 'andhikalagi', 0, '2020-06-24 07:45:22', '2020-06-24 07:46:23');

-- --------------------------------------------------------

--
-- Table structure for table `group_member`
--

CREATE TABLE `group_member` (
  `id` int(11) NOT NULL,
  `id_group` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `status` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `group_member`
--

INSERT INTO `group_member` (`id`, `id_group`, `id_user`, `created_at`, `status`) VALUES
(2, 1, 1, '2020-06-14 13:20:52', 0),
(3, 1, 3, '2020-06-23 08:47:28', 1),
(4, 1, 2, '2020-06-24 08:20:26', 1);

-- --------------------------------------------------------

--
-- Table structure for table `group_schedule`
--

CREATE TABLE `group_schedule` (
  `id` int(11) NOT NULL,
  `id_group` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `date` date NOT NULL,
  `start_time` time NOT NULL,
  `end_time` time NOT NULL,
  `status` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `group_schedule`
--

INSERT INTO `group_schedule` (`id`, `id_group`, `id_user`, `date`, `start_time`, `end_time`, `status`) VALUES
(2, 2, 1, '2020-06-25', '17:10:00', '18:00:00', 1),
(3, 2, 2, '2020-06-25', '16:13:00', '17:00:00', 0),
(4, 3, 3, '2020-06-25', '11:00:00', '22:00:00', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `group`
--
ALTER TABLE `group`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `group_member`
--
ALTER TABLE `group_member`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `group_schedule`
--
ALTER TABLE `group_schedule`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `group`
--
ALTER TABLE `group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `group_member`
--
ALTER TABLE `group_member`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `group_schedule`
--
ALTER TABLE `group_schedule`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
