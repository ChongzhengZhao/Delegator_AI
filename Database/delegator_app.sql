-- phpMyAdmin SQL Dump
-- version 4.4.15.10
-- https://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: 2020-09-27 14:58:43
-- 服务器版本： 5.7.30-log
-- PHP Version: 5.6.40

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `delegator_app`
--

-- --------------------------------------------------------

--
-- 表的结构 `tickets`
--

CREATE TABLE IF NOT EXISTS `tickets` (
  `id` int(11) NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `app_name` varchar(255) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `issue_type` varchar(30) NOT NULL,
  `impact_rank` varchar(10) NOT NULL,
  `description` text NOT NULL,
  `file` varchar(255) DEFAULT NULL,
  `assign_to_who` varchar(50) DEFAULT 'Pending',
  `status` varchar(20) DEFAULT 'In progress'
) ENGINE=InnoDB AUTO_INCREMENT=286 DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `tickets`
--

INSERT INTO `tickets` (`id`, `time`, `app_name`, `name`, `email`, `issue_type`, `impact_rank`, `description`, `file`, `assign_to_who`, `status`) VALUES
(280, '2020-09-27 05:20:54', 'Issue for the style of the website', 'John Wang', 'wang.john@google.com', 'Other', 'High', 'It’s really tough coming up with engaging ideas for your Facebook page when you’re not getting a response to any of them. Fewer interactions also means that your page loses algorithmic power and Facebook will show it to less of your fans. Facebook’s algorithm is set up to show posts you’ve liked to your friends. If you stop liking a page’s posts then your friends will stop seeing them too.', NULL, 'Alex', 'Resolved'),
(281, '2020-09-27 05:20:58', 'Urgent Water pipe burst', 'Alber', 'alber@gmail.com', 'Other', 'High', 'There is a burst water main or gushes of running water. A burst water main or large gushes of running water  be caused by pipe or hydrant damage. Could please help me to address this problem? Please! Be quick! There is a burst water main or gushes of running water. A burst water main or large gushes of running water  be caused by pipe or hydrant damage. Could please help me to address this problem? Please! Be quick!', NULL, 'David', 'Resolved'),
(282, '2020-09-27 05:19:59', 'I can''t visit the web page,please help me', 'Poppy', 'Poppy@gmail.com', 'Web Page Not Working', 'Medium', 'When I tried to access Google with my browser this morning, the page gave me an error message that I could not access it successfully. I checked my home network and everything is fine, but I just can''t access the page successfully with my browser. How do I deal with this and can you please help me quickly?', NULL, 'Marcus', 'In progress'),
(284, '2020-09-27 05:40:13', 'Android', 'Harshal', 'harshalshah71@gmail.com', '500 Internal Server Error', 'High', 'Internal Server Error\r\nThe server encountered an internal error or misconfiguration and was unable to complete your request. Please contact the server administrator webmaster@******.com and inform them of the time the error occurred and anything you might have done that may have caused the error. More information about this error may be available in the server error log.\r\nAdditionally, a 500 Internal Server Error was encountered while trying to use an ErrorDocument to handle the request.', NULL, 'Josh', 'In progress');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tickets`
--
ALTER TABLE `tickets`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id` (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tickets`
--
ALTER TABLE `tickets`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=286;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
