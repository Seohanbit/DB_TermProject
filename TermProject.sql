DROP DATABASE IF EXISTS  TermProject;
DROP USER IF EXISTS  TermProject@localhost;
create user TermProject@localhost identified WITH mysql_native_password  by '1234';
create database TermProject;
grant all privileges on TermProject.* to TermProject@localhost with grant option;
commit;
 
USE TermProject;

-- Table structure for table `student`
CREATE TABLE `student` (
  `Student_id` varchar(20) NOT NULL,
  `Password` bigint NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Phone` bigint NOT NULL,
  `Grade` int NOT NULL,
  `Major` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  PRIMARY KEY (`Student_id`)
);

-- Data for table `student`
INSERT INTO `student` VALUES 
('2019038016', 223, '최동진', 1080077235, 3, '소프트웨어학과', 'cdj7235@naver.com'),
('2019038043', 627, '서한빛', 1099397036, 3, '소프트웨어학과', 'hanbit0627@gmail.com');

-- Table structure for table `prof`
CREATE TABLE `prof` (
  `Prof_id` varchar(20) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Major` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  PRIMARY KEY (`Prof_id`)
);

-- Data for table `prof`
INSERT INTO `prof` VALUES 
('P201', 'Prof Smith', 'Computer Science', 'smith@example.com'),
('P202', 'Prof Johnson', 'Computer Science', 'johnson@example.com'),
('P203','Prof Williams','Computer Science','williams@example.com'),
('P204','Prof Brown','Computer Science','brown@example.com'),
('P205','Prof Jones','Mathematics','jones@example.com'),
('P206','Prof Davis','Mathematics','davis@example.com'),
('P207','Prof Miller','Psychology','miller@example.com'),
('P208','Prof Wilson','Psychology','wilson@example.com'),
('P209','Prof Moore','Chemistry','moore@example.com'),
('P210','Prof Taylor','Chemistry','taylor@example.com'),
('P211','Prof Anderson','History','anderson@example.com'),
('P212','Prof Martinez','History','martinez@example.com'),
('P213','Prof Jackson','Environmental Science','jackson@example.com'),
('P214','Prof White','Environmental Science','white@example.com'),
('P215','Prof Harris','Business','harris@example.com'),
('P216','Prof Martin','Business','martin@example.com'),
('P217','Prof Thompson','Language','thompson@example.com'),
('P218','Prof Garcia','Language','garcia@example.com'),
('P219','Prof Martinez','Art','martinez@example.com'),
('P220','Prof Robinson','Art','robinson@example.com');

-- Table structure for table `class`
CREATE TABLE `class` (
  `Class_id` bigint NOT NULL,
  `C_Group` int NOT NULL,
  `C_Name` varchar(100) NOT NULL,
  `Class_day` varchar(255) NOT NULL,
  `Grade` int NOT NULL,
  `Current_std` int NOT NULL,
  `Max_std` int NOT NULL,
  `Major` varchar(50) NOT NULL,
  `Division` varchar(20) NOT NULL,
  `Prof_id` varchar(20) DEFAULT NULL,
  `Class_room` varchar(20) NOT NULL,
  PRIMARY KEY (`Class_id`),
  KEY `fk_Prof` (`Prof_id`),
  CONSTRAINT `fk_Prof` FOREIGN KEY (`Prof_id`) REFERENCES `prof` (`Prof_id`)
);

