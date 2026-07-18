from extract import extract_data
from transform import transform_data

from load import (
    get_connection,
    load_dim_customer,
    load_dim_product,
    load_dim_location,
    load_dim_shipping,
    load_dim_date,
    build_fact_table,
    load_fact_sales
)


def main():

    print("=" * 60)
    print("DATA WAREHOUSE ETL PIPELINE")
    print("=" * 60)

    # ---------------------------------------
    # STEP 1 - Extract
    # ---------------------------------------
    print("\n[1] Extracting data...")
    df = extract_data()

    # ---------------------------------------
    # STEP 2 - Transform
    # ---------------------------------------
    print("\n[2] Transforming data...")
    (
        dim_customer,
        dim_product,
        dim_location,
        dim_shipping,
        dim_date,
        raw_df
    ) = transform_data(df)

    # ---------------------------------------
    # STEP 3 - Connect PostgreSQL
    # ---------------------------------------
    print("\n[3] Connecting to PostgreSQL...")
    conn = get_connection()

    # ---------------------------------------
    # STEP 4 - Load Dimension Tables
    # ---------------------------------------
    print("\n[4] Loading Dimensions...")

    load_dim_customer(conn, dim_customer)
    load_dim_product(conn, dim_product)
    load_dim_location(conn, dim_location)
    load_dim_shipping(conn, dim_shipping)
    load_dim_date(conn, dim_date)

    # ---------------------------------------
    # STEP 5 - Build Fact Table
    # ---------------------------------------
    print("\n[5] Building Fact Table...")

    fact = build_fact_table(conn, raw_df)

    print(f"\nFact Records : {len(fact)}")
    print(fact.head())

    # ---------------------------------------
    # STEP 6 - Load Fact Table
    # ---------------------------------------
    print("\n[6] Loading Fact Table...")

    load_fact_sales(conn, fact)

    conn.close()

    print("\n" + "=" * 60)
    print("ETL PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()