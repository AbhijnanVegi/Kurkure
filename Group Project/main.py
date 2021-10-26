import subprocess as sp
from utils.cursor import con
from utils.insert import insert_user,insert_product,insert_address,insert_payment, insert_review
from utils.select import select_user,select_product
from utils.delete import delete_product,delete_address,delete_review
from utils.update import update_productdetails, update_address, update_review, update_payment
from utils.search import search_product
from utils.analysis import below_avg
from utils.project import above_amount, above_rating
from utils.aggregate import max_rating, max_sales

OPTIONS = """
Choose the option corresponding to the action you want to perform:
0. Exit [EXIT]
1. Add a new user [INSERT]
2. Add a new product [INSERT]
3. Add a new address [INSERT]
4. Add a new payment method [INSERT]
5. Add a review to a product [INSERT]
6. Update Product details [UPDATE]
7. Update Address details [UPDATE]
8. Update Payment details [UPDATE]
9. Update Review details [UPDATE]
10. Delete a product [DELETE]
11  Delete an address [DELETE]
12  Delete a review [DELETE]
13. Display all products [SELECT]
14. Display user details [SELECT]
15. List of all orders above the value of certain amount [PROJECT]
16. List of all reviews for a particular product rated above a certain rating [PROJECT]
17. Product with maximum sales [AGGREGATE]
18. Product with highest reviews in a category [AGGREGATE]
19. Search a product based on name [SEARCH]
20. List of products less than average rating for that category
Option: """


def dispatch(opt):
    functions = {
        0: exit,
        1: insert_user,
        2: insert_product,
        3: insert_address,
        4: insert_payment,
        5: insert_review,
        6: update_productdetails,
        7: update_address,
        8: update_payment, 
        9: update_review,
        10: delete_product,
        11: delete_address,
        12: delete_review,
        13: select_product,
        14: select_user,
        15: above_amount,
        16: above_rating, 
        17: max_sales,
        18: max_rating,
        19: search_product,
        20: below_avg
    }
    try:
        functions[opt]()
    except KeyError:
        print("Invalid option\n\n")

def main():
    _ = sp.call('clear', shell=True)
    if not con.open:
        print("There was an error connecting to database")
        exit(0)    
    while(True):
        _ = sp.call('clear', shell=True)
        try:
            opt = int(input(OPTIONS))
            _ = sp.call('clear', shell=True)
            dispatch(opt)
            _ = input("Press enter to continue...")
        except ValueError:
            print("Invalid option\n\n")
            _ = input("Press enter to continue...")
        except EOFError:
            break

if __name__ == "__main__":
    main()

        


