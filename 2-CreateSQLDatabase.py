import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text

db_user = "root"
db_password = "Password"
db_host = "localhost"
db_name = "ecommerce"

engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}")

with engine.connect() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {db_name}"))

engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")

df_customers = pd.read_csv("C:/Users/amznncar/Documents/DataProjects/E-Commerce Project/Data/olist_customers_dataset.csv")
df_orders = pd.read_csv("C:/Users/amznncar/Documents/DataProjects/E-Commerce Project/Data/olist_orders_dataset.csv")
df_order_items = pd.read_csv("C:/Users/amznncar/Documents/DataProjects/E-Commerce Project/Data/olist_order_items_dataset.csv")

df_customers.to_sql("customers", con=engine, if_exists="replace", index=False)
df_orders.to_sql("orders", con=engine, if_exists="replace", index=False)
df_order_items.to_sql("order_items", con=engine, if_exists="replace", index=False)

print("Data successfully imported into MySQL!")