# Group Project-1

## Introduction



## Purpose

This database is used to store and manage various transactions of online store. 

## Users

- User to place an order 
- Store management to manage various products and user’s orders

## Applications

- User : To store basic user details
- Address : To store the addresses of a user
- Cards Details : Store the card details of cards used by the user
- Product : Store details of the product 
- Reviews : Store reviews of product by the customer
- Order : Store details regarding order 

## Database Requirements

### Entities

1. User
   - Email
     - Char(128), Not NULL, Unique
   - Mobile Number
     - Char(128), Not NULL, Unique
   - Name
     - Composite of First name, Middle name, Last name, Not NULL
     - First name, Middle name, Last name = Char(64)
   - Premium Subscription Status
     - Boolean, Not NULL
2. Address
   - Lines
     - Composite of Address Line 1, Address Line 2, Not NULL
     - Address line 1 and Address Line 2 = Char(128)
   - City
     - Char(64), Not NULL
   - State
     - Char(64), Not NULL
   - Zip Code
     - 100000 < Integer < 999999, Not NULL
3. Product
   - ID
     - Integer, Not NULL, Unique
   - Name 
     - Char(128), Not NULL
   - Delivery availability
     - Multi valued (All cities where delivery is available), Not NULL
   - Category
     - Multi valued ( All the categories product falls into ), Not NULL
   - Price
     - Integer, Not NULL
   - Total Quantity
     - Integer, Not NULL
   - Rating
     - Average of all reviews
4. Review
   - Rating
     - Integer (1,5), Not NULL
   - Review
     - Char(1024)
5. Order
   - Order ID
     - Integer, Not NULL, Unique
   - Order status
     - One of [ Billed, In transit, Delivered ], Not NULL
   - Order Date
     - Date, Not NULL
   - Total Bill
     - Derived, Integer, Not NULL
6. Payment Method
   - Date Added
     - Date, Not NULL
   - is_default
     - Boolean, default=False, Not NULL
   - Subclasses:
     - Wallet
       - Provider (Char(32), Not NULL)
       - Auth Token (Char(128), Not NULL)
       - Balance (Integer)
     - Card Details
       - Name (Char(64), Not NULL)
       - Card Number (Integer(16 digits), Not NULL)
       - Expiry Date ( Date, Not NULL)
       - Name on card ( Char(128), Not NULL)
       - Billing address (Char(1024), Not NULL)

### Weak Entities 

`Address`, `Review`, ` Payment Method` are weak entities in this database.

### Relationships

### n > 2 Relationship

## Functional Requirements

### Modifications

### Retrieval

