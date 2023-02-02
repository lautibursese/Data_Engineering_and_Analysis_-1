# Data dictionary

* Geolocations:
  * zip_code_prefix: unique postal code of 5 digits.
  * latitude: latitude coordinates location in format "double".
  * longitude: longitude coordinates location in format "double".
  * city: name of the city in string-format. 
  * state: name of the state in string-format.

* Marketing_qualified_leads:
  * mql_id: id único del lider de marqueting de 32 caracteres.
  * first_contact_date: Fecha de primer contacto en formato fecha.
  * landing_page_id: id de la página de aterrizaje en formato string.
  * origin: Origen en formato string de 25 caracteres, puede ser nulo.

* Product_categories:
  * product_category_name: Nombre de la categoría de producto en formato string.
  * name_in_english: Nombre de la categoría de producto en inglés en formato string.

* Tabla products:
  * product_id: id único del producto de 32 caracteres.
  * product_category_name: Nombre de la categoría de producto en formato string.
  * name_length: Longitud del nombre en formato entero.
  * description_length: Longitud de la descripción en formato entero.
  * photos_quantity: Cantidad de fotos en formato entero.
  * weight_in_gram: Peso en gramos en formato entero.
  * length_in_cm: Longitud en centímetros en formato entero.
  * height_in_cm: Altura en centímetros en formato entero.
  * width_in_cm: Ancho en centímetros en formato entero.

* Tabla sellers:
  * seller_id: id  único del vendedor de 32 caracteres.
  * zip_code_prefix: Código postal de 5 dígitos.

* seller_products:
  * seller_product_id: id único del producto del vendedor de 32 caracteres.
  * seller_id: id del vendedor asociado al producto.
  * product_id: id del producto.

* customers:
  * customer_id: id único del cliente de 32 caracteres.

* closed_deals:
  * mql_id: id del cliente calificado para el mercado de 32 caracteres.
  * seller_id: id del vendedor asociado a la oferta cerrada.
  * sdr_id: id del representante de ventas responsable del cliente calificado para el mercado.
  * sr_id: id del representante de ventas responsable del cierre de la oferta.
  * won_date: fecha en la que se cerró la oferta.
  * business_segment: segmento de negocio asociado a la oferta cerrada.
  * lead_type: tipo de cliente calificado para el mercado.
  * lead_behaviour_profile: perfil de comportamiento del cliente calificado para el mercado.
  * has_company: indica si el cliente calificado para el mercado tiene una empresa.
  * has_gtin: indica si el producto asociado a la oferta cerrada tiene un código GTIN.
  * average_stock: stock promedio del producto.
  * business_type: tipo de negocio del cliente.
  * declared_product_catalog_size: tamaño del catálogo de productos declarado por el cliente.
  * declared_monthly_revenue: ingresos mensuales declarados por el cliente.

* orders:
  * order_id: id único del pedido de 32 caracteres.
  * customer_id: id del cliente asociado al pedido.
  * order_status: estado del pedido.
  * purchase_date: fecha de compra del pedido.
  * approved_date : fecha en la que el pedido fue aprobado.
  * delivered_carrier_date: fecha en la que el producto fue entregado por el transportista.
  * delivered_customer_date: fecha en la que el producto fue entregado al cliente.
  * estimated_delivery_date: fecha estimada de entrega del producto.
  * zip_code_prefix: Código postal.

* order_items:

  * order_id: id del pedido al que pertenece el artículo de 32 caracteres.
  * seller_product_id: id del producto y vendedor.
  * price: precio del artículo en el momento de la compra.
  * freight_value: valor del flete para el envío del artículo.

* order_payments:
  * order_id: id del pedido al que pertenece el pago.
  * payment_sequential: secuencia del pago dentro del pedido.
  * type: tipo de pago realizado (tarjeta de crédito, transferencia, etc.).
  * installments: número de cuotas para el pago.
  * value: valor del pago.

* reviews:
  * review_id: id único de la reseña de 32 caracteres.
  * order_id: id del pedido al que pertenece la reseña.
  * score: puntuación de la reseña (de 1 a 5).
  * comment_title: título de la reseña.
  * comment_message: cuerpo de la reseña.
  * creation_date: fecha de creación de la reseña.
  * answer_date: fecha de respuesta de la reseña.
  * order_id: id del pedido al que pertenece el pago.
