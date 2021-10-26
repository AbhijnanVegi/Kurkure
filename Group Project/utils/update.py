import re
import random
import string

from utils.cursor import con, cur
from utils.utils import get_input 

def update_productdetails():

    print("Hello There")
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

def update_address1():
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
        """ % (details["Address Line 1"], details["Address Line 2"], details["City"], details["State"], int(details["Zipcode"]), details["User Email Address"])
        cur.execute(query)
        con.commit()
        print("Address Details Updated\n\n")
        
    except Exception as e:
        print("Operation failed")
        print(">>>>>>>", e)
        con.rollback()

def update_address():
    try:

        details = {}
        details["User Email Address"] = input(f"User Email Address: ")

        contains_query = """SELECT * FROM ADDRESS WHERE UserEmailAddress="%s" """ % (details["User Email Address"])
        cur.execute(contains_query)
        contains_details = cur.fetchone()
        
        # print(contains_details)

        details["Address Line 1"] = input(f"Address Line 1: ")
        details["Address Line 2"] = input(f"Address Line 2: ")
        details["City"] = input(f"City: ")
        details["State"] = input(f"State: ")
        details["Zipcode"] = input(f"Zipcode: ")

        
        
        if(details["Address Line 1"]==''):
            details["Address Line 1"] = contains_details["Line1"]
        
        if(details["Address Line 2"]==''):
            details["Address Line 2"] = contains_details["Line2"]
        
        if(details["City"]==''):
            details["City"] = contains_details["City"]
        
        if(details["State"]==''):
            details["State"] = contains_details["State"]
        
        if(details["Zipcode"]==''):
            details["Zipcode"] = contains_details["Zipcode"]
        
        
        query ="""
        UPDATE ADDRESS 
            SET Line1 = "%s" , Line2 = "%s", City = "%s", State = "%s", Zipcode = %s
            WHERE UserEmailAddress = "%s"
        """ % (details["Address Line 1"], details["Address Line 2"], details["City"], details["State"], int(details["Zipcode"]), details["User Email Address"])
        cur.execute(query)
        con.commit()
        
        # contains_query = """SELECT * FROM ADDRESS WHERE UserEmailAddress="%s" """ % (details["User Email Address"])
        # cur.execute(contains_query)
        # contains_details = cur.fetchone()
        # print(contains_details)

        print("Address Details Updated\n\n")
        
    except Exception as e:
        print(cur._last_executed)
        print("Operation failed")
        print(">>>>>>>", e)
        con.rollback()
