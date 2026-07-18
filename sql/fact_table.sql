-- ==========================================
-- Fact Table: Sales
-- ==========================================

CREATE TABLE fact_sales (

    sales_key SERIAL PRIMARY KEY,

    order_id VARCHAR(30) NOT NULL,

    customer_key INT NOT NULL,
    product_key INT NOT NULL,
    location_key INT NOT NULL,
    date_key INT NOT NULL,
    shipping_key INT NOT NULL,

    sales NUMERIC(10,2),
    quantity INT,
    discount NUMERIC(5,2),
    profit NUMERIC(10,2),

    CONSTRAINT fk_customer
        FOREIGN KEY (customer_key)
        REFERENCES dim_customer(customer_key),

    CONSTRAINT fk_product
        FOREIGN KEY (product_key)
        REFERENCES dim_product(product_key),

    CONSTRAINT fk_location
        FOREIGN KEY (location_key)
        REFERENCES dim_location(location_key),

    CONSTRAINT fk_date
        FOREIGN KEY (date_key)
        REFERENCES dim_date(date_key),

    CONSTRAINT fk_shipping
        FOREIGN KEY (shipping_key)
        REFERENCES dim_shipping(shipping_key)
);