-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 25, 2020 at 10:49 AM
-- Server version: 10.3.16-MariaDB
-- PHP Version: 7.3.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `soa`
--

-- --------------------------------------------------------

--
-- Table structure for table `transaction`
--

CREATE TABLE `transaction` (
  `id` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `id_word_pack` int(11) DEFAULT NULL,
  `type` varchar(20) NOT NULL DEFAULT 'PURCHASE',
  `amount` double DEFAULT NULL,
  `code` varchar(255) DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `transaction`
--

INSERT INTO `transaction` (`id`, `id_user`, `id_word_pack`, `type`, `amount`, `code`, `created_at`, `updated_at`) VALUES
(1, 1, NULL, 'REDEEM', 20000, 'wp1', '2020-06-23 23:10:50', '2020-06-23 23:10:50'),
(2, 2, NULL, 'REDEEM', 20000, 'wp1', '2020-06-23 23:14:19', '2020-06-23 23:14:19'),
(18, 2, 1, 'PURCHASED', 4542, NULL, '2020-06-24 21:08:20', '2020-06-24 21:08:20'),
(19, 2, NULL, 'REDEEM', 20000, 'wp1', '2020-06-24 21:14:10', '2020-06-24 21:14:10'),
(20, 3, NULL, 'REDEEM', 20000, 'wp1', '2020-06-24 21:29:22', '2020-06-24 21:29:22'),
(21, 4, NULL, 'REDEEM', 20000, 'wp1', '2020-06-24 21:30:36', '2020-06-24 21:30:36'),
(22, 5, NULL, 'REDEEM', 20000, 'wp1', '2020-06-24 21:31:56', '2020-06-24 21:31:56'),
(23, 6, NULL, 'REDEEM', 20000, 'wp1', '2020-06-24 21:32:52', '2020-06-24 21:32:52'),
(24, 6, 0, 'REDEEM', 20000, 'wp1', '2020-06-24 21:36:20', '2020-06-24 21:36:20'),
(25, 6, NULL, 'REDEEM', 20000, 'wp1', '2020-06-24 21:37:56', '2020-06-24 21:37:56'),
(26, 6, 0, 'REDEEM', 20000, 'wp1', '2020-06-24 21:39:02', '2020-06-24 21:39:02'),
(27, 6, 0, 'REDEEM', 20000, 'wp1', '2020-06-24 21:39:47', '2020-06-24 21:39:47'),
(28, 6, 0, 'REDEEM', 20000, 'wp1', '2020-06-24 21:42:25', '2020-06-24 21:42:25'),
(29, 7, NULL, 'REDEEM', 20000, 'ww', '2020-06-24 21:43:00', '2020-06-24 21:43:00'),
(30, 6, 2, 'PURCHASED', 27611, 'None', '2020-06-24 21:45:33', '2020-06-24 21:45:33'),
(31, 9, 0, 'REDEEM', 20000, 'wp1', '2020-06-24 21:49:42', '2020-06-24 21:49:42'),
(32, 9, 2, 'PURCHASED', 27611, 'None', '2020-06-24 21:50:07', '2020-06-24 21:50:07'),
(33, 9, 2, 'PURCHASED', 27611, 'None', '2020-06-24 22:07:50', '2020-06-24 22:07:50'),
(34, 7, 2, 'PURCHASED', 27611, 'None', '2020-06-24 22:08:10', '2020-06-24 22:08:10'),
(35, 7, 2, 'PURCHASED', 27611, 'None', '2020-06-24 22:08:10', '2020-06-24 22:08:10'),
(36, 9, 0, 'REDEEM', 20000, 'wp1', '2020-06-24 22:10:39', '2020-06-24 22:10:39'),
(37, 9, 2, 'PURCHASED', 27611, 'None', '2020-06-24 22:11:03', '2020-06-24 22:11:03'),
(38, 9, 3, 'PURCHASE', 0, NULL, '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(39, 9, 3, 'PURCHASE', 0, NULL, '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(40, 9, 3, 'PURCHASE', 0, NULL, '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(41, 9, 3, 'PURCHASE', 0, NULL, '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(42, 9, 3, 'PURCHASE', 0, NULL, '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(43, 9, 3, 'PURCHASE', NULL, NULL, '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(44, 9, 3, 'PURCHASE', NULL, NULL, '2020-06-24 22:32:32', '2020-06-24 22:32:32'),
(45, 9, 3, 'PURCHASE', NULL, NULL, '2020-06-24 22:32:35', '2020-06-24 22:32:35'),
(46, 9, 3, 'PURCHASE', NULL, NULL, '2020-06-24 22:34:08', '2020-06-24 22:34:08'),
(47, 2, 3, 'PURCHASED', 66599, 'None', '2020-06-24 22:35:36', '2020-06-24 22:35:36'),
(48, 2, 3, 'PURCHASE', NULL, NULL, '2020-06-24 22:35:36', '2020-06-24 22:35:36'),
(49, 2, 3, 'PURCHASED', 66599, 'None', '2020-06-24 22:36:20', '2020-06-24 22:36:20'),
(50, 3, 1, 'PURCHASED', 4542, 'None', '2020-06-24 22:37:32', '2020-06-24 22:37:32'),
(51, 9, 0, 'REDEEM', 20000, 'wp1', '2020-06-24 22:44:57', '2020-06-24 22:44:57'),
(52, 9, 2, 'PURCHASED', 27611, 'None', '2020-06-24 22:45:26', '2020-06-24 22:45:26'),
(53, 9, 0, 'REDEEM', 20000, 'wp1', '2020-06-24 22:48:37', '2020-06-24 22:48:37'),
(54, 9, 5, 'PURCHASED', 98808, 'None', '2020-06-24 22:49:09', '2020-06-24 22:49:09'),
(55, 9, 5, 'PURCHASE', NULL, NULL, '2020-06-25 00:39:24', '2020-06-25 00:39:24'),
(56, 9, 2, 'PURCHASE', NULL, NULL, '2020-06-25 00:52:54', '2020-06-25 00:52:54'),
(57, 9, 3, 'PURCHASE', NULL, NULL, '2020-06-25 00:52:57', '2020-06-25 00:52:57'),
(58, 9, 4, 'PURCHASED', 6863, 'None', '2020-06-25 00:52:58', '2020-06-25 00:52:58'),
(59, 9, 0, 'REDEEM', 20000, 'wp1', '2020-06-25 00:53:21', '2020-06-25 00:53:21'),
(60, 9, 2, 'PURCHASED', 27611, 'None', '2020-06-25 01:00:19', '2020-06-25 01:00:19'),
(61, 8, 0, 'REDEEM', 20000, 'wp1', '2020-06-25 14:19:36', '2020-06-25 14:19:36'),
(62, 8, 0, 'REDEEM', 20000, 'wp1', '2020-06-25 14:20:19', '2020-06-25 14:20:19'),
(63, 8, 0, 'REDEEM', 20000, 'wp1', '2020-06-25 14:20:35', '2020-06-25 14:20:35'),
(64, 8, 3, 'PURCHASE', NULL, NULL, '2020-06-25 14:21:50', '2020-06-25 14:21:50'),
(65, 8, 2, 'PURCHASED', 27611, 'None', '2020-06-25 14:22:15', '2020-06-25 14:22:15'),
(66, 6, 2, 'REDEEMED', 27611, 'None', '2020-06-25 14:23:46', '2020-06-25 15:04:46'),
(67, 8, 1, 'PURCHASED', 4542, 'None', '2020-06-25 14:24:28', '2020-06-25 14:24:28'),
(68, 8, 0, 'REDEEM', 20000, 'wp1', '2020-06-25 14:36:13', '2020-06-25 14:36:13'),
(69, 9, 0, 'REDEEM', 20000, 'ww', '2020-06-25 14:37:12', '2020-06-25 14:37:12'),
(71, 10, 0, 'REDEEM', 100000, 'yokengg', '2020-06-25 14:52:59', '2020-06-25 14:52:59');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `transaction`
--
ALTER TABLE `transaction`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `transaction`
--
ALTER TABLE `transaction`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=72;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
