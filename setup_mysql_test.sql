-- Create database hbnb_test_db if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create user hbnb_test@localhost if it doesn't exist
CREATE USER IF NOT EXISTS hbnb_test@localhost IDENTIFIED WITH mysql_native_password BY 'hbnb_test_pwd';

-- Grant all privileges hbnb_test_db to hbnb_test@localhost
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO hbnb_test@localhost;

-- Grant SELECT privilege on performance_schema to hbnb_test@localhost
GRANT SELECT ON performance_schema.* TO hbnb_test@localhost;
