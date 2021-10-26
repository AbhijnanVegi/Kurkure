import re
import random
import string

from utils.cursor import con, cur
from utils.utils import get_input 

def delete_product():
    try:
        details = {}
        details["ProductID"] = input(f"Product ID: ")
        print(details)

        query ="""
        DELETE from CONTAINS WHERE ProductID = %s
        """ % int(details["ProductID"])
        cur.execute(query)
        con.commit()

        query ="""
        DELETE from REVIEWSREL WHERE ProductID = %s
        """ % int(details["ProductID"])
        cur.execute(query)
        con.commit()

        query ="""
        DELETE from CATEGORY WHERE ProductID = %s
        """ % int(details["ProductID"])
        cur.execute(query)
        con.commit()

        query ="""
        DELETE from DELIVERY_AVAILABILITY WHERE ProductID = %s
        """ % int(details["ProductID"])
        cur.execute(query)
        con.commit()

        query ="""
        DELETE from PRODUCT WHERE ProductID = %s
        """ % int(details["ProductID"])
        cur.execute(query)
        con.commit()
        print("Product with product id: " + str(details["ProductID"]) + " deleted\n\n")

    except Exception as e:
        print("Operation failed")
        print(">>>>>>>", e)
        con.rollback()

def delete_address():
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

        i = int(input("Select the address to delete: "))

        query="""
        DELETE FROM ADDRESS WHERE UserEmailAddress = "%s" AND Line1 = "%s" AND Line2 = "%s"
        """% (details["Email Address"], addresses[i]["Line1"], addresses[i]["Line2"])

        # Domian error handling
        if (i >=  len(addresses)):
            raise("Invalid index for address")

        cur.execute(query)
        con.commit()
        print("Address deleted\n\n")

    except Exception as e:
        print("Operation failed")
        print(">>>>>>>", e)
        con.rollback()       

def delete_review():
    try:
        details = {}
        details["UserEmailAddress"] = input(f"EMAIL ADDRESS: ")
        details["ProductID"] = input(f"Product ID: ")
        details["OrderId"] = input(f"Order ID: ")

        query="""
        SELECT * from REVIEWSREL WHERE UserEmailAddress = "%s" AND ProductID = %s AND OrderID = %s
        """ % (details["UserEmailAddress"], int(details["ProductID"]), int(details["OrderId"]))
        cur.execute(query)
        review = cur.fetchone()
        if not review:
            raise("No review exists")
        
        query="""
        DELETE FROM REVIEW WHERE ReviewId = %s
        """ % int(review["ReviewId"])
        cur.execute(query)

        query ="""
        DELETE from REVIEWSREL WHERE UserEmailAddress = "%s" AND ProductID = %s AND OrderId = %s
        """ % (details["UserEmailAddress"], int(details["ProductID"]), int(details["OrderId"]))
        print("Review deleted\n\n")
        cur.execute(query)
        con.commit()

    except Exception as e:
        print("Operation failed")
        print(">>>>>>>", e)
        con.rollback()