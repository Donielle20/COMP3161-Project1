-- Group 11
-- 620126475
-- 620138478
-- 620109436
-- 620147266
-- 620141763

DROP DATABASE registry;

CREATE DATABASE registry;

USE registry;

CREATE TABLE students (
	stud_id INTEGER(5) PRIMARY KEY,
	first_name varchar(50),
	last_name(50),
	stud_email varchar(30),
	stud_password varchar(30)
);

