use Library_Management_System;

-- List members who have borrowed more than 1 book:
SELECT m.name, COUNT(bi.issue_id) as books_borrowed
FROM members as m
JOIN book_issues as bi ON m.member_id = bi.member_id
GROUP BY m.name
HAVING COUNT(bi.issue_id) > 1;

--  List books that have been issued more than once.
SELECT b.title, COUNT(bi.issue_id) as times_issued
FROM books as b
JOIN book_issues as bi ON b.book_id = bi.book_id
GROUP BY b.title
HAVING COUNT(bi.issue_id) > 1;

-- Books that were issued but not returned
SELECT m.name,b.title 
FROM books as b
JOIN book_issues as bi on b.book_id = bi.book_id
JOIN members as m ON bi.member_id = m.member_id
WHERE bi.return_date IS NULL;


-- Members with total unpaid fine greater than 50
SELECT m.name, SUM(f.amount) AS total_unpaid
FROM members as m
JOIN book_issues as bi ON m.member_id = bi.member_id
JOIN fines as f ON bi.issue_id = f.issue_id
WHERE f.paid = FALSE
GROUP BY m.name
HAVING SUM(f.amount)>50;



