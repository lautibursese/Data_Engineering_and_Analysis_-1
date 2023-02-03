from MysqlDB import MysqlDB
import pandas as pd
import numpy as np

if __name__ == "__main__":
    db = MysqlDB()

    path_cleaned_datasets = "./cleaned_datasets"

    # insertamos los datos limpios de product_categories
    product_categories = pd.read_csv(f"{path_cleaned_datasets}/category_name_translation.csv")
    db.insert_product_categories(list(product_categories.itertuples(index=False, name=None)))

    # insertamos los dato geolocations
    geolocations = pd.read_csv(f"{path_cleaned_datasets}/geolocation.csv")
    geolocations.drop_duplicates(subset="geolocation_zip_code_prefix", inplace=True)
    db.insert_many_geolocations(list(geolocations.itertuples(index=False, name=None)))

    # insertamos los datos marketing qualify lead
    mql = pd.read_csv(f"{path_cleaned_datasets}/marketing.csv")
    mql.replace(np.nan, None, inplace=True)
    db.insert_many_marketing_qualified_leads(list(mql.itertuples(index=False, name=None)))


    # insertamos los products

    products = pd.read_csv(f"{path_cleaned_datasets}/products.csv")
    products.replace(np.nan, None, inplace=True)

    for product in list(products.itertuples(index=False, name=None)):
        _, product_category_name, _, _, _, _, _, _, _ = product

        # buscamos si existe categoria del producto
        db_product_category = db.get_product_category_name(product_category_name)

        if db_product_category is None:
            db.insert_product_categories([(product_category_name, None)])

    db.insert_many_products(list(products.itertuples(index=False, name=None)))


    # insertamos los customers
    customers = pd.read_csv(f"{path_cleaned_datasets}/customers.csv")
    customers.replace(np.nan, None, inplace=True)
    for customer in list(customers.itertuples(index=False, name=None)):
        customer_id, customer_unique_id, zip_code_prefix, city, state = customer

        # buscamos si el zip_code existe:
        if zip_code_prefix is not None:
            db_zip_code = db.get_zip_code_prefix(zip_code_prefix)

            # si no existe ingresamos una nueva geolocation
            if db_zip_code is None:
                # ingresamos nueva geolocations
                db.insert_many_geolocations([(zip_code_prefix, None, None, city, state)])

    customers.drop_duplicates(subset="customer_unique_id", inplace=True)
    # creamos el nuevo customer
    db.insert_many_customers(list(customers[["customer_unique_id"]].itertuples(index=False, name=None)))

    # insertamos los sellers
    sellers = pd.read_csv(f"{path_cleaned_datasets}/sellers.csv")
    sellers.replace(np.nan, None, inplace=True)

    for seller in list(sellers.itertuples(index=False, name=None)):
        seller_id, zip_code_prefix, city, state = seller

        # buscamos si el zip_code existe:
        if zip_code_prefix is not None:
            db_zip_code = db.get_zip_code_prefix(zip_code_prefix)

            # si no existe ingresamos una nueva geolocation
            if db_zip_code is None:
                # ingresamos nueva geolocations
                db.insert_many_geolocations([(zip_code_prefix, None, None, city, state)])

    db.insert_many_sellers(list(sellers[["seller_id", "seller_zip_code_prefix"]].itertuples(index=False, name=None)))

    # insertamos los closed_deals
    closed_deals = pd.read_csv(f"{path_cleaned_datasets}/closed_deals.csv")
    closed_deals.replace(np.nan, None, inplace=True)
    for deal in list(closed_deals.itertuples(index=False, name=None)):
        mql_id, seller_id, sdr_id, sr_id, won_date, business_segment, lead_type, lead_behaviour_profile, has_company, \
            has_gtin, average_stock, business_type, catalog_size, monthly_revenue = deal

        # buscamos el seller en la bd
        db_seller_id = db.get_seller_id_by_id(seller_id)

        if db_seller_id is None:
            db.insert_many_sellers([(seller_id, None)])

        # buscamos el mql en la bd
        db_mql_id = db.get_mql_id_by_id(mql_id)

        if db_mql_id is None:
            db.insert_many_marketing_qualified_leads([(mql_id, None, None, None)])
    db.insert_many_closed_deals(list(closed_deals.itertuples(index=False, name=None)))

    # insert orders
    orders = pd.read_csv(f"{path_cleaned_datasets}/orders.csv")
    orders.replace(np.nan, None, inplace=True)

    for order in list(orders.itertuples(index=False, name=None)):
        order_id, customer_id, _, _, _, _, _, _, _ = order
        # buscamos si existe el cliente
        db_customer_id = db.get_customer_id_by_id(customer_id)

        if db_customer_id is None:
            db.insert_customer((customer_id, customer_id))

    db.insert_many_orders(list(orders.itertuples(index=False, name=None)))

    # insert order_payments

    payments = pd.read_csv(f"{path_cleaned_datasets}/payments.csv")
    payments.replace(np.nan, None, inplace=True)

    for payment in list(payments.itertuples(index=False, name=None)):
        order_id, payment_sequential, payment_type, payment_installments, payment_value = payment

        # buscamos order_id en la bd si existe
        db_order_id = db.get_order_id_by_id(order_id)

        if db_order_id is None:
            db.insert_many_orders([(order_id, None, None, None, None, None, None, None)])

    db.insert_many_order_payments(list(payments.itertuples(index=False, name=None)))


    # insert reviews

    reviews = pd.read_csv(f"{path_cleaned_datasets}/reviews.csv")
    reviews.replace(np.nan, None, inplace=True)
    reviews.drop_duplicates(subset="review_id", inplace=True)

    db.insert_many_reviews(list(reviews.itertuples(index=False, name=None)))

    # insert order_items

    order_items = pd.read_csv("./cleaned_datasets/order_items.csv")
    order_items.replace(np.nan, None, inplace=True)

    for item in list(order_items.itertuples(index=False, name=None)):
        order_id, order_item_id, product_id, seller_id, shipping_limit_date, price, freight_value = item

        # buscamos seller_product_id si existe
        db_seller_product_id = db.get_seller_product_id_by_seller_and_product_id(seller_id, product_id)

        if db_seller_product_id is None:
            db.insert_seller_product((seller_id, product_id))

            # buscamos nuevamente seller_product que acabamos de ingresar
            db_seller_product_id = db.get_seller_product_id_by_seller_and_product_id(seller_id, product_id)


        # buscamos si ya existe el item
        db_order_item_id = db.get_order_item_id_by_id(order_id, db_seller_product_id[0])

        if db_order_item_id is None:
            # insertamos order item
            db.insert_order_item((order_id, db_seller_product_id[0], shipping_limit_date, price, freight_value, 1))

        else:
            db.update_quantity_from_order_item_by_id(order_id, db_seller_product_id[0])





