-- SQL Script to Initialize Database Schema

-- Create Categories Table
CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    url TEXT UNIQUE NOT NULL
);

-- Create Products Table
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price VARCHAR(50),
    rating FLOAT,
    category_id INT REFERENCES categories(id) ON DELETE CASCADE,
    UNIQUE(name, category_id)
);
