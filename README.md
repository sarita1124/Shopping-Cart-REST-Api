# Shopping Cart REST API
A repository containing example of REST API in python with  flask  and  mongoDB, for CRUD operations on a cart.



# Problem Statement
To create a shopping cart REST API(Use Python/Mongodb) that handles CRUD
operations for a specific user like create cart, get items, add items and remove items

# Solution
## Tools  Required
- MongoDB : To create and maintain database
- Postman App : To make requests to API from client side
- Python(3.9.6) : To create the  API

## Download and Install Required  tools
- MongoDB Community Version (5.0.1) : https://www.mongodb.com/try/download/community
- Postman : https://www.postman.com/downloads/
- Python (3.9.6) : https://www.python.org/downloads/

## Required  packages for python
- flask : To work with flask framework in python
- pymongo : To work with MongoDB database from python

##### Command to  install required packages
- All  packages at once : pip install -r requirements.txt
- Individual packages : pip install <package_name> 
  - <package_name> : flask, py_mongo

## Operations that can be performed with API
- Create and/or Add items to  cart
- Get items in cart
- Update name for  item in  cart
- Update price for item in cart
- Update quantity for  item in cart
- Remove specific item from cart
- Empty cart

## Explaination about  different operations
- Create and/or  Add items to  cart :
  - By performing  this  operation, if the  collection/table doesn't  exist in MongoDB,  than it will  create the collection  and add item to  the  cart,  else if the collection already exists, then  it will add item to  existig cart.
  - EndPoint : localhost:5000/carts
  - Methods : POST
  - form_data : "name", "price",  "quantity"
- Get items in cart :
  - This operation allow  you to  get all the items present in the cart
  - EndPoint : localhost:5000/carts
  - Methods : GET
- Update name of item in cart
  - This  operation allow you to  update name of item present in the cart by providing item id.
  - EndPoint : localhost:5000/carts/name/{item_id}
  - Methods : PUT
  - form_data : "name"
- Update price of item in cart
  - This  operation allow you to  update price of item present in the cart by providing item id.
  - EndPoint : localhost:5000/carts/price/{item_id}
  - Methods : PUT
  - form_data : "price"
- Update quantity of item in cart
  - This  operation allow you to  update quantity of item present in the cart by providing item id.
  - EndPoint : localhost:5000/carts/quantity/{item_id}
  - Methods : PUT
  - form_data : "quantity"
- Remove specific item from cart
  - This operation  allows you to  remove specific item from cart by providing its item id.
  - EndPoint : localhost:5000/carts/{item_id}
  - Methods : DELETE
- Empty Cart
  - This operation  allows you to  empty your cart by  removing all  items in the cart.
  - EndPoint : localhost:5000/carts
  - Methods : DELETE

