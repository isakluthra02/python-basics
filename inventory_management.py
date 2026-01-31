import mysql.connector
import pandas as pd
import numpy as np

#connection establishment
conn=mysql.connector.connect(
    host='localhost',
    user='Username',
    password='Password'
)
#loading data
query="SELECT * FROM inventory"
data = pd.read_sql(query, conn)
print("Current products: ")
print(data)
data["stock_price"]=data["price"]*data["stock_count"]

#minimum stock qty
min_val=5

#checking the if 
stock_list=data["stock_count"].to_numpy()
data["status"] = np.where(
     stock_list<= min_val,
    "REORDER",
    "All checks OK"
)

#total value of the products in inventory
total_inv_val=np.sum(data["stock_price"])

#priting inentory information
print("Inventory Information :")
print(data[["product","stock_count","status"]])
print(f"Total inventory value {total_inv_val}")
cursor = conn.cursor()


update_query = """
UPDATE inventory
SET stock_value=%s, status=%s
WHERE id=%s
"""
# For each product, update the database with the current stock and status
for search,row in data.iterrows():
    cursor.execute(update_query,(
        row["stock_price"],
        row["status"],
        row["id"]
    ))

#saving changes and closing connection
conn.commit()
conn.close()