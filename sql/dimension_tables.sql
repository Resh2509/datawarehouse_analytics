-- ==========================================
-- Dimension: Customer
-- ==========================================

CREATE TABLE dim_customer (
    customer_key SERIAL PRIMARY KEY,
    customer_id VARCHAR(20) UNIQUE NOT NULL,
    customer_name VARCHAR(100),
    segment VARCHAR(50)
);
-- ==========================================
-- Dimension: Product
-- ==========================================

CREATE TABLE dim_product (
    product_key SERIAL PRIMARY KEY,
    product_id VARCHAR(30) UNIQUE NOT NULL,
    product_name VARCHAR(255),
    category VARCHAR(100),
    sub_category VARCHAR(100)
);
-- ==========================================
-- Dimension: Location
-- ==========================================

CREATE TABLE dim_location (
    location_key SERIAL PRIMARY KEY,
    country VARCHAR(100),
    state VARCHAR(100),
    city VARCHAR(100),
    region VARCHAR(100)
);
-- ==========================================
-- Dimension: Date
-- ==========================================

CREATE TABLE dim_date (
    date_key SERIAL PRIMARY KEY,
    order_date DATE UNIQUE,
    year INT,
    quarter INT,
    month INT,
    month_name VARCHAR(20),
    day INT,
    weekday VARCHAR(20)
);
-- ==========================================
-- Dimension: Shipping
-- ==========================================

CREATE TABLE dim_shipping (
    shipping_key SERIAL PRIMARY KEY,
    ship_mode VARCHAR(50) UNIQUE
);