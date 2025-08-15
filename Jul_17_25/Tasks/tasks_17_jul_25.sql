CREATE DATABASE students_db;

use students_db;

create table students_info (
	roll_num int primary key,
    first_name varchar(25),
    last_name varchar(25)
    );

create table marks (
	roll_num int,
	sub_id int,
	sub_name varchar(10),
    mark int,
	foreign key (roll_num) references students_info(roll_num)
    );

drop table marks;

insert into students_info values (1,'kuldeep','yadav'),(2,'vedant','kalal'),(3,'rahul','patel');
select * from students_info ;

insert into marks values (1,031,'maths',90),(2,031,'maths',60),(3,031,'maths',50);

select * from marks;
    
update students_info set first_name='kuldip' where roll_num = 1;

select * from students_info;