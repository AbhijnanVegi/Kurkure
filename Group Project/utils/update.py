import re
import random
import string

from utils.cursor import con, cur
from utils.utils import get_input 

def update_productdetails():

    #print("Hello There")
    try:
        

        details = {}
        details["ProductID"] = input(f"Product ID: ")
        details["Name"] = input(f"Name: ")
        details["TotalQuantity"] = input(f"Total quantity: ")
        details["Price"] = input(f"Price: ")


        contains_query = """SELECT * FROM PRODUCT WHERE ProductID=%s""" % (int(details["ProductID"]))
        cur.execute(contains_query)
        contains_details = cur.fetchone()

        if(details["Name"]==''):
            details["Name"] = contains_details["Name"]

        if(details["TotalQuantity"]==''):
            details["TotalQuantity"] = contains_details["TotalQuantity"]

        if(details["Price"]==''):
            details["Price"] = contains_details["Price"]



        # print(contains_details);
        
        query ="""
        UPDATE PRODUCT 
            SET Name = coalesce("%s",Name), TotalQuantity = coalesce("%s",TotalQuantity), Price = coalesce(%s,Price)
            WHERE ProductID = %s
        """ % (details["Name"], details["TotalQuantity"], details["Price"], details["ProductID"]) 
        #% ("NULL" if details["Name"]=='' else details["Name"], "NULL" if details["TotalQuantity"]=='' else details["TotalQuantity"], "NULL" if details["Price"]=='' else int(details["Price"]), "NULL" if details["TotalQuantity"]=='' else int(details["TotalQuantity"]),int(details["ProductID"]))
        cur.execute(query)
        con.commit()
        print("Product Details Updated\n\n")
        
    except Exception as e:
        #print(cur._last_executed)
        print("Operation failed")
        print(">>>>>>>", e)
        con.rollback()


def update_address():
    try:

        details = {}
        details["Email Address"] = input(f"Email Address: ")
        
        query ="""
        SELECT * from ADDRESS WHERE UserEmailAddress = "%s"
        """ % details["Email Address"]

        cur.execute(query)
        addresses = cur.fetchall()
        for i,address in enumerate(addresses):
            print(f"{i}. {address['Line1']}, {address['Line2']}")

        i = int(input("Select the address to update: "))


        details["Address Line 1"] = input(f"Address Line 1: ")
        details["Address Line 2"] = input(f"Address Line 2: ")
        details["City"] = input(f"City: ")
        details["State"] = input(f"State: ")
        details["Zipcode"] = input(f"Zipcode: ")

        
        
        if(details["Address Line 1"]==''):
            details["Address Line 1"] = addresses[i]["Line1"]
        
        if(details["Address Line 2"]==''):
            details["Address Line 2"] = addresses[i]["Line2"]
        
        if(details["City"]==''):
            details["City"] = addresses[i]["City"]
        
        if(details["State"]==''):
            details["State"] = addresses[i]["State"]
        
        if(details["Zipcode"]==''):
            details["Zipcode"] = addresses[i]["Zipcode"]
        
        
        query ="""
        UPDATE ADDRESS 
            SET Line1 = "%s" , Line2 = "%s", City = "%s", State = "%s", Zipcode = %s
            WHERE UserEmailAddress = "%s" AND Line1 = "%s" AND Line2 = "%s"
        """ % (details["Address Line 1"], details["Address Line 2"], details["City"], details["State"], int(details["Zipcode"]), details["Email Address"], addresses[i]["Line1"], addresses[i]["Line2"])
        cur.execute(query)
        con.commit()

        print("Address Details Updated\n\n")
        
    except Exception as e:
        print(cur._last_executed)
        print("Operation failed")
        print(">>>>>>>", e)
        con.rollback()


def update_review():
    try:
        details = get_input(request=[
                "User Email Address",
                "Product ID",
                "Order ID",
            ])

        contains_query = """SELECT * FROM REVIEWSREL WHERE UserEmailAddress="%s" AND ProductId = %s AND OrderId = %s  
        """ % (details["User Email Address"], int(details["Product ID"]), int(details["Order ID"]))
        cur.execute(contains_query)
        contains_details = cur.fetchone()

        review_id = contains_details["ReviewId"]

        print(review_id)
        review = get_input(request=[
            "Review",
            "Rating"
        ])
        query = """
        UPDATE REVIEW
            SET Review = "%s", Rating = %s
            WHERE ReviewId = %s
        """ % (review["Review"], int(review["Rating"]), review_id)
        cur.execute(query)
        con.commit()
        #print(query)
        

    except Exception as e:
        print(cur._last_executed)
        print("Operation failed")
        print(">>>>>>>", e)
        con.rollback()
    

def update_payment():
    try:
        details = get_input(request=[
            "User Email Address",
            "Name of payment method",
        ])


        new = get_input(request=[
            "New name of payment method",
            "Set as default [y/N]"
        ])

        query = """
        UPDATE PAYMENT_METHOD SET Name = "%s", IsDefault = %s WHERE UserEmailAddress = "%s" AND Name="%s" 
        """ % (new["New name of payment method"], 1 if new["Set as default [y/N]"]=="y" else 0, details["User Email Address"], details["Name of payment method"])
        cur.execute(query)
        con.commit()
        #print(query)
        

    except Exception as e:
        print(cur._last_executed)
        print("Operation failed")
        print(">>>>>>>", e)
        con.rollback()

   


    
   
