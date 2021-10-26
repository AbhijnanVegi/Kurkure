from tabulate import tabulate

from utils.cursor import con, cur
from utils.utils import get_input 

def search_product():
    ''' User can search for products based on name.'''
    try:
        word = input(f"Enter the word : ")

        query ="""
        SELECT * FROM PRODUCT WHERE Name = "%s"
        """ % word

        cur.execute(query)
        products = cur.fetchall()
        print(tabulate(products, headers = {
            "ProductID" : "Product ID",
            "Name" : "Name",
            "TotalQuantity" : "Total Quantity",
            "Price" : "Price",
            "DeliveryLocations" : "Delivery Locations",
            "Categories" : "Categories"
        }))
    
    except Exception as e:
        print(cur._last_executed)
        print("Operation failed")
        print(">>>>>>>", e)
        con.rollback()

