CREATE SCHEMA `attendance` ;
CREATE TABLE `attendance`.`student` (
  `Dep` VARCHAR(45) NOT NULL,
  `Course` VARCHAR(45) NOT NULL,
  `Year` VARCHAR(45) NOT NULL,
  `StudentID` VARCHAR(45) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `RollNumber` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NULL,
  PRIMARY KEY (`StudentID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_cs_0900_ai_ci;
insert into `attendance`.`student`(Dep,Course,Year,StudentID,name,RollNumber,email)
values('IT','CS','2020-21','0','Adarsh Ranjan','111222345','adarsh@gmail.com'),
('Mechanical','BIO','2019-20','1','Raghuram Rajan','12387658','rajan@gmail.com'),
('Electrical','CS','2021-22','2','Selena Gomez','1744221','selena@facebook'),
('IT','MA','2022-23','3','Tom Cruise','17432752','tomcruise@hotmail.com');