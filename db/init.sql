CREATE DATABASE IF NOT EXISTS thinkon;
USE thinkon;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);

INSERT INTO users (name) VALUES ('Chris'), ('Pat');
