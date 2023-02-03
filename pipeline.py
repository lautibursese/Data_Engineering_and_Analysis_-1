
import pandas as pd
from geopy.geocoders import Nominatim
from preprocessing import Preprocessing

print("Processing...")
'''

    *** ORDERS ***

'''
Orders = pd.read_csv("C:/Users/Predator/Desktop/Lauti/Programación/GitHub/2. Data Analytics/#2/datasets/olist_orders_dataset.csv")
orders = Preprocessing(Orders)

orders.replace_null_dates("order_purchase_timestamp", "order_approved_at")
orders.replace_null_dates("order_approved_at", "order_delivered_carrier_date")
orders.replace_null_dates("order_delivered_carrier_date", "order_delivered_customer_date")

orders.change_type_date("order_purchase_timestamp")
orders.change_type_date("order_approved_at")
orders.change_type_date("order_delivered_carrier_date")
orders.change_type_date("order_delivered_customer_date")
orders.change_type_date("order_estimated_delivery_date")

orders.swap_dates("order_approved_at", "order_delivered_carrier_date")
orders.swap_dates("order_delivered_carrier_date", "order_delivered_customer_date")

orders.clean_to_csv("orders.csv")

'''

    *** ORDER ITEMS ***

'''
Order_Items = pd.read_csv("C:/Users/Predator/Desktop/Lauti/Programación/GitHub/2. Data Analytics/#2/datasets/olist_order_items_dataset.csv")
order_items = Preprocessing(Order_Items)

order_items.clean_to_csv("order_items.csv")

'''

    *** SELLERS ***

'''

Sellers = pd.read_csv("C:/Users/Predator/Desktop/Lauti/Programación/GitHub/2. Data Analytics/#2/datasets/olist_sellers_dataset.csv")
sellers = Preprocessing(Sellers)

sellers.clean_to_csv("sellers.csv")


'''

    *** PRODUCTS ***

'''
Products = pd.read_csv("C:/Users/Predator/Desktop/Lauti/Programación/GitHub/2. Data Analytics/#2/datasets/olist_products_dataset.csv")
products = Preprocessing(Products)

products.fill_nulls()

products.clean_to_csv("products.csv")


'''

    *** CLOSED DEALS ***

'''
Closed_Deals = pd.read_csv("C:/Users/Predator/Desktop/Lauti/Programación/GitHub/2. Data Analytics/#2/datasets/olist_closed_deals_dataset.csv")
closed_deals = Preprocessing(Closed_Deals)
closed_deals.change_type_date("won_date")
closed_deals.replace_str("business_segment")
closed_deals.replace_str("lead_type")

closed_deals.clean_to_csv("closed_deals.csv")

'''

    *** CUSTOMERS ***

'''
Customers = pd.read_csv("C:/Users/Predator/Desktop/Lauti/Programación/GitHub/2. Data Analytics/#2/datasets/olist_customers_dataset.csv")
customers = Preprocessing(Customers)
customers.drop_column("customer_unique_id")
customers.clean_to_csv("customers.csv")

'''

    *** PAYMENTS ***

'''
Payments = pd.read_csv("C:/Users/Predator/Desktop/Lauti/Programación/GitHub/2. Data Analytics/#2/datasets/olist_order_payments_dataset.csv")
payments = Preprocessing(Payments)
payments.replace_str_regex("payment_type")
payments.clean_to_csv("payments.csv")


'''

    *** CATEGORY NAME ***

'''
Category_Name = pd.read_csv("C:/Users/Predator/Desktop/Lauti/Programación/GitHub/2. Data Analytics/#2/datasets/product_category_name_translation.csv")
category_name = Preprocessing(Category_Name)
category_name.replace_str_regex("product_category_name")
category_name.replace_str_regex("product_category_name_english")
category_name.clean_to_csv("category_name_translation.csv")

'''

    *** GEOLOCATION ***

'''

Geolocation = pd.read_csv("C:/Users/Predator/Desktop/Lauti/Programación/GitHub/2. Data Analytics/#2/datasets/olist_geolocation_dataset.csv")
geolocation = Preprocessing(Geolocation)

itabatã = Geolocation['geolocation_city'] == 'itabatan'
barra_do_quarai = Geolocation['geolocation_city'] == 'barrado quarai'
# Some city names correction for outliers
Geolocation.loc[itabatã, 'geolocation_city'] = 'itabatã'
Geolocation.loc[barra_do_quarai, 'geolocation_city'] = 'barra do quarai'

