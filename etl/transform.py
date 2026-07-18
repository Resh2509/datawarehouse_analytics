import pandas as pd

def transform_data(df):
    """
    Transform the raw Superstore dataset into dimension tables.
    PostgreSQL will generate all surrogate keys.
    """

    # ----------------------------
    # Convert Date
    # ----------------------------
    df["Order.Date"] = pd.to_datetime(df["Order.Date"])

    # =====================================================
    # CUSTOMER DIMENSION
    # =====================================================
    dim_customer = (
        df[["Customer.ID", "Customer.Name", "Segment"]]
        .drop_duplicates(subset=["Customer.ID"])
        .reset_index(drop=True)
    )

    # =====================================================
    # PRODUCT DIMENSION
    # =====================================================
    dim_product = (
        df[["Product.ID", "Product.Name", "Category", "Sub.Category"]]
        .drop_duplicates(subset=["Product.ID"])
        .reset_index(drop=True)
    )

    # =====================================================
    # LOCATION DIMENSION
    # =====================================================
    dim_location = (
        df[["Country", "State", "City", "Region"]]
        .drop_duplicates()
        .reset_index(drop=True)
    )

    # =====================================================
    # SHIPPING DIMENSION
    # =====================================================
    dim_shipping = (
        df[["Ship.Mode"]]
        .drop_duplicates()
        .reset_index(drop=True)
    )

    # =====================================================
    # DATE DIMENSION
    # =====================================================
    dim_date = (
        df[["Order.Date"]]
        .drop_duplicates()
        .sort_values("Order.Date")
        .reset_index(drop=True)
    )

    dim_date["Year"] = dim_date["Order.Date"].dt.year
    dim_date["Quarter"] = dim_date["Order.Date"].dt.quarter
    dim_date["Month"] = dim_date["Order.Date"].dt.month
    dim_date["Month_Name"] = dim_date["Order.Date"].dt.month_name()
    dim_date["Day"] = dim_date["Order.Date"].dt.day
    dim_date["Weekday"] = dim_date["Order.Date"].dt.day_name()

    print("\n==============================")
    print("Transformation Completed")
    print("==============================")

    print(f"Customers : {len(dim_customer)}")
    print(f"Products  : {len(dim_product)}")
    print(f"Locations : {len(dim_location)}")
    print(f"Shipping  : {len(dim_shipping)}")
    print(f"Dates     : {len(dim_date)}")

    return (
        dim_customer,
        dim_product,
        dim_location,
        dim_shipping,
        dim_date,
        df          # return original dataframe for fact table creation
    )