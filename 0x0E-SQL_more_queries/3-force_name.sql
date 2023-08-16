-- script that creates the table force_name --
SET @db_name = 'your_database_name';

-- Create table force_name if it doesn't exist
CREATE TABLE IF NOT EXISTS `force_name` (
    `id` INT PRIMARY KEY,
    `name` VARCHAR(256) NOT NULL
) ENGINE=InnoDB;

-- Use the specified database
USE @db_name;

-- Show table information
DESCRIBE force_name;