-- Data for table `class`
INSERT INTO `class` VALUES 
(22, 1, 'Introduction to Computer Science', 'Monday 09:00', 1, 0, 35, 'software', 'specialty', 'P201', 'Room201'),
(23, 2, 'Introduction to Computer Science', 'Monday 10:00', 1, 0, 38, 'software', 'specialty', 'P202', 'Room202'),
(24,1,'Data Structures','Tuesday 09:00',2,0,40,'computer','all','P203','Room203'),
(25,2,'Data Structures','Tuesday 10:00',2,0,32,'computer','all','P204','Room204'),
(26,1,'Linear Algebra','Wednesday 09:00',1,0,30,'all','specialty','P205','Room205'),
(27,2,'Linear Algebra','Wednesday 10:00',1,0,38,'all','specialty','P206','Room206'),
(28,1,'Introduction to Psychology','Thursday 09:00',1,0,37,'software','all','P207','Room207'),
(29,2,'Introduction to Psychology','Thursday 10:00',1,0,40,'software','all','P208','Room208'),
(30,1,'Organic Chemistry','Friday 09:00',2,0,30,'computer','specialty','P209','Room209'),
(31,2,'Organic Chemistry','Friday 10:00',2,0,35,'computer','specialty','P210','Room210'),
(32,1,'World History','Monday 11:00',3,0,32,'all','all','P211','Room211'),
(33,2,'World History','Monday 12:00',3,0,38,'all','all','P212','Room212'),
(34,1,'Environmental Science','Tuesday 11:00',2,0,34,'software','all','P213','Room213'),
(35,2,'Environmental Science','Tuesday 12:00',2,0,39,'software','all','P214','Room214'),
(36,1,'Introduction to Business','Wednesday 11:00',1,0,31,'computer','specialty','P215','Room215'),
(37,2,'Introduction to Business','Wednesday 12:00',1,0,40,'computer','specialty','P216','Room216'),
(38,1,'Spanish Language','Thursday 11:00',2,0,35,'all','all','P217','Room217'),
(39,2,'Spanish Language','Thursday 12:00',2,0,30,'all','all','P218','Room218'),
(40,1,'Introduction to Art','Friday 11:00',1,0,38,'software','all','P219','Room219'),
(41,2,'Introduction to Art','Friday 12:00',1,0,32,'software','all','P220','Room220'),
(42,1,'Introduction to Sociology','Friday 13:00',2,0,35,'Sociology','Lecture','P213','Room221'),
(43,2,'Introduction to Sociology','Friday 14:00',2,0,40,'Sociology','Lecture','P214','Room222'),
(44,1,'Calculus I','Monday 13:00',1,0,32,'Mathematics','Lecture','P211','Room223'),
(45,2,'Calculus I','Monday 14:00',1,0,38,'Mathematics','Lecture','P212','Room224'),
(46,1,'Introduction to Physics','Tuesday 13:00',2,0,34,'Physics','Lab','P209','Room225'),
(47,2,'Introduction to Physics','Tuesday 14:00',2,0,39,'Physics','Lab','P210','Room226'),
(48,1,'Digital Marketing','Wednesday 13:00',3,0,31,'Marketing','Lecture','P213','Room227'),
(49,2,'Digital Marketing','Wednesday 14:00',3,0,40,'Marketing','Lecture','P214','Room228'),
(50,1,'Music Appreciation','Thursday 13:00',1,0,35,'Music','Lecture','P215','Room229'),
(51,2,'Music Appreciation','Thursday 14:00',1,0,30,'Music','Lecture','P216','Room230'),
(52,1,'Introduction to Computer Science','Friday 15:00',1,0,38,'software','specialty','P201','Room231'),
(53,2,'Introduction to Computer Science','Friday 16:00',1,0,32,'software','specialty','P202','Room232'),
(54,1,'Data Structures','Monday 15:00',2,0,40,'computer','all','P203','Room233'),
(55,2,'Data Structures','Monday 16:00',2,0,35,'computer','all','P204','Room234'),
(56,1,'Linear Algebra','Tuesday 15:00',1,0,30,'all','specialty','P205','Room235'),
(57,2,'Linear Algebra','Tuesday 16:00',1,0,38,'all','specialty','P206','Room236'),
(58,1,'Introduction to Psychology','Wednesday 15:00',1,0,37,'software','all','P207','Room237'),
(59,2,'Introduction to Psychology','Wednesday 16:00',1,0,40,'software','all','P208','Room238'),
(60,1,'Organic Chemistry','Thursday 15:00',2,0,30,'computer','specialty','P209','Room239'),
(61,2,'Organic Chemistry','Thursday 16:00',2,0,35,'computer','specialty','P210','Room240');

-- Table structure for table `r_basket`
CREATE TABLE `r_basket` (
  `Basket_id` varchar(50) NOT NULL,
  `Student_id` varchar(20) DEFAULT NULL,
  `Class_id` bigint DEFAULT NULL,
  PRIMARY KEY (`Basket_id`),
  KEY `fk_Student_R_basket` (`Student_id`),
  KEY `fk_Class_R_basket` (`Class_id`),
  CONSTRAINT `fk_Class_R_basket` FOREIGN KEY (`Class_id`) REFERENCES `class` (`Class_id`),
  CONSTRAINT `fk_Student_R_basket` FOREIGN KEY (`Student_id`) REFERENCES `student` (`Student_id`)
);

-- Table structure for table `course_registration`
CREATE TABLE `course_registration` (
  `Registration_id` varchar(50) NOT NULL,
  `Student_id` varchar(20) DEFAULT NULL,
  `Class_id` bigint DEFAULT NULL,
  PRIMARY KEY (`Registration_id`),
  KEY `fk_Student` (`Student_id`),
  KEY `fk_Class` (`Class_id`),
  CONSTRAINT `fk_Class` FOREIGN KEY (`Class_id`) REFERENCES `class` (`Class_id`),
  CONSTRAINT `fk_Student` FOREIGN KEY (`Student_id`) REFERENCES `student` (`Student_id`)
);
