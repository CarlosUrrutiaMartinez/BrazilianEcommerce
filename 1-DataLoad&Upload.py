import pandas as pd
import os

base_path = r"C:\Users\amznncar\Documents\DataProjects\E-Commerce Project\Data"

df_customers = pd.read_csv(os.path.join(base_path, "olist_customers_dataset.csv"))
df_geolocation = pd.read_csv(os.path.join(base_path, "olist_geolocation_dataset.csv"))
df_order_items = pd.read_csv(os.path.join(base_path, "olist_order_items_dataset.csv"))
df_order_payments = pd.read_csv(os.path.join(base_path, "olist_order_payments_dataset.csv"))
df_order_reviews = pd.read_csv(os.path.join(base_path, "olist_order_reviews_dataset.csv"))
df_orders = pd.read_csv(os.path.join(base_path, "olist_orders_dataset.csv"))
df_products = pd.read_csv(os.path.join(base_path, "olist_products_dataset.csv"))
df_sellers = pd.read_csv(os.path.join(base_path, "olist_sellers_dataset.csv"))
df_category_translation = pd.read_csv(os.path.join(base_path, "product_category_name_translation.csv"))

print("Dataset Shapes:")
print(f"Customers: {df_customers.shape}")
print(f"Geolocation: {df_geolocation.shape}")
print(f"Order Items: {df_order_items.shape}")
print(f"Order Payments: {df_order_payments.shape}")
print(f"Order Reviews: {df_order_reviews.shape}")
print(f"Orders: {df_orders.shape}")
print(f"Products: {df_products.shape}")
print(f"Sellers: {df_sellers.shape}")
print(f"Category Translation: {df_category_translation.shape}")

print("Orders Info:")
print(df_orders.info(), "\n")

print("Order Items Info:")
print(df_order_items.info(), "\n")

print("Customers Info:")
print(df_customers.info(), "\n")

print("Missing values in Orders:")
print(df_orders.isnull().sum(), "\n")

print("Missing values in Order Items:")
print(df_order_items.isnull().sum(), "\n")

print("Missing values in Customers:")
print(df_customers.isnull().sum(), "\n")

missing_delivery_orders = df_orders[df_orders["order_delivered_customer_date"].isnull()]
print(missing_delivery_orders["order_status"].value_counts())

unique_statuses = df_orders["order_status"].unique()
print(f"Unique order statuses: {unique_statuses}")

df_orders["order_delivered_customer_date"].fillna("missing", implace=True)