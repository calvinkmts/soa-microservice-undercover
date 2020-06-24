-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 23, 2020 at 01:55 PM
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
(1, 'k.koesoemo@ymail.com', '1234', 'kevin', 'M', '2020-01-01', 'CREATED', '2020-12-31 09:00:00', '2020-12-31 09:00:00', 1000),
(2, 'devphil@yahoo.ca', '6b75789a3c2415f290139923f8fbc0f2', 'Alexandra Lutz', 'F', '2002-10-05', 'ACTIVE', '2017-12-31 09:00:00', '2017-12-31 09:00:00', 0),
(3, 'barnett@me.com', 'c3faad0e29c54860c92cf1ec20f4fdbf', 'Leonidas Hughes', 'F', '1982-07-23', 'ACTIVE', '2017-12-31 09:00:00', '2017-12-31 09:00:00', 0),
(4, 'shaffei@mac.com', '457e05ded2ce000f8819a281a16f1f8d', 'Marquis Marks', 'M', '1994-09-24', 'ACTIVE', '2017-12-31 09:00:00', '2017-12-31 09:00:00', 0),
(5, 'hamilton@yahoo.com', '5ea15d8c1b66320049b07e6eeb9963c4', 'Aidan Krueger', 'F', '1975-09-02', 'CREATED', '2017-12-31 09:00:00', '2017-12-31 09:00:00', 0),
(6, 'murdocj@comcast.net', '2203d3a1fcdf34da8ed34ab3d412417e', 'Rebekah Berger', 'F', '1997-05-14', 'ACTIVE', '2017-12-31 09:00:00', '2017-12-31 09:00:00', 0),
(7, 'milton@hotmail.com', 'c0c9151335f96f90667ef358d0b7af57', 'Mattie Fields', 'F', '2007-06-04', 'CREATED', '2017-12-31 09:00:00', '2017-12-31 09:00:00', 0),
(8, 'debest@live.com', '6eb8a30ea9720627ccf5af22efd541f8', 'Celeste Parsons', 'M', '1957-04-22', 'CREATED', '2017-12-31 09:00:00', '2017-12-31 09:00:00', 0),
(9, 'gknauss@outlook.com', '4bebd505c66aca1a4432715c74451b53', 'Jamar Armstrong', 'M', '2009-04-05', 'ACTIVE', '2017-12-31 09:00:00', '2017-12-31 09:00:00', 0),
(10, 'fglock@icloud.com', '0cbdcd9b8edc83e3cfc790f8ef9dc98b', 'Nelson Bolton', 'M', '1951-05-31', 'ACTIVE', '2017-12-31 09:00:00', '2017-12-31 09:00:00', 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
