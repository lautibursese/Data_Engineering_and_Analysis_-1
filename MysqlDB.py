import mysql.connector


class MysqlDB:

    def __init__(self) -> None:
        self.mydb = mysql.connector.connect(
            # host='35.232.179.155',
            host='localhost',
            user='root',
            password='root',
            database='olist_db'
        )

    def insert_product_categories(self, values):
        cursor = self.mydb.cursor()

        insert_product_categories_query = """INSERT INTO product_categories (product_category_name, name_in_english) 
                                             VALUES (%s, %s);"""

        cursor.executemany(insert_product_categories_query, values)
        self.mydb.commit()
        print(cursor.rowcount, "new product_categories inserted")

    def insert_many_geolocations(self, values):
        cursor = self.mydb.cursor()

        insert_geolocations_query = """INSERT INTO geolocations (zip_code_prefix, latitude, longitude, city, state) 
                                       VALUES (%s, %s, %s, %s, %s)"""

        cursor.executemany(insert_geolocations_query, values)
        self.mydb.commit()
        print(cursor.rowcount, "new geolocation inserted")

    def insert_many_marketing_qualified_leads(self, values):
        cursor = self.mydb.cursor()

        insert_marketing_query = """INSERT INTO marketing_qualified_leads (mql_id, first_contact_date, landing_page_id, 
                                                                           origin) 
                                    VALUES (%s, %s, %s, %s)"""

        cursor.executemany(insert_marketing_query, values)
        self.mydb.commit()
        print(cursor.rowcount, "new mql inserted")

    def get_product_category_name(self, category_name):
        cursor = self.mydb.cursor()

        get_category_name_query = """SELECT product_category_name FROM product_categories 
                                     WHERE product_category_name = %s;"""

        cursor.execute(get_category_name_query, (category_name,))

        result = cursor.fetchone()
        return result

    def insert_many_products(self, value):
        cursor = self.mydb.cursor()

        insert_products_query = """INSERT INTO products (product_id, product_category_name, name_length, 
                                    description_length, photos_quantity, weight_in_gram, length_in_cm, height_in_cm, 
                                    width_in_cm)
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        cursor.executemany(insert_products_query, value)
        self.mydb.commit()
        print(cursor.rowcount, "new product inserted")

    def insert_customer(self, value):
        cursor = self.mydb.cursor()

        insert_customer_query = """INSERT INTO customers (customer_id) VALUES (%s);"""

        cursor.execute(insert_customer_query, value)
        self.mydb.commit()
        print(cursor.rowcount, "new customer inserted")

    def get_seller_id_by_id(self, seller_id):
        cursor = self.mydb.cursor()

        get_seller_id_query = """SELECT seller_id FROM sellers WHERE seller_id = %s"""

        cursor.execute(get_seller_id_query, (seller_id,))

        result = cursor.fetchone()
        return result

    def get_customer_id_by_id(self, customer_id):
        cursor = self.mydb.cursor()

        get_customer_id_query = """SELECT customer_id FROM customers WHERE customer_id = %s"""

        cursor.execute(get_customer_id_query, (customer_id,))

        result = cursor.fetchone()
        return result

    def get_mql_id_by_id(self, mql_id):
        cursor = self.mydb.cursor()

        get_mql_id_query = """SELECT mql_id FROM marketing_qualified_leads WHERE mql_id = %s"""

        cursor.execute(get_mql_id_query, (mql_id,))

        result = cursor.fetchone()
        return result

    def insert_many_sellers(self, values):
        cursor = self.mydb.cursor()

        insert_sellers_query = """INSERT INTO sellers (seller_id, zip_code_prefix) VALUES (%s, %s);"""

        cursor.executemany(insert_sellers_query, values)
        self.mydb.commit()
        print(cursor.rowcount, "new seller inserted")

    def insert_many_customers(self, values):
        cursor = self.mydb.cursor()

        insert_customers_query = """INSERT INTO customers (customer_id) VALUES (%s);"""

        cursor.executemany(insert_customers_query, values)
        self.mydb.commit()
        print(cursor.rowcount, "new customer inserted")

    def get_zip_code_prefix(self, zip_code):
        cursor = self.mydb.cursor()

        get_zip_code_query = """SELECT zip_code_prefix FROM geolocations WHERE zip_code_prefix = %s"""

        cursor.execute(get_zip_code_query, (zip_code,))

        result = cursor.fetchone()
        return result

    def get_order_id_by_id(self, order_id):
        cursor = self.mydb.cursor()

        get_order_id_query = """SELECT order_id FROM orders WHERE order_id = %s"""

        cursor.execute(get_order_id_query, (order_id,))

        result = cursor.fetchone()
        return result

    def insert_many_closed_deals(self, value):
        cursor = self.mydb.cursor()

        insert_deals_query = """INSERT INTO closed_deals (mql_id, seller_id, sdr_id, sr_id, won_date, business_segment, 
                                lead_type, lead_behaviour_profile, has_company, has_gtin, average_stock, business_type, 
                                declared_product_catalog_size, declared_monthly_revenue) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        cursor.executemany(insert_deals_query, value)
        self.mydb.commit()
        print(cursor.rowcount, "new closed deal inserted")

    def insert_many_orders(self, values):
        cursor = self.mydb.cursor()

        insert_orders_query = """insert into orders (order_id, customer_id, order_status, purchase_date, approved_date, 
                                 delivered_carrier_date, delivered_customer_date, estimated_delivery_date, zip_code_prefix) 
                                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        cursor.executemany(insert_orders_query, values)
        self.mydb.commit()
        print(cursor.rowcount, "new order inserted")

    def insert_many_order_payments(self, values):
        cursor = self.mydb.cursor()

        insert_order_payments_query = """insert into order_payments (order_id, payment_sequential, type, 
                                         installments, payment_value) 
                                         VALUES (%s, %s, %s, %s, %s)"""

        cursor.executemany(insert_order_payments_query, values)
        self.mydb.commit()
        print(cursor.rowcount, "new order_payment inserted")

    def insert_many_reviews(self, values):
        cursor = self.mydb.cursor()

        insert_reviews_query = """INSERT INTO reviews (review_id, order_id, score, comment_title, comment_message, creation_date, 
                                  answer_date)  
                                  VALUES (%s, %s, %s, %s, %s, %s, %s)"""

        cursor.executemany(insert_reviews_query, values)
        self.mydb.commit()
        print(cursor.rowcount, "new review inserted")

    def get_seller_product_id_by_seller_and_product_id(self, seller_id, product_id):
        cursor = self.mydb.cursor()

        get_seller_product_id_query = """SELECT seller_product_id FROM seller_products WHERE seller_id = %s AND product_id = %s"""

        cursor.execute(get_seller_product_id_query, (seller_id, product_id))

        result = cursor.fetchone()
        return result

    def insert_seller_product(self, value):
        cursor = self.mydb.cursor()

        insert_seller_product_query = """INSERT INTO seller_products (seller_id, product_id) VALUES (%s, %s);"""

        cursor.execute(insert_seller_product_query, value)
        self.mydb.commit()
        print(cursor.rowcount, "new seller product inserted")

    def insert_order_item(self, value):
        cursor = self.mydb.cursor()

        insert_order_item_query = """insert into order_items (order_id, seller_product_id, shipping_limit_date, 
        price, freight_value, quantity)  VALUES (%s, %s, %s, %s, %s, %s);"""

        cursor.execute(insert_order_item_query, value)
        self.mydb.commit()
        print(cursor.rowcount, "new order_item inserted")

    def get_order_item_id_by_id(self, order_id, seller_product_id):
        cursor = self.mydb.cursor()

        get_order_item_id_query = """SELECT order_id FROM order_items WHERE order_id = %s AND seller_product_id = %s"""

        cursor.execute(get_order_item_id_query, (order_id, seller_product_id))

        result = cursor.fetchone()
        return result

    def update_quantity_from_order_item_by_id(self, order_id, seller_product_id):
        cursor = self.mydb.cursor()

        get_order_item_id_query = """UPDATE order_items set quantity = quantity + 1 
                                     WHERE order_id = %s AND seller_product_id= %s;"""

        cursor.execute(get_order_item_id_query, (order_id, seller_product_id))

        self.mydb.commit()
        print(cursor.rowcount, "record(s) affected")


