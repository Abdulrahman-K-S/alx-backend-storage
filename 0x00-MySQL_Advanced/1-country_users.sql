-- Task 1. In and not out
-- Creates a table users that contains id, email, name,
-- and country enum attributes
CREATE TABLE IF NOT EXISTS users (
    id int NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL,
    PRIMARY KEY (id)
);