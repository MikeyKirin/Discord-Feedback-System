DROP DATABASE IF EXISTS yafsDB;

CREATE DATABASE yafsDB;

\c yafsDB

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    userID BIGINT,
    username VARCHAR(255),
    contact INTEGER,
    email VARCHAR(255),
    feedback_desc VARCHAR(5000),
    created_at DATE,
    is_public VARCHAR(255)
);
