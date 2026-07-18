-- =====================================================
-- BUSINESS KPI 1: Total Sales
-- =====================================================

SELECT
    ROUND(SUM(sales), 2) AS total_sales
FROM fact_sales;
-- =====================================================
-- BUSINESS KPI 2: Total Profit
-- =====================================================

SELECT
    ROUND(SUM(profit), 2) AS total_profit
FROM fact_sales;
-- =====================================================
-- BUSINESS KPI 3: Total Orders
-- =====================================================

SELECT COUNT(DISTINCT order_id) AS total_orders
FROM fact_sales;
-- =====================================================
-- BUSINESS KPI 4: Total Customers
-- =====================================================

SELECT COUNT(*) AS total_customers
FROM dim_customer;
-- =====================================================
-- BUSINESS KPI 5: Average Order Value
-- =====================================================

SELECT
ROUND(SUM(sales)/COUNT(DISTINCT order_id),2)
AS average_order_value
FROM fact_sales;
-- =====================================================
-- Top 10 Products by Sales
-- =====================================================

SELECT
p.product_name,
ROUND(SUM(f.sales),2) AS total_sales

FROM fact_sales f

JOIN dim_product p
ON f.product_key=p.product_key

GROUP BY p.product_name

ORDER BY total_sales DESC

LIMIT 10;
-- =====================================================
-- Top 10 Products by Profit
-- =====================================================

SELECT

p.product_name,

ROUND(SUM(f.profit),2) AS total_profit

FROM fact_sales f

JOIN dim_product p
ON f.product_key=p.product_key

GROUP BY p.product_name

ORDER BY total_profit DESC

LIMIT 10;
-- =====================================================
-- Sales by Category
-- =====================================================

SELECT

p.category,

ROUND(SUM(f.sales),2) AS total_sales

FROM fact_sales f

JOIN dim_product p
ON f.product_key=p.product_key

GROUP BY p.category

ORDER BY total_sales DESC;
-- =====================================================
-- Sales by Sub Category
-- =====================================================

SELECT

p.sub_category,

ROUND(SUM(f.sales),2) AS total_sales

FROM fact_sales f

JOIN dim_product p
ON f.product_key=p.product_key

GROUP BY p.sub_category

ORDER BY total_sales DESC;
-- =====================================================
-- Top 10 Customers by Revenue
-- =====================================================

SELECT

c.customer_name,

ROUND(SUM(f.sales),2) AS revenue

FROM fact_sales f

JOIN dim_customer c
ON f.customer_key=c.customer_key

GROUP BY c.customer_name

ORDER BY revenue DESC

LIMIT 10;
-- =====================================================
-- Customer Segment Performance
-- =====================================================

SELECT

c.segment,

ROUND(SUM(f.sales),2) AS total_sales,

ROUND(SUM(f.profit),2) AS total_profit

FROM fact_sales f

JOIN dim_customer c
ON f.customer_key=c.customer_key

GROUP BY c.segment

ORDER BY total_sales DESC;
-- =====================================================
-- Sales by Region
-- =====================================================

SELECT

l.region,

ROUND(SUM(f.sales),2) AS sales

FROM fact_sales f

JOIN dim_location l
ON f.location_key=l.location_key

GROUP BY l.region

ORDER BY sales DESC;
-- =====================================================
-- Top States by Sales
-- =====================================================

SELECT

l.state,

ROUND(SUM(f.sales),2) AS sales

FROM fact_sales f

JOIN dim_location l
ON f.location_key=l.location_key

GROUP BY l.state

ORDER BY sales DESC

LIMIT 10;
-- =====================================================
-- Top Cities by Sales
-- =====================================================

SELECT

l.city,

ROUND(SUM(f.sales),2) AS sales

FROM fact_sales f

JOIN dim_location l
ON f.location_key=l.location_key

GROUP BY l.city

ORDER BY sales DESC

LIMIT 10;
-- =====================================================
-- Monthly Sales Trend
-- =====================================================

SELECT

d.year,

d.month_name,

ROUND(SUM(f.sales),2) AS sales

FROM fact_sales f

JOIN dim_date d
ON f.date_key=d.date_key

GROUP BY d.year,d.month,d.month_name

ORDER BY d.year,d.month;
-- =====================================================
-- Yearly Sales
-- =====================================================

SELECT

d.year,

ROUND(SUM(f.sales),2) AS sales

FROM fact_sales f

JOIN dim_date d
ON f.date_key=d.date_key

GROUP BY d.year

ORDER BY d.year;
-- =====================================================
-- Quarterly Sales
-- =====================================================

SELECT

d.year,

d.quarter,

ROUND(SUM(f.sales),2) AS sales

FROM fact_sales f

JOIN dim_date d
ON f.date_key=d.date_key

GROUP BY d.year,d.quarter

ORDER BY d.year,d.quarter;
-- =====================================================
-- Shipping Mode Performance
-- =====================================================

SELECT

s.ship_mode,

ROUND(SUM(f.sales),2) AS total_sales,

ROUND(SUM(f.profit),2) AS total_profit

FROM fact_sales f

JOIN dim_shipping s
ON f.shipping_key=s.shipping_key

GROUP BY s.ship_mode

ORDER BY total_sales DESC;