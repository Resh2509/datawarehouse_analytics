import psycopg2
from psycopg2.extras import execute_values
import pandas as pd
from config import DB_CONFIG


# ==========================================================
# DATABASE CONNECTION
# ==========================================================

def get_connection():
    return psycopg2.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        database=DB_CONFIG["database"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"]
    )


# ==========================================================
# LOAD CUSTOMER DIMENSION
# ==========================================================

def load_dim_customer(conn, df):

    rows = list(
        df[
            ["Customer.ID", "Customer.Name", "Segment"]
        ].itertuples(index=False, name=None)
    )

    cur = conn.cursor()

    execute_values(
        cur,
        """
        INSERT INTO dim_customer
        (customer_id, customer_name, segment)
        VALUES %s
        ON CONFLICT (customer_id) DO NOTHING
        """,
        rows
    )

    conn.commit()
    cur.close()

    print("✓ dim_customer loaded")


# ==========================================================
# LOAD PRODUCT DIMENSION
# ==========================================================

def load_dim_product(conn, df):

    rows = list(
        df[
            ["Product.ID",
             "Product.Name",
             "Category",
             "Sub.Category"]
        ].itertuples(index=False, name=None)
    )

    cur = conn.cursor()

    execute_values(
        cur,
        """
        INSERT INTO dim_product
        (product_id, product_name, category, sub_category)
        VALUES %s
        ON CONFLICT (product_id) DO NOTHING
        """,
        rows
    )

    conn.commit()
    cur.close()

    print("✓ dim_product loaded")


# ==========================================================
# LOAD LOCATION DIMENSION
# ==========================================================

def load_dim_location(conn, df):

    rows = list(
        df[
            ["Country",
             "State",
             "City",
             "Region"]
        ].itertuples(index=False, name=None)
    )

    cur = conn.cursor()

    execute_values(
        cur,
        """
        INSERT INTO dim_location
        (country, state, city, region)
        VALUES %s
        """,
        rows
    )

    conn.commit()
    cur.close()

    print("✓ dim_location loaded")


# ==========================================================
# LOAD SHIPPING DIMENSION
# ==========================================================

def load_dim_shipping(conn, df):

    rows = list(
        df[
            ["Ship.Mode"]
        ].itertuples(index=False, name=None)
    )

    cur = conn.cursor()

    execute_values(
        cur,
        """
        INSERT INTO dim_shipping
        (ship_mode)
        VALUES %s
        ON CONFLICT (ship_mode) DO NOTHING
        """,
        rows
    )

    conn.commit()
    cur.close()

    print("✓ dim_shipping loaded")


# ==========================================================
# LOAD DATE DIMENSION
# ==========================================================

def load_dim_date(conn, df):

    rows = list(
        df[
            [
                "Order.Date",
                "Year",
                "Quarter",
                "Month",
                "Month_Name",
                "Day",
                "Weekday"
            ]
        ].itertuples(index=False, name=None)
    )

    cur = conn.cursor()

    execute_values(
        cur,
        """
        INSERT INTO dim_date
        (
        order_date,
        year,
        quarter,
        month,
        month_name,
        day,
        weekday
        )
        VALUES %s
        ON CONFLICT (order_date) DO NOTHING
        """,
        rows
    )

    conn.commit()
    cur.close()

    print("✓ dim_date loaded")


# ==========================================================
# BUILD FACT TABLE USING DATABASE KEYS
# ==========================================================

def build_fact_table(conn, df):

    customer = pd.read_sql("""
        SELECT customer_key,
               customer_id
        FROM dim_customer
    """, conn)

    product = pd.read_sql("""
        SELECT product_key,
               product_id
        FROM dim_product
    """, conn)

    location = pd.read_sql("""
        SELECT location_key,
               country,
               state,
               city,
               region
        FROM dim_location
    """, conn)

    shipping = pd.read_sql("""
        SELECT shipping_key,
               ship_mode
        FROM dim_shipping
    """, conn)

    dates = pd.read_sql("""
        SELECT date_key,
               order_date
        FROM dim_date
    """, conn)

    dates["order_date"] = pd.to_datetime(dates["order_date"])

    fact = df.copy()

    fact["Order.Date"] = pd.to_datetime(fact["Order.Date"])

    fact = fact.merge(
        customer,
        left_on="Customer.ID",
        right_on="customer_id"
    )

    fact = fact.merge(
        product,
        left_on="Product.ID",
        right_on="product_id"
    )

    fact = fact.merge(
        location,
        left_on=["Country","State","City","Region"],
        right_on=["country","state","city","region"]
    )

    fact = fact.merge(
        shipping,
        left_on="Ship.Mode",
        right_on="ship_mode"
    )

    fact = fact.merge(
        dates,
        left_on="Order.Date",
        right_on="order_date"
    )

    fact = fact[
        [
            "Order.ID",
            "customer_key",
            "product_key",
            "location_key",
            "date_key",
            "shipping_key",
            "Sales",
            "Quantity",
            "Discount",
            "Profit"
        ]
    ]

    return fact


# ==========================================================
# LOAD FACT TABLE
# ==========================================================

def load_fact_sales(conn, fact):

    rows = list(fact.itertuples(index=False, name=None))

    cur = conn.cursor()

    execute_values(
        cur,
        """
        INSERT INTO fact_sales
        (
        order_id,
        customer_key,
        product_key,
        location_key,
        date_key,
        shipping_key,
        sales,
        quantity,
        discount,
        profit
        )
        VALUES %s
        """,
        rows
    )

    conn.commit()
    cur.close()

    print("✓ fact_sales loaded")