# Extreme coordinate points of Brazil
# Northest latitude point
LatitudeN = Geolocation['geolocation_lat'] > (5.269582)
# Southest latitude point
LatitudeS = Geolocation['geolocation_lat'] < (-33.750936)
# Eastest longitude point
LongitudeE = Geolocation['geolocation_lng'] > (-34.793015)
# Westest longitude point
LongitudeW = Geolocation['geolocation_lng'] < (-73.98306)

# For wrong north points
geolocator = Nominatim(user_agent="burseselautaro@gmail.com")


i = 0
while i < Geolocation[LatitudeN].shape[0]:
    position = Geolocation[LatitudeN].index[i]
    Geolocation.loc[position, 'geolocation_lat'] = geolocator.geocode(f"{Geolocation.loc[position, 'geolocation_city']}, Brasil", timeout=3).latitude
    Geolocation.loc[position, 'geolocation_lng'] = geolocator.geocode(f"{Geolocation.loc[position, 'geolocation_city']}, Brasil", timeout=3).longitude
    i += 1

# For wrong south points
i = 0
while i < Geolocation[LatitudeS].shape[0]:
    position = Geolocation[LatitudeS].index[i]
    Geolocation.loc[position, 'geolocation_lat'] = geolocator.geocode(f"{Geolocation.loc[position, 'geolocation_city']}, Brasil", timeout=3).latitude
    Geolocation.loc[position, 'geolocation_lng'] = geolocator.geocode(f"{Geolocation.loc[position, 'geolocation_city']}, Brasil", timeout=3).longitude
    i += 1

# For wrong east points
i = 0
while i < Geolocation[LongitudeE].shape[0]:
    position = Geolocation[LongitudeE].index[i]
    Geolocation.loc[position, 'geolocation_lat'] = geolocator.geocode(f"{Geolocation.loc[position, 'geolocation_city']}, Brasil", timeout=3).latitude
    Geolocation.loc[position, 'geolocation_lng'] = geolocator.geocode(f"{Geolocation.loc[position, 'geolocation_city']}, Brasil", timeout=3).longitude
    i += 1

# For wrong west points
i = 0
while i < Geolocation[LongitudeW].shape[0]:
    position = Geolocation[LongitudeW].index[i]
    Geolocation.loc[position, 'geolocation_lat'] = geolocator.geocode(f"{Geolocation.loc[position, 'geolocation_city']}, Brasil", timeout=3).latitude
    Geolocation.loc[position, 'geolocation_lng'] = geolocator.geocode(f"{Geolocation.loc[position, 'geolocation_city']}, Brasil", timeout=3).longitude
    i += 1

Specific = Geolocation['geolocation_lat'] < (-30.00) #495 rows
Specific2 = Geolocation['geolocation_lng'] < (-55.00) #495 rows
i = 0
while i < Geolocation[Specific&Specific2].shape[0]:
    position = Geolocation[Specific&Specific2].index[i]
    Geolocation.loc[position, 'geolocation_lat'] = geolocator.geocode(f"{Geolocation.loc[position, 'geolocation_city']}, Brasil", timeout=3).latitude
    Geolocation.loc[position, 'geolocation_lng'] = geolocator.geocode(f"{Geolocation.loc[position, 'geolocation_city']}, Brasil", timeout=3).longitude
    i += 1

geolocation.clean_to_csv("geolocation.csv")

'''

    *** MARKETING ***

'''

Marketing = pd.read_csv("C:/Users/Predator/Desktop/Lauti/Programación/GitHub/2. Data Analytics/#2/datasets/olist_marketing_qualified_leads_dataset.csv")
marketing = Preprocessing(Marketing)

marketing.criteria_unification('origin', 'unknown', 'other')
marketing.criteria_unification('origin', 'other_publicities', 'other')

marketing.change_type_date('first_contact_date')

marketing.clean_to_csv('marketing.csv')

'''

    *** REVIEWS ***

'''
Reviews = pd.read_csv("C:/Users/Predator/Desktop/Lauti/Programación/GitHub/2. Data Analytics/#2/datasets/olist_order_reviews_dataset.csv")
reviews = Preprocessing(Reviews)

reviews.change_type_date('review_creation_date')
reviews.change_type_date('review_answer_timestamp')

reviews.fill_some_values('review_comment_title', 'Sin Dato')
reviews.fill_some_values('review_comment_message', 'Sin Dato')

reviews.clean_to_csv('reviews.csv')


print("Datasets creados!!!")
