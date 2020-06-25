-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 25, 2020 at 10:08 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.3.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `round`
--

-- --------------------------------------------------------

--
-- Table structure for table `game_round`
--

CREATE TABLE `game_round` (
  `id` int(11) NOT NULL,
  `id_game` int(11) NOT NULL,
  `round` int(11) NOT NULL,
  `word_1` varchar(20) NOT NULL,
  `word_2` varchar(20) NOT NULL,
  `num_mr_white` int(11) NOT NULL,
  `num_civilian` int(11) NOT NULL,
  `num_undercover` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `round_detail`
--

CREATE TABLE `round_detail` (
  `id` int(11) NOT NULL,
  `id_round` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `id_role` int(11) NOT NULL,
  `condition` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `turn_detail`
--

CREATE TABLE `turn_detail` (
  `id` int(11) NOT NULL,
  `id_round_detail` int(11) NOT NULL,
  `turn` int(11) NOT NULL,
  `user_word` varchar(10) NOT NULL,
  `user_desc` varchar(20) NOT NULL,
  `user_vote` int(11) NOT NULL,
  `status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `game_round`
--
ALTER TABLE `game_round`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `round_detail`
--
ALTER TABLE `round_detail`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `turn_detail`
--
ALTER TABLE `turn_detail`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `game_round`
--
ALTER TABLE `game_round`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `round_detail`
--
ALTER TABLE `round_detail`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `turn_detail`
--
ALTER TABLE `turn_detail`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
