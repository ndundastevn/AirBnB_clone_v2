-- script prepares db server for project
-- create project dev db with specified name 
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create user with specified details 
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grant all privileges to specified user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- reload from disk, clear cache
FLUSH PRIVILEGES;
-- grant SELECT privilege to hbnb_dev performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- reload from disk, clear cache
FLUSH PRIVILEGES;
