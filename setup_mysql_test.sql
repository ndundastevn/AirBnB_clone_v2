-- prepares a MySQL server for AirBnB_v2 project
-- create project test db as specified
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create user with details as specified
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grants all privileges to specified user
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
-- grants the SELECT privilege on db performance_schema
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
-- reload privileges from disk, clear cache
FLUSH PRIVILEGES;
