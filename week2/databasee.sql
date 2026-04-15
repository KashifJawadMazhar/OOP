-- create database (ignored in SQLite but ok for MySQL)
CREATE DATABASE LibraryDB;
USE LibraryDB;

-- create authors table
CREATE TABLE Authors (
    author_id INT PRIMARY KEY,
    name VARCHAR(50)
);

-- create books table
CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(100),
    author_id INT,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

-- insert authors
INSERT INTO Authors VALUES (1, 'John Smith');
INSERT INTO Authors VALUES (2, 'Emily Rose');

-- insert books
INSERT INTO Books VALUES (101, 'Python Basics', 1);
INSERT INTO Books VALUES (102, 'AI for Beginners', 2);

-- select books with author names
SELECT Books.title, Authors.name
FROM Books
JOIN Authors ON Books.author_id = Authors.author_id;