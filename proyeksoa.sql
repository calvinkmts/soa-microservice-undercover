-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 24, 2020 at 02:54 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
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
-- Table structure for table `games`
--

CREATE TABLE `games` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `status` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `game_members`
--

CREATE TABLE `game_members` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `id_game` bigint(20) UNSIGNED NOT NULL,
  `id_member` bigint(20) UNSIGNED NOT NULL,
  `id_round` bigint(20) UNSIGNED NOT NULL,
  `role` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `status` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `game_rounds`
--

CREATE TABLE `game_rounds` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `id_game` bigint(20) UNSIGNED NOT NULL,
  `round` int(11) NOT NULL,
  `word_1` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `word_2` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `num_mr_white` int(11) NOT NULL,
  `num_civilian` int(11) NOT NULL,
  `num_undercover` int(11) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `game_word_packs`
--

CREATE TABLE `game_word_packs` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `id_game` bigint(20) UNSIGNED NOT NULL,
  `id_word_pack` bigint(20) UNSIGNED NOT NULL,
  `id_contributor` bigint(20) UNSIGNED NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `groups`
--

CREATE TABLE `groups` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `status` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `group_members`
--

CREATE TABLE `group_members` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `id_group` bigint(20) UNSIGNED NOT NULL,
  `id_user` bigint(20) UNSIGNED NOT NULL,
  `status` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `group_schedules`
--

CREATE TABLE `group_schedules` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `id_group` bigint(20) UNSIGNED NOT NULL,
  `id_user` bigint(20) UNSIGNED NOT NULL,
  `date` date NOT NULL,
  `start_time` time NOT NULL,
  `end_time` time NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `round_details`
--

CREATE TABLE `round_details` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `id_round` bigint(20) UNSIGNED NOT NULL,
  `id_user` bigint(20) UNSIGNED NOT NULL,
  `turn` int(11) NOT NULL,
  `condition` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `user_word` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `user_description` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `transactions`
--

CREATE TABLE `transactions` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `id_user` bigint(20) UNSIGNED NOT NULL,
  `id_word_pack` bigint(20) UNSIGNED NOT NULL,
  `type` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `amount` double(8,2) NOT NULL,
  `voucher_code` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `status` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `gender` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `dob` date NOT NULL,
  `status` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `balance` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `email`, `password`, `name`, `gender`, `dob`, `status`, `created_at`, `updated_at`, `balance`) VALUES
(2, 'devphil@yahoo.ca', '6b75789a3c2415f290139923f8fbc0f2', 'Alexandra Lutz', 'F', '2002-10-05', 'ACTIVE', '2017-12-31 09:00:00', '2017-12-31 09:00:00', 0),
(3, 'barnett@me.com', 'c3faad0e29c54860c92cf1ec20f4fdbf', 'Leonidas Hughes', 'F', '1982-07-23', 'ACTIVE', '2017-12-31 09:00:00', '2017-12-31 09:00:00', 0),
(4, 'shaffei@mac.com', '457e05ded2ce000f8819a281a16f1f8d', 'Marquis Marks', 'M', '1994-09-24', 'ACTIVE', '2017-12-31 09:00:00', '2017-12-31 09:00:00', 0),
(5, 'hamilton@yahoo.com', '5ea15d8c1b66320049b07e6eeb9963c4', 'Aidan Krueger', 'F', '1975-09-02', 'CREATED', '2017-12-31 09:00:00', '2017-12-31 09:00:00', 0),
(6, 'murdocj@comcast.net', '2203d3a1fcdf34da8ed34ab3d412417e', 'Rebekah Berger', 'F', '1997-05-14', 'ACTIVE', '2017-12-31 09:00:00', '2017-12-31 09:00:00', 0),
(7, 'milton@hotmail.com', 'c0c9151335f96f90667ef358d0b7af57', 'Mattie Fields', 'F', '2007-06-04', 'CREATED', '2017-12-31 09:00:00', '2017-12-31 09:00:00', 0),
(8, 'debest@live.com', '6eb8a30ea9720627ccf5af22efd541f8', 'Celeste Parsons', 'M', '1957-04-22', 'CREATED', '2017-12-31 09:00:00', '2017-12-31 09:00:00', 0),
(9, 'gknauss@outlook.com', '4bebd505c66aca1a4432715c74451b53', 'Jamar Armstrong', 'M', '2009-04-05', 'ACTIVE', '2017-12-31 09:00:00', '2017-12-31 09:00:00', 0),
(10, 'fglock@icloud.com', '0cbdcd9b8edc83e3cfc790f8ef9dc98b', 'Nelson Bolton', 'M', '1951-05-31', 'ACTIVE', '2017-12-31 09:00:00', '2017-12-31 09:00:00', 0),
(11, 'eric13@gmail.com', 'ericeric', 'eboi', 'M', '1998-12-13', 'CREATED', '2020-12-31 09:00:00', '2020-12-31 09:00:00', 1000),
(12, 'erictirtana13@gmail.com', 'ericeric', 'Eric Tirtana', 'M', '1998-12-13', 'CREATED', '2020-12-31 09:00:00', '2020-12-31 09:00:00', 1000);

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
(2, 1, 2, '2020-12-31 09:00:00', '2020-12-31 09:00:00'),
(3, 114, 157, '2017-12-31 09:00:00', '2017-12-31 09:00:00'),
(4, 64, 182, '2017-12-31 09:00:00', '2017-12-31 09:00:00'),
(5, 155, 121, '2017-12-31 09:00:00', '2017-12-31 09:00:00'),
(6, 64, 92, '2017-12-31 09:00:00', '2017-12-31 09:00:00'),
(7, 80, 182, '2017-12-31 09:00:00', '2017-12-31 09:00:00'),
(8, 51, 130, '2017-12-31 09:00:00', '2017-12-31 09:00:00'),
(9, 97, 153, '2017-12-31 09:00:00', '2017-12-31 09:00:00'),
(10, 172, 51, '2017-12-31 09:00:00', '2017-12-31 09:00:00'),
(11, 1, 70, '2019-12-31 09:00:00', '2019-12-31 11:00:00'),
(12, 11, 2, '2020-12-31 09:00:00', '2020-12-31 09:00:00'),
(22, 11, 2, '2020-12-31 09:00:00', '2020-12-31 09:00:00'),
(23, 172, 3, '2020-12-31 09:00:00', '2020-12-31 09:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `word_packs`
--

CREATE TABLE `word_packs` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `price` double(8,2) NOT NULL,
  `status` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `word_pairs`
--

CREATE TABLE `word_pairs` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `id_word_pack` bigint(20) UNSIGNED NOT NULL,
  `word_1` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `word_2` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `status` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_word_packs`
--
ALTER TABLE `user_word_packs`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `user_word_packs`
--
ALTER TABLE `user_word_packs`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
