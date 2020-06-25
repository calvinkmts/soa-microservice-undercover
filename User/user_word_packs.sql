-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 25, 2020 at 06:01 PM
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
-- Table structure for table `user_word_packs`
--

CREATE TABLE `user_word_packs` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `id_user` bigint(20) UNSIGNED NOT NULL,
  `id_word_pack` bigint(20) UNSIGNED NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `user_word_packs`
--

INSERT INTO `user_word_packs` (`id`, `id_user`, `id_word_pack`, `created_at`, `updated_at`) VALUES
(1, 1, 70, '2019-12-31 09:00:00', '2019-12-31 11:00:00'),
(2, 1, 2, '2020-12-31 09:00:00', '2020-12-31 09:00:00'),
(3, 114, 157, '2017-12-31 09:00:00', '2017-12-31 09:00:00'),
(4, 64, 182, '2017-12-31 09:00:00', '2017-12-31 09:00:00'),
(5, 155, 121, '2017-12-31 09:00:00', '2017-12-31 09:00:00'),
(6, 64, 92, '2017-12-31 09:00:00', '2017-12-31 09:00:00'),
(7, 80, 182, '2017-12-31 09:00:00', '2017-12-31 09:00:00'),
(8, 51, 130, '2017-12-31 09:00:00', '2017-12-31 09:00:00'),
(9, 97, 153, '2017-12-31 09:00:00', '2017-12-31 09:00:00'),
(10, 172, 51, '2017-12-31 09:00:00', '2017-12-31 09:00:00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `user_word_packs`
--
ALTER TABLE `user_word_packs`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user_word_packs`
--
ALTER TABLE `user_word_packs`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
