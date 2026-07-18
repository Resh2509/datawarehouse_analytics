-- ==========================================
-- Indexes for Performance
-- ==========================================

CREATE INDEX idx_customer
ON fact_sales(customer_key);

CREATE INDEX idx_product
ON fact_sales(product_key);

CREATE INDEX idx_location
ON fact_sales(location_key);

CREATE INDEX idx_date
ON fact_sales(date_key);

CREATE INDEX idx_shipping
ON fact_sales(shipping_key);

CREATE INDEX idx_order
ON fact_sales(order_id);