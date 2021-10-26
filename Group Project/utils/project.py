import re
import random
import string
from tabulate import tabulate

from utils.cursor import con, cur
from utils.utils import get_input 

def above_amount():
    try:
        amount = input(f"Enter the amount : ")

        
        query ="""
        SELECT *, Price*Quantity as TotalPrice FROM (SELECT * FROM CONTAINS NATURAL JOIN PRODUCT) AS B WHERE Price*Quantity > %s
        """ % int(amount)

        
        cur.execute(query)
        count = cur.fetchall()
        con.commit()
        print("Count of orders above " + amount + " :- \n\n")

        print(tabulate(count, headers="keys", tablefmt='psql'))

    except Exception as e:
        print(cur._last_executed)
        print("Operation failed")
        print(">>>>>>>", e)
        con.rollback()

def above_rating():
    try:
        rating = input(f"Rating : ")

        query ="""
        SELECT * FROM (SELECT * FROM REVIEWSREL NATURAL JOIN REVIEW) AS B WHERE Rating > %s
        """ % (int(rating))
        
        cur.execute(query)
        count = cur.fetchall()
        con.commit()

        print("Reviews above rating " + rating +  ":- \n\n")

        print(tabulate(count, headers="keys", tablefmt='psql'))

    except Exception as e:
        print(cur._last_executed)
        print("Operation failed")
        print(">>>>>>>", e)
        con.rollback()



