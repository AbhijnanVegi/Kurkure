import re

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
