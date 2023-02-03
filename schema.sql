create database IF NOT EXISTS olist_db;
use olist_db;



CREATE TABLE geolocations(
    zip_code_prefix VARCHAR(5) PRIMARY KEY NOT NULL,
    latitude DOUBLE(25,20) NULL,
    longitude DOUBLE(25,20) NULL,
    city VARCHAR(100) NULL,
    state VARCHAR(100) NULL
);

CREATE TABLE marketing_qualified_leads(
    mql_id VARCHAR(32) PRIMARY KEY NOT NULL,
    first_contact_date DATE NULL,
    landing_page_id VARCHAR(32) NOT NULL,
    origin VARCHAR(25) NULL
);

CREATE TABLE product_categories(
    product_category_name VARCHAR(100) PRIMARY KEY,
    name_in_english VARCHAR(100) NULL
);

CREATE TABLE products(
    product_id VARCHAR(32) PRIMARY KEY NOT NULL,
    product_category_name VARCHAR(100) NULL,
    name_length INTEGER NULL,
    description_length INTEGER NULL,
    photos_quantity INTEGER NULL,
    weight_in_gram INTEGER NULL,
    length_in_cm INTEGER NULL,
    height_in_cm INTEGER NULL,
    width_in_cm INTEGER NULL,

    FOREIGN KEY (product_category_name) REFERENCES product_categories(product_category_name)
);

CREATE TABLE sellers(
    seller_id VARCHAR(32) PRIMARY KEY NOT NULL,
    zip_code_prefix VARCHAR(5) NULL,

    FOREIGN KEY (zip_code_prefix) REFERENCES geolocations(zip_code_prefix)
);

CREATE TABLE seller_products(
    seller_product_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    seller_id VARCHAR(32) NOT NULL,
    product_id VARCHAR(32) NOT NULL,

    FOREIGN KEY (seller_id) REFERENCES sellers(seller_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE customers(
    customer_id VARCHAR(32) PRIMARY KEY NOT NULL
);

CREATE TABLE closed_deals(
    mql_id VARCHAR(32) NOT NULL,
    seller_id VARCHAR(32) NOT NULL,
    sdr_id VARCHAR(32) NULL,
    sr_id VARCHAR(32) NULL,
    won_date DATETIME NULL,
    business_segment VARCHAR(50) NULL,
    lead_type VARCHAR(25) NULL,
    lead_behaviour_profile VARCHAR(50) NULL,
    has_company BOOLEAN NULL,
    has_gtin BOOLEAN NULL,
    average_stock VARCHAR(25),
    business_type VARCHAR(25),
    declared_product_catalog_size FLOAT NULL,
    declared_monthly_revenue FLOAT NULL,

    PRIMARY KEY (mql_id, seller_id),
    FOREIGN KEY (mql_id) REFERENCES marketing_qualified_leads(mql_id),
    FOREIGN KEY (seller_id) REFERENCES sellers(seller_id)
);

CREATE TABLE orders(
    order_id VARCHAR(32) PRIMARY KEY NOT NULL,
    customer_id VARCHAR(32) NOT NULL,
    order_status VARCHAR(25) NULL,
    purchase_date DATETIME NULL,
    approved_date DATETIME NULL,
    delivered_carrier_date DATETIME NULL,
    delivered_customer_date DATETIME NULL,
    estimated_delivery_date DATETIME NULL,

    zip_code_prefix VARCHAR(5) NULL,

    FOREIGN KEY (zip_code_prefix) REFERENCES geolocations(zip_code_prefix),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items(
    order_id VARCHAR(32) NOT NULL,
    seller_product_id INTEGER NOT NULL,
    shipping_limit_date DATETIME NOT NULL,
    price FLOAT NOT NULL,
    freight_value FLOAT NOT NULL,
    quantity INTEGER NOT NULL,

    PRIMARY KEY (order_id,seller_product_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (seller_product_id) REFERENCES seller_products(seller_product_id)
);

CREATE TABLE order_payments(
    order_payment_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    order_id VARCHAR(32) NULL,
    payment_sequential INTEGER NULL,
    type VARCHAR(25) NULL,
    installments INTEGER NULL,
    payment_value FLOAT NULL,

    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

CREATE TABLE reviews(
    review_id VARCHAR(32) PRIMARY KEY NOT NULL,
    score INTEGER NULL,
    comment_title VARCHAR(225) NULL,
    comment_message TEXT NULL,
    creation_date DATETIME NOT NULL,
    answer_date DATETIME NULL,
    order_id VARCHAR(32) NOT NULL,

    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);