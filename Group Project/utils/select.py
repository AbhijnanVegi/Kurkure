from tabulate import tabulate

from utils.cursor import con, cur
from utils.utils import get_input 

def select_user():
    try:
        query = "SELECT * FROM USER"
        cur.execute(query)
        users = cur.fetchall()
        print(tabulate(users, headers = {
            "EmailAddress" : "Email Address",
            "FirstName" : "First Name",
            "MiddleName" : "Middle Name",
            "LastName" : "Last Name",
            "MobileNumber" : "Mobile Number",
            "SubscriptionStatus" : "Subscription Status"
        })) 
    except Exception as e:
        print("Operation failed")
        print(">>>>>>>", e)

def select_product():
    try:
        query = "SELECT * FROM PRODUCT"
        cur.execute(query)
        products = cur.fetchall()
        
        for product in products:
            delivery_query = "SELECT Location FROM DELIVERY_AVAILABILITY WHERE ProductId=%s"%(product["ProductId"])
            cur.execute(delivery_query)
            delivery_locations = cur.fetchall()
            product["DeliveryLocations"] = ",".join(loc["Location"] for loc in delivery_locations)

            category_query = "SELECT Category FROM CATEGORY WHERE ProductId=%s"%(product["ProductId"])
            cur.execute(category_query)
            categories = cur.fetchall()
            product["Categories"] = ",".join(cat["Category"] for cat in categories)
        
        print(tabulate(products, headers = {
            "ProductID" : "Product ID",
            "Name" : "Name",
            "TotalQuantity" : "Total Quantity",
            "Price" : "Price",
            "DeliveryLocations" : "Delivery Locations",
            "Categories" : "Categories"
        }))
    except Exception as e:
        print("Operation failed")
        print(">>>>>>>", e)

