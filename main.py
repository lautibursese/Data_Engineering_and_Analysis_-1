from fastapi import FastAPI
import pandas as pd

app = FastAPI(title="API olist", version="2.0")

sellers = pd.read_csv("./clean_datasets/sellers.csv")
reviews = pd.read_csv("./clean_datasets/reviews.csv")
products = pd.read_csv("./clean_datasets/products.csv")
payments = pd.read_csv("./clean_datasets/payments.csv")
orders = pd.read_csv("./clean_datasets/orders.csv")
order_items = pd.read_csv("./clean_datasets/order_items.csv")
marketing = pd.read_csv("./clean_datasets/marketing.csv")
geolocation = pd.read_csv("./clean_datasets/geolocation.csv")
customers = pd.read_csv("./clean_datasets/customers.csv")
closed_deals = pd.read_csv("./clean_datasets/closed_deals.csv")
category_name_translation = pd.read_csv("./clean_datasets/category_name_translation.csv")

@app.get("/"):
async def welcome():
    return "Bienvenido a nuestra API"

@app.get("/sellers")
async def get_sellers():
    return sellers