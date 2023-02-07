# Data dictionary

* Geolocations:
  * zip_code_prefix: unique postal code of 5 digits.
  * latitude: latitude coordinates location in format "double".
  * longitude: longitude coordinates location in format "double".
  * city: name of the city in string-format. 
  * state: name of the state in string-format.

* Marketing_qualified_leads:
  * mql_id: 32 characters unique ID of the marketing leader.
  * first_contact_date: Date of first contact in date format.
  * landing_page_id: id of the landing page in string format.
  * origin: Origin in 25-character string format, can be null.

* Product_categories:
  * product_category_name: Name of the product category in string format.
  * name_in_english: Name of the product category in English in string format.

* Products:
  * product_id: 32-character unique product id.
  * product_category_name: Name of the product category in string format.
  * name_length: Length of the name in integer format.
  * description_length: Length of the description in integer format.
  * photos_quantity: Quantity of photos in full format.
  * weight_in_gram: Weight in grams in integer format.
  * length_in_cm: Length in centimeters in integer format.
  * height_in_cm: Height in centimeters in integer format.
  * width_in_cm: Width in centimeters in integer format.

* Sellers:
  * seller_id: Unique 32-character seller id.
  * zip_code_prefix: 5-digit zip code.

* seller_products:
  * seller_product_id: Unique 32-character seller's product id.
  * seller_id: id of the seller associated with the product.
  * product_id: product id.

* customers:
  * customer_id: unique 32-character customer id.

* closed_deals:
  * mql_id: 32-character id of the qualified customer for the market.
  * seller_id: id of the seller associated with the closed offer.
  * sdr_id: id of the sales representative responsible for the customer qualified for the market.
  * sr_id: id of the sales representative responsible for closing the offer.
  * won_date: date the deal was closed.
  * business_segment: business segment associated with the closed offer.
  * lead_type: type of customer qualified for the market.
  * lead_behaviour_profile: behavior profile of the qualified customer for the market.
  * has_company – Indicates whether the market-qualified customer has a company.
  * has_gtin: indicates if the product associated with the closed offer has a GTIN code.
  * average_stock: average stock of the product.
  * business_type: type of business of the client.
  * declared_product_catalog_size: size of the product catalog declared by the client.
  * declared_monthly_revenue: monthly income declared by the client.

* orders:
  * order_id: unique order id of 32 characters.
  * customer_id: id of the customer associated with the order.
  * order_status: order status.
  * purchase_date: purchase date of the order.
  * approved_date : date the order was approved.
  * delivered_carrier_date: date the product was delivered by the carrier.
  * delivered_customer_date: date the product was delivered to the customer.
  * estimated_delivery_date: estimated delivery date of the product.
  * zip_code_prefix: Postal code.

* order_items:
  * order_id: id of the order to which the 32-character article belongs.
  * seller_product_id: id of the product and seller.
  * price: price of the item at the time of purchase.
  * freight_value: freight value for shipping the item.

* order_payments:
  * order_id: id of the order to which the payment belongs.
  * payment_sequential: payment sequence within the order.
  * type: type of payment made (credit card, transfer, etc.).
  * installments: number of installments for payment.
  * value: value of the payment.

* reviews:
  * review_id: unique 32-character review id.
  * order_id: id of the order to which the review belongs.
  * score: score of the review (from 1 to 5).
  * comment_title: title of the review.
  * comment_message: body of the review.
  * creation_date: date the review was created.
  * answer_date: review response date.
  * order_id: id of the order to which the payment belongs.
