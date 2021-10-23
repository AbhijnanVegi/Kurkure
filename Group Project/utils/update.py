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

        #print(details)
        
        query ="""
        UPDATE PRODUCT 
            SET Name = coalesce(%s,Name), TotalQuantity = coalesce(%s,TotalQuantity), Price = coalesce(%s,Price)
            WHERE ProductID = %s
        """ % ("NULL" if details["Name"]=='' else details["Name"], "NULL" if details["TotalQuantity"]=='' else details["TotalQuantity"], "NULL" if details["Price"]=='' else int(details["Price"]), "NULL" if details["TotalQuantity"]=='' else int(details["TotalQuantity"]),int(details["ProductID"]))
        cur.execute(query)
        con.commit()
        print("Product Details Updated\n\n")
        
    except Exception as e:
        print("Operation failed")
        print(">>>>>>>", e)
        con.rollback()

def update_address():
    try:

        details = {}
        details["User Email Address"] = input(f"User Email Address: ")
        details["Address Line 1"] = input(f"Address Line 1: ")
        details["Address Line 2"] = input(f"Address Line 2: ")
        details["City"] = input(f"City: ")
        details["State"] = input(f"State: ")
        details["Zipcode"] = input(f"Zipcode: ")

        #print(details)
        
        query ="""
        UPDATE ADDRESS 
            SET Line1 = coalesce("%s",Line1), Line2 = coalesce("%s",Line2), City = coalesce("%s",City), State = coalesce("%s",State), Zipcode = coalesce(%s,Zipcode)
            WHERE UserEmailAddress = "%s"
        """ % ("NULL" if details["Address Line 1"]=='' else details["Address Line 1"], "NULL" if details["Address Line 2"]=='' else details["Address Line 2"], "NULL" if details["City"]=='' else details["City"], "NULL" if  details["State"]=='' else details["State"], "NULL" if details["Zipcode"]=='' else int(details["Zipcode"]), details["User Email Address"])
        cur.execute(query)
        con.commit()
        print("Address Details Updated\n\n")
        
    except Exception as e:
        print("Operation failed")
        print(">>>>>>>", e)
        con.rollback()

