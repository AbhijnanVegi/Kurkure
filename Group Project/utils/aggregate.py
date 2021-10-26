import re
import random
import string

from utils.cursor import con, cur
from utils.utils import get_input 

def max_sales():
    try:

        query ="""
        SELECT SUM(QUANTITY) AS Count, ProductId FROM (SELECT * FROM CONTAINS NATURAL JOIN PRODUCT) AS B GROUP BY ProductID ORDER BY Count DESC
        """
        cur.execute(query)
        max = cur.fetchone()
        print("ProductID of the product with maximum sales : " + str(max["ProductId"]))
        con.commit()    
    
    except Exception as e:
        print(cur._last_executed)
        print("Operation failed")
        print(">>>>>>>", e)
        con.rollback()    

def max_rating():
    try:
        
        query ="""
        SELECT AVG(Rating) as AvgRating, ProductId FROM (SELECT * FROM REVIEWSREL NATURAL JOIN REVIEW) AS B GROUP BY ProductID ORDER BY AvgRating DESC
        """
        cur.execute(query)
        max = cur.fetchone()
        print("ProductID of the product with maximum rating : " + str(max["ProductId"]))
        con.commit()    
    
    except Exception as e:
        print(cur._last_executed)
        print("Operation failed")
        print(">>>>>>>", e)
        con.rollback()   
