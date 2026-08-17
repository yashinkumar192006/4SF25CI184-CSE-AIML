CREATE TABLE Department(
 department_id serial primary key, 
 department_name VARCHAR(30) not null UNIQUE
);

select*from Department

INSERT INTO Department (department_id, department_name)
VALUES
(1, 'HR'),
(2, 'IT'),
(3, 'Finance'),
(4, 'Sales');

CREATE TABLE Employee(
emp_id serial PRIMARY KEY,
emp_name varchar(20) not null,
gender VARCHAR(10) CHECK(gender IN ('Male','Female','other')),
age INT CHECK(age>=24),
hire_date DATE not null,
dept_id INT not null,
city VARCHAR(100) DEFAULT 'Bangalore',
salary INT NOT NULL,

)


INSERT INTO Employee (emp_id, emp_name, gender, age, hire_date, dept_id, city, salary)
VALUES
(101,'Amit Kumar','Male',  34,'2018-07-01', 2,'Hyderabad', 55000),
(102,'Sneha Reddy','Female',29, '2019-03-15', 1, 'Bangalore', 48000),
(103, 'Ravi Sharma','Male',  36,'2015-06-10', 3, 'Hyderabad', 62000),
(104,'Priya Singh','Female',27,'2020-01-20', 2 'Delhi', 51000),
(105, 'Karan Mehta','Male', 31, '2017-09-05', 4, 'Bangalore', 58000);


select * from Employee

select distinct department_name from Department

SELECT DISTINCT department_name
FROM Employee
JOIN Department
ON Employee.dept_id = Department.department_id;


from Employee
select * from Employee where salary >50000

select * from  Employee where dept_id = 2;

select * from Employee where salary between 50000 AND 60000 
select * from Employee where dept_id IN (2, 4)

select * from Employee
ORDER BY salary desc;

select * from  Employee
where (dept_id = 2 OR dept_id = 4)
  AND salary > 50000
  AND city <> 'Hyderabad'

SELECT emp_name, department_name
FROM Employee, Department
WHERE Employee.dept_id = Department.department_id;

alter table Employee
add dept_name varchar(30)

update employee set dept_name=Department.department_name
from Department
where Employee.dept_id= Department.department_id;



select distinct department_name , emp_name
from Employee
join Department on Employee.dept_id=Department.department_id

