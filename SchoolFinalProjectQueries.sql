
-- Select all students that are named Kole
SELECT * FROM student
WHERE FirstName = "Kole";

-- Count the amount of students ordered by their grade letter
-- This shows a sample of the performance in general of the school students, It is noticable that the student grades are distributed normaly

SELECT count(gradeletter) AS 'Student count', gradeletter, (100 / 2000 * COUNT(gradeletter)) AS Percentage
FROM gradeletter
GROUP BY gradeletter.GradeLetter;


-- Select many students had A on their Grade
SELECT ROW_NUMBER() OVER (ORDER BY FirstName, LastName) AS NumberOfStudents, FirstName, LastName, gradeletter
FROM student 
JOIN gradeletter ON student.GradeID = gradeletter.GradeID
WHERE gradeletter = 'A';


-- Select all the professors that their faculty is Computer Science
Select * FROM teacher
WHERE Department = "Computer Science";

-- This query provides the name, department, and date at which a teacher joined the school
-- given that they joined in January and that they are within the computer science department.
-- surprisingly there is 11 out of 50 theology professors
SELECT LastName, FirstName, Department, JoinDate FROM projectschool.teacher
WHERE JoinDate LIKE '%-01-%' AND Department = 'Computer Science';

-- Select and count the professors based on their faculty, And show the average of professors per department
SELECT COUNT(teacher.Department) AS 'Count of professors', teacher.Department, (100 / 50 * COUNT(teacher.Department)) AS Percentage 
FROM teacher
GROUP BY teacher.Department;

-- This query selects the teachers that their class is 490
SELECT teacher.FirstName, teacher.LastName, class.ClassName
FROM teacher, class
WHERE ClassName = '490';

-- Select all the exams and what type of exams there is on the school
SELECT class.ClassName, subject.SubjectName, exam.ExamName, examtype.TypeName
FROM class, exam, examtype, subject;

-- This query uses the average function to find the average grade amongst students within the school.
-- What this tells us is that the average grade in the school
SELECT 
    AVG(CASE 
            WHEN gradeletter.GradeLetter = 'A' THEN 4.0
            WHEN gradeletter.GradeLetter = 'B' THEN 3.6
            WHEN gradeletter.GradeLetter = 'C' THEN 2.8
            WHEN gradeletter.GradeLetter = 'D' THEN 1.7
            WHEN gradeletter.GradeLetter = 'F' THEN 0.8
            ELSE NULL 
        END) AS 'Average school GPA'
FROM 
    gradeletter;

-- This query uses a RIGHT JOIN to display the students' last names and first names along with their grade ID's.
SELECT student.LastName, student.FirstName, gradeletter.GradeID,Address
FROM gradeletter
RIGHT JOIN student ON gradeletter.GradeID = student.GradeID
ORDER BY student.LastName;

-- We created this trigger to prevent deletion in our GradeLetter table.
-- The goal here is to keep this table as it is and to ensure that nobody tampers with how the grades work.
DELIMITER //

CREATE TRIGGER glProtect 
	BEFORE UPDATE ON projectschool.gradeletter 
	FOR EACH ROW
	BEGIN
		DECLARE errorMSG VARCHAR(255);
        SET errorMSG = 'YOU ARE NOT PERMITTED TO DELETE INFORMATION FROM THIS TABLE';
		SIGNAL SQLSTATE '45000' 
			SET MESSAGE_TEXT = errorMSG;
	END //
DELIMITER ;

-- We created this trigger to update the schedule table whenever we want to update the Ending Date of the class to the current time
-- This would allow a user to quickly update the date of the end of the class, which would be useful in cases where the schedule is altered.
CREATE TRIGGER schedule_audit
	BEFORE UPDATE ON projectschool.schedule
	FOR EACH ROW
INSERT INTO teacher_audit
SET action = 'update',
	ScheduleID = OLD.ScheduleID,
    ZoomLink = OLD.ZoomLink,
    DateStart = OLD.DateStart,
    DateEnd = NOW(),
    ClassID = OLD.ClassID;

-- We created this stored procedure to help users quickly select all colleges in the College of Sciences.
DELIMITER //
CREATE PROCEDURE ClassSubject()
BEGIN
	SELECT SubjectName, SubjectCollege FROM projectschool.subject
	WHERE SubjectCollege = 'College of Sciences';
END //
DELIMITER ;

CALL ClassSubject();

-- We created users for both the principal of the school and a member of the IT department.
CREATE USER padilla@localhost IDENTIFIED BY '12345';
CREATE USER infotech@localhost IDENTIFIED BY '67890';

SELECT * FROM mysql.user;

-- We also gave the principal and the IT member all of the available priveleges to the class table.
GRANT ALL ON class TO padilla@localhost;
GRANT ALL ON class TO infotech@localhost;

-- The principal was fired, so we revoked his priveleges.
-- REVOKE ALL ON class FROM padilla@localhost;
-- DROP USER padilla@localhost;

-- We then added the newly-hired principal here and gave him class table priveleges.
CREATE USER newprincipal@localhost IDENTIFIED BY '12345';

