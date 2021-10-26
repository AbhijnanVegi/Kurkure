def update_review():
    try:
        details = get_input(request=[
            "User Email Address",
            "Product ID",
            "Order ID",
        ])
        order_query = """SELECT * FROM ORDERS WHERE OrderId=%s""" % int(details["Order ID"])
        cur.execute(order_query)
        order_details = cur.fetchone()
        if (order_details == None):
            raise Exception("Order ID not found")
        if order_details["UserEmailAddress"] != details["User Email Address"]:
            raise Exception("Order doesn't belong to user")
        
        product_query = """SELECT * FROM PRODUCT WHERE ProductID=%s""" % int(details["Product ID"])
        cur.execute(product_query)
        product_details = cur.fetchone()
        if (product_details == None):
            raise Exception("Product ID not found")
        
        contains_query = """SELECT * FROM CONTAINS WHERE OrderId=%s AND ProductID=%s""" % (int(details["Order ID"]), int(details["Product ID"]))
        cur.execute(contains_query)
        contains_details = cur.fetchone()
        if (contains_details == None):
            raise Exception("Order doesn't contain product")

        review = get_input(request=[
            "Review",
            "Rating"
        ])
        query = """
        UPDATE REVIEW
        SET Review = coalesce(%s,Review), Rating = coalesce(%s,Rating)
        WHERE 
        """ 
        % (review["Review"], int(review["Rating"]))
        cur.execute(query)

        rev_id = cur.execute("SELECT LAST_INSERT_ID()")
        rev_id = cur.fetchone()["LAST_INSERT_ID()"]
        query = """
        INSERT INTO REVIEWSREL(UserEmailAddress,ProductID,OrderId,ReviewId)
        VALUES ("%s",%s,%s,%s) """ % (details["User Email Address"], int(details["Product ID"]), int(details["Order ID"]), rev_id)
        cur.execute(query)
        con.commit()

        print("Review inserted successfully\n\n")
    except Exception as e:
        print("Operation failed")
        print(">>>>>>>", e)
        con.rollback() 


(SELECT COUNT(*) FROM (SELECT * FROM CONTAINS NATURAL JOIN PRODUCT) AS B GROUP BY ProductID ORDER BY COUNT DSC)
        (SELECT COUNT() AS C, ProductId FROM (SELECT * FROM CONTAINS NATURAL JOIN PRODUCT) AS B GROUP BY ProductID ORDER BY C DESC)