CREATE DATABASE expense_db;

USE expense_db;

CREATE TABLE category (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) UNIQUE
);

CREATE TABLE expense (
    expense_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT,
    amount DECIMAL(10,2),
    date DATE,
    description VARCHAR(100),
    FOREIGN KEY (category_id) REFERENCES category(category_id)
);

INSERT IGNORE INTO category (category_name)
VALUES ('Food'), ('Travel'), ('Bills'), ('Shopping'), ('Entertainment');
