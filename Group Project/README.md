# Group Project
**Team Name** : Kurkure

# About
A model database of an online shopping website created as a part of Data and applications course@IIITH.

# Installation
You will need `docker` and `docker-compose` to run this project.  
After installing the above dependencies run the following commands  
```
docker-compose up -d

pip install -r requirements.txt
```
Initialise the database by running the following command
```
docker exec -i mysql sh -c 'exec mysql -uroot -p"$MYSQL_ROOT_PASSWORD" db' < dump.sql
```
To run the application run
```
python main.py
```
# Useful commands
To access the mysql console run
```
docker exec -it mysql mysql -uroot --password=password db
```
To create a new dump file run
```
docker exec mysql sh -c 'exec mysqldump -uroot -p"$MYSQL_ROOT_PASSWORD" db' > dump.sql
```
# List of commands 

 **0. Exit [EXIT]**

Exit from the program

 **1. Add a new user [INSERT]**

Insert a user to database

 **2. Add a new product [INSERT]**

Insert a product to database

 **3. Add a new address [INSERT]**

Insert a new address for a user

 **4. Add a new payment method [INSERT]**

Insert a new payment method for a user

 **5. Add a review to a product [INSERT]**

Insert a product review

 **6. Update Product details [UPDATE]**

update a product's details

 **7. Update Address details [UPDATE]**

update an address details

 **8. Update Payment details [UPDATE]**

update a payment method's details 

 **9. Update Review details [UPDATE]**

update a review's details

 **10. Delete a product [DELETE]**

Delete a product from database

**11  Delete an address [DELETE]**

delete an address for a user

**12  Delete a review [DELETE]**

delete a review from db

 **13. Display all products [SELECT]**

display all products in db

 **14. Display user details [SELECT]**

display details of all users in db

 **15. List of all orders above the value of certain amount [PROJECT]**

List of all orders above the value of certain amount

 **16. List of all reviews for a particular product rated above a certain rating [PROJECT]**

List of all reviews for a particular product rated above a certain rating 

 **17. Product with maximum sales [AGGREGATE]**

display the product with maximum sales

 **18. Product with highest reviews in a category [AGGREGATE]**

display a product with highest reviews 

 **19. Search a product based on name [SEARCH]**

Search a product based on name

# [Link to video](https://iiitaphyd-my.sharepoint.com/:v:/g/personal/shavak_kansal_students_iiit_ac_in/ETE-WoxBpStItlWFfNovufkBuVMVf6T0qz1JAYJHlbNqWw?e=fG1D5v)

---

