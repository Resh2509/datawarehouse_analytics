CREATE OR REPLACE VIEW vw_sales_summary AS
SELECT
    f.order_id,
    d.order_date,
    d.year,
    d.month_name,
    c.customer_name,
    c.segment,
    p.product_name,
    p.category,
    p.sub_category,
    l.country,
    l.state,
    l.city,
    l.region,
    s.ship_mode,
    f.sales,
    f.quantity,
    f.discount,
    f.profit
FROM fact_sales f
JOIN dim_customer c ON f.customer_key = c.customer_key
JOIN dim_product p ON f.product_key = p.product_key
JOIN dim_location l ON f.location_key = l.location_key
JOIN dim_date d ON f.date_key = d.date_key
JOIN dim_shipping s ON f.shipping_key = s.shipping_key;
CREATE OR REPLACE VIEW vw_product_performance AS
SELECT
    p.product_name,
    p.category,
    p.sub_category,
    SUM(f.sales) AS total_sales,
    SUM(f.profit) AS total_profit,
    SUM(f.quantity) AS total_quantity
FROM fact_sales f
JOIN dim_product p
ON f.product_key = p.product_key
GROUP BY
p.product_name,
p.category,
p.sub_category;
CREATE OR REPLACE VIEW vw_customer_performance AS
SELECT
    c.customer_name,
    c.segment,
    SUM(f.sales) AS total_sales,
    SUM(f.profit) AS total_profit
FROM fact_sales f
JOIN dim_customer c
ON f.customer_key = c.customer_key
GROUP BY
c.customer_name,
c.segment;
CREATE OR REPLACE VIEW vw_region_performance AS
SELECT
    l.country,
    l.state,
    l.city,
    l.region,
    SUM(f.sales) AS total_sales,
    SUM(f.profit) AS total_profit
FROM fact_sales f
JOIN dim_location l
ON f.location_key = l.location_key
GROUP BY
l.country,
l.state,
l.city,
l.region;
CREATE OR REPLACE VIEW vw_time_analysis AS
SELECT
    d.year,
    d.quarter,
    d.month,
    d.month_name,
    SUM(f.sales) AS total_sales,
    SUM(f.profit) AS total_profit
FROM fact_sales f
JOIN dim_date d
ON f.date_key = d.date_key
GROUP BY
d.year,
d.quarter,
d.month,
d.month_name;