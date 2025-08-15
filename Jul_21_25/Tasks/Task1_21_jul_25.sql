create database Library_Management_System;
use Library_Management_System;

create table members(
	member_id int primary key,
    name varchar(50),
    email varchar(50),
    join_date date
);

create table books(
	book_id int primary key,
    title varchar(50),
    genre varchar(50),
    author varchar(50),
    total_copies int
);

create table book_issues(
	issue_id int primary key,
    book_id int,
    member_id int,
    issue_date date,
    return_date date,
    foreign key (book_id) references books(book_id),
    foreign key (member_id) references members(member_id)
);

create table fines(
	fine_id int primary key,
    issue_id int,
    amount int,
    paid boolean,
    foreign key (issue_id) references book_issues(issue_id)
);

insert into  members (member_id, name, email, join_date) values
(1, 'Ravi Sharma', 'ravi.sharma@example.com', '2023-01-15'),
(2, 'Priya Desai', 'priya.desai@example.com', '2023-03-10'),
(3, 'Amit Verma', 'amit.verma@example.com', '2023-06-05'),
(4, 'Sneha Kapoor', 'sneha.kapoor@example.com', '2023-07-22'),
(5, 'Karan Joshi', 'karan.joshi@example.com', '2023-08-01');

insert into books (book_id, title, genre, author, total_copies) values
(101, 'Wings of Fire', 'Biography', 'A.P.J Abdul Kalam', 5),
(102, 'The White Tiger', 'Fiction', 'Aravind Adiga', 3),
(103, 'Think Like a Monk', 'Self-help', 'Jay Shetty', 4),
(104, 'The Guide', 'Fiction', 'R.K. Narayan', 2),
(105, 'India 2020', 'Non-fiction', 'A.P.J Abdul Kalam', 6);

insert into book_issues (issue_id, book_id, member_id, issue_date, return_date) values
(1001, 101, 1, '2023-07-01', '2023-07-15'),
(1002, 102, 2, '2023-07-05', NULL),
(1003, 103, 3, '2023-07-10', '2023-07-20'),
(1004, 104, 1, '2023-07-25', NULL),
(1005, 105, 4, '2023-08-01', '2023-08-20'),
(1006, 102, 5, '2023-08-05', NULL),
(1007, 103, 2, '2023-08-10', NULL);

insert into  fines (fine_id, issue_id, amount, paid) values
(1, 1001, 0, TRUE),
(2, 1002, 50, FALSE),
(3, 1003, 10, TRUE),
(4, 1004, 70, FALSE),
(5, 1005, 0, TRUE),
(6, 1006, 30, FALSE),
(7, 1007, 0, TRUE);

select * from members;

select * from books;

select * from book_issue;

select * from fines;
