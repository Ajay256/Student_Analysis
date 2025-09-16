-- Insert Teachers
INSERT INTO teachers (name, email) VALUES
('Mr. Sharma','sharma@university.edu'),
('Ms. Gupta','gupta@university.edu'),
('Mr. Verma','verma@university.edu'),
('Ms. Singh','singh@university.edu'),
('Mr. Rao','rao@university.edu');

-- Insert Subjects
INSERT INTO subjects (subject_name, teacher_name) VALUES
('Python','Mr. Sharma'),
('AI Basics','Ms. Gupta'),
('DBMS','Mr. Verma'),
('Data Analysis','Ms. Singh'),
('Statistics','Mr. Rao');

-- Insert Students (10 example, extendable to 100+)
INSERT INTO students (name, roll_no, class, semester) VALUES
('Ajay Verma','MBA101','MBA-IT',1),
('Ravi Kumar','MBA102','MBA-IT',1),
('Neha Singh','MBA103','MBA-IT',1),
('Simran Kaur','MBA104','MBA-IT',1),
('Amit Sharma','MBA105','MBA-IT',1),
('Pooja Jain','MBA106','MBA-IT',1),
('Rahul Gupta','MBA107','MBA-IT',1),
('Sakshi Verma','MBA108','MBA-IT',1),
('Karan Mehta','MBA109','MBA-IT',1),
('Anjali Reddy','MBA110','MBA-IT',1);

-- Insert Performance (5 subjects x 10 students example)
INSERT INTO performance (student_id, subject_id, semester, marks, attendance) VALUES
(1,1,1,85,90),(1,2,1,78,95),(1,3,1,80,92),(1,4,1,88,90),(1,5,1,70,85),
(2,1,1,72,88),(2,2,1,65,80),(2,3,1,70,75),(2,4,1,60,85),(2,5,1,78,80),
(3,1,1,90,95),(3,2,1,85,90),(3,3,1,80,88),(3,4,1,92,96),(3,5,1,75,90);
-- Extend similar entries for all students and semesters
