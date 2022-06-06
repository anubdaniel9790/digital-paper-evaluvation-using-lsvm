-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 03, 2022 at 07:32 PM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `python_digital_ai_exam`
--

-- --------------------------------------------------------

--
-- Table structure for table `question_details`
--

CREATE TABLE `question_details` (
  `id` int(100) NOT NULL,
  `staff` varchar(100) NOT NULL,
  `degree` varchar(100) NOT NULL,
  `department` varchar(100) NOT NULL,
  `year` varchar(100) NOT NULL,
  `semester` varchar(100) NOT NULL,
  `subject_code` varchar(100) NOT NULL,
  `subject_name` varchar(100) NOT NULL,
  `paper_code` varchar(100) NOT NULL,
  `no_of_qustions` varchar(100) NOT NULL,
  `mark_per_question` varchar(100) NOT NULL,
  `total_marks` varchar(100) NOT NULL,
  `qid` varchar(100) NOT NULL,
  `question` text NOT NULL,
  `keypoint` text NOT NULL,
  `mkey` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `report` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `question_details`
--

INSERT INTO `question_details` (`id`, `staff`, `degree`, `department`, `year`, `semester`, `subject_code`, `subject_name`, `paper_code`, `no_of_qustions`, `mark_per_question`, `total_marks`, `qid`, `question`, `keypoint`, `mkey`, `status`, `report`) VALUES
(2, 'yoga', 'be', 'cs', '1', '2', 'p1', 'python', 'p3439', '10', '5', '50', '2', 'Introduction to Python', 'Python was developed by Guido van Rossum and was released first on February 20', '-', '0', '0'),
(3, 'yoga', 'be', 'cs', '1', '2', 'p1', 'python', 'p3439', '10', '5', '50', '3', ' What is a dynamically typed language', 'Before we understand a dynamically typed language, we should learn about what typing is. Typing refers to type-checking in programming languages', '-', '0', '0'),
(4, 'yoga', 'be', 'cs', '1', '2', 'p1', 'python', 'p3439', '10', '5', '50', '4', ' What is an Interpreted language', 'An Interpreted language executes its statements line by line. Languages such as Python, Javascript, R, PHP, and Ruby are prime examples of Interpreted languages', '-', '0', '0'),
(5, 'yoga', 'be', 'cs', '1', '2', 'p1', 'python', 'p3439', '10', '5', '50', '5', 'What is Scope in Python', 'Every object in Python functions within a scope. A scope is a block of code where an object in Python remains relevant. Namespaces uniquely identify all the objects inside a program', '-', '0', '0'),
(6, 'yoga', 'be', 'cs', '1', '2', 'p1', 'python', 'p3439', '10', '5', '50', '6', 'What are lists and tuples', 'Lists and Tuples are both sequence data types that can store a collection of objects in Python. The objects stored in both sequences can have different data types.', '-', '0', '0'),
(7, 'yoga', 'be', 'cs', '1', '2', 'p1', 'python', 'p3439', '10', '5', '50', '7', 'What are lists and tuples', 'Lists and Tuples are both sequence data types that can store a collection of objects in Python. The objects stored in both sequences can have different data types.', '-', '0', '0'),
(8, 'yoga', 'be', 'cs', '1', '2', 'p1', 'python', 'p3439', '10', '5', '50', '8', 'What is pass in Python', 'The pass keyword represents a null operation in Python. It is generally used for the purpose of filling up empty blocks of code which may execute during runtime but has yet to be written.', '-', '0', '0'),
(9, 'yoga', 'be', 'cs', '1', '2', 'p1', 'python', 'p3439', '10', '5', '50', '9', 'What are modules and packages in Python', 'Python packages and Python modules are two mechanisms that allow for modular programming in Python. Modularizing has several advantages', '-', '0', '0'),
(10, 'yoga', 'be', 'cs', '1', '2', 'p1', 'python', 'p3439', '10', '5', '50', '10', 'What is the use of self in Python', 'Self is used to represent the instance of the class. With this keyword, you can access the attributes and methods of the class in python.', '-', '0', '0'),
(1, 'yoga', 'be', 'cs', '1', '2', 'p1', 'python', 'p3439', '1', '5', '50', '1', 'How do you copy an object in Python', ' the assignment statement  does not copy', '-', '0', '0');

-- --------------------------------------------------------

--
-- Table structure for table `staff_details`
--

CREATE TABLE `staff_details` (
  `staff_name` varchar(100) NOT NULL,
  `department` varchar(100) NOT NULL,
  `qualification` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `designation` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `report` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `staff_details`
--

INSERT INTO `staff_details` (`staff_name`, `department`, `qualification`, `gender`, `designation`, `email`, `username`, `password`, `status`, `report`) VALUES
('yoga', 'cs', 'me', 'Male', 'Associate professor', 'yoga@gmail.com', 'yoga', '123', '0', '0');

-- --------------------------------------------------------

--
-- Table structure for table `student_details`
--

CREATE TABLE `student_details` (
  `register_no` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `degree` varchar(100) NOT NULL,
  `department` varchar(100) NOT NULL,
  `dob` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `report` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student_details`
--

INSERT INTO `student_details` (`register_no`, `name`, `degree`, `department`, `dob`, `password`, `gender`, `status`, `report`) VALUES
('101', 'arun', 'be', 'cs', '14-07-1994', '123', 'Male', '0', '0');

-- --------------------------------------------------------

--
-- Table structure for table `student_exam_details`
--

CREATE TABLE `student_exam_details` (
  `id` int(100) NOT NULL,
  `subject_code` varchar(100) NOT NULL,
  `student` varchar(100) NOT NULL,
  `total_mark` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `report` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student_exam_details`
--

INSERT INTO `student_exam_details` (`id`, `subject_code`, `student`, `total_mark`, `status`, `report`) VALUES
(1, 'p2', '101', '6', '0', '0');
