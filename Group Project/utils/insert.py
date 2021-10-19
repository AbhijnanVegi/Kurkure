import re
import random
import string

from utils.cursor import con, cur
from utils.utils import get_input 

def insert_user():
    """
    Insert a new user into db
    """
    try: 
        details = get_input(request=[
            "Email Address",
            "First Name",
            "Middle Name",
            "Last Name",
            "Subcription Status",
            "Mobile Number"
        ])
        query ="""
        INSERT INTO USER (EmailAddress, FirstName, MiddleName, LastName, SubscriptionStatus, MobileNumber)
        VALUES ("%s","%s","%s","%s",%s,"%s")
        """ % (details["Email Address"], details["First Name"], details["Middle Name"], details["Last Name"], details["Subcription Status"], int(details["Mobile Number"]))
        
        # Domain error handling 
        if (len(details["Mobile Number"]) != 10):
            raise Exception("Mobile Number must be 10 digits")
        elif not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', details["Email Address"]):
            raise Exception(f"Invalid Email Address {details['Email Address']}")

        cur.execute(query)
        con.commit()
        print("User inserted successfully\n\n")
    except Exception as e:
        print("Operation failed")
        print(">>>>>>>", e)

def insert_product():
    """
    Insert a new product into db
    """
    try:
        details = get_input(request=[
            "Product ID",
            "Name",
            "Total quantity",
            "Price",
        ])
        query ="""
        INSERT INTO PRODUCT (ProductID, Name, TotalQuantity, Price)
        VALUES (%s,"%s",%s,%s)
        """ % (int(details["Product ID"]), details["Name"], int(details["Total quantity"]), int(details["Price"]))

        # Domain error handling
        if (int(details["Total quantity"]) < 0):
            raise Exception("Total quantity cannot be negative")
        elif (int(details["Price"]) < 0):
            raise Exception("Price cannot be negative")
        
        cur.execute(query)

        locations = input("Enter comma separated values for delivery availability: ")
        locations = locations.split(",")
        for location in locations:
            query = """
            INSERT INTO DELIVERY_AVAILABILITY (ProductID, Location)
            VALUES (%s,"%s")
            """ % (int(details["Product ID"]), location)
            cur.execute(query)
        
        categories = input("Enter comma separated values for product categories: ")
        categories = categories.split(",")
        for category in categories:
            query = """
            INSERT INTO CATEGORY (ProductID, Category)
            VALUES (%s,"%s")
            """ % (int(details["Product ID"]), category)
            cur.execute(query)

        con.commit()
        print("Product inserted successfully\n\n")
    except Exception as e:
        print("Operation failed")
        print(">>>>>>>", e)
        con.rollback()

def insert_address():
    try:
        details = get_input(request=[
            "User Email Address",
            "Address Line 1",
            "Address Line 2",
            "City",
            "State",
            "Zipcode"
        ])
        query ="""
        INSERT INTO ADDRESS (UserEmailAddress, Line1, Line2, City, State, Zipcode)
        VALUES ("%s","%s","%s","%s","%s",%s)
        """ % (details["User Email Address"], details["Address Line 1"], details["Address Line 2"], details["City"], details["State"], int(details["Zipcode"]))

        # Domain error handling
        if (int(details["Zipcode"]) < 0):
            raise Exception("Zipcode cannot be negative")
        elif (len(details["Zipcode"]) != 6):
            raise Exception("Zipcode must be 6 digits")
        
        cur.execute(query)
        con.commit()
        print("Address inserted successfully\n\n")
    except Exception as e:
        print("Operation failed")
        print(">>>>>>>", e)
        con.rollback()

def insert_payment():
    try:
        details = get_input(request=[
            "User Email Address",
            "Name",
            "Set as default [y/N]"
        ])
        query ="""
        INSERT INTO PAYMENT_METHOD (UserEmailAddress, Name, IsDefault)
        VALUES ("%s","%s",%s)
        """ % (details["User Email Address"], details["Name"], details["Set as default [y/N]"] == "y")
    
        # Domain error handling
        if (details["Set as default [y/N]"] not in ["y","n",""]):
            raise Exception("Input to 'Set as default' must be y/n")
        
        cur.execute(query)
        
        ptype = input("Payment Methods : 1.Wallet 2.Card\nEnter payment method type: ")
        if (ptype == "1"):
            wallet_details = get_input(request=[
                "Provider"
            ])
            characters = string.ascii_letters + string.digits 
            auth_token = "".join(random.choice(characters) for i in range(128))
            balance = random.randint(0, 100000)
            query = """
            INSERT INTO WALLET (UserEmailAddress, Name, Provider, AuthToken, Balance)
            VALUES ("%s","%s","%s","%s",%s)
            """ % (details["User Email Address"], details["Name"], wallet_details["Provider"],auth_token, balance)
        elif ptype == "2":
            card_details = get_input(request=[
                "Card Number",
                "Expiry Date",
                "Name of card holder",
                "Billing address"
            ])
            query = """
            INSERT INTO CARD(UserEmailAddress, Name, CardNumber, ExpiryDate, NameOfCardHolder, BillingAddress)
            VALUES ("%s","%s","%s","%s","%s","%s")
            """ % (details["User Email Address"], details["Name"], card_details["Card Number"], card_details["Expiry Date"], card_details["Name of card holder"], card_details["Billing address"])

            # Domain error handling
            if (len(card_details["Card Number"]) != 16):
                raise Exception("Card Number must be 16 digits")
            elif (not re.fullmatch(r"(0[1-9]|1[0-2])\/?([0-9]{2})", card_details["Expiry Date"])):
                raise Exception("Invalid Expiry Date")
        else:
            raise Exception("Invalid payment method type")

        cur.execute(query)
        con.commit()
        print("Payment inserted successfully\n\n")
    except Exception as e:
        print("Operation failed")
        print(">>>>>>>", e)
        con.rollback()