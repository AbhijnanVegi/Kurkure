import re
import random
import string

from utils.cursor import con, cur
from utils.utils import get_input 

def below_avg():
    try:
        ''' Products with less than the average rating. '''
        query ="""
        SELECT AVG(Rating) as AvgRating, ProductId FROM (SELECT * FROM REVIEWSREL NATURAL JOIN REVIEW) AS B GROUP BY ProductID ORDER BY AvgRating DESC
        """
        # avg = cur.fetchone()
        cur.execute(query)
        products = cur.fetchall()
        print("ProductID of the product with maximum rating : " + str(max["ProductId"]))
        con.commit()    
    
    except Exception as e:
        print(cur._last_executed)
        print("Operation failed")
        print(">>>>>>>", e)
        con.rollback()   