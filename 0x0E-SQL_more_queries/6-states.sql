-- Script that creates the database hbtn_0d_usa and the table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use the new database
USE hbtn_0d_usa;
-- Create the table
CREATE TABLE IF NOT EXISTS states (id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, name VARCHAR(256) NOT NULL);
