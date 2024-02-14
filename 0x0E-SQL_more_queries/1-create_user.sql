-- Creates user_0d_1 to MySQL server
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grant all privileges to all user_0d_1_pwd
GRANT ALL PRIVILEGES ON *.* To 'user_0d_1'@'localhost' ;