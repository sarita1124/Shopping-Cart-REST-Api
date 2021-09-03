from flask import Flask, Response, request
import json
from bson.objectid import ObjectId
import pymongo
import os
import ssl
app=Flask(__name__)


# connecting with mongoDB database
try:
    
    DB_URI=os.getenv('DB_URI')
    client = pymongo.MongoClient(DB_URI,ssl_cert_reqs=ssl.CERT_NONE)
    

    #string_connection="mongodb+srv://testuser:testpass24@cluster0.uwvsw.mongodb.net/Shoppingdb?retryWrites=true&w=majority"
    #mongo=pymongo.MongoClient(string_connection)
    print(client.list_database_names())
    #mongo.server_info() 
    db=client.Shoppingdb
except Exception as ex:
    print("Error - Cannot connect to database")
    print(ex)


@app.route("/",methods=["GET"])
def home():
    return "Shopping Cart Application"

# create the cart
@app.route("/carts",methods=["POST"])
def create_cart():
    try:
        item  = {
            "name":request.form["name"],
            "price":request.form["price"],
            "quantity":request.form["quantity"]

        }
        dbResponse = db.carts.insert_one(item)
        print(dbResponse.inserted_id)
        return Response(
            response=json.dumps(
                {"message":"item added to cart",
                "id":f"{dbResponse.inserted_id}"}
                ),
                status=200,
                mimetype = "application/json"
            )
    except Exception as ex:
        return Response(
            response=json.dumps(
                {"message":"item not added to cart",
                "error":ex
                }
                ),
                status=500,
                mimetype = "application/json"
            )

###################################

@app.route("/carts",methods=["GET"])
def show_items_in_cart():
    try:
        data = list(db.carts.find())
        print(data)
        for item in data:
            item["_id"] = str(item["_id"])
        return Response(
            response = json.dumps(data),
            status = 200,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)
        return Response(
            response = json({"message":"Error fetching items in cart"}),
            status = 500,
            mimetype="application/json"
        )



##############################################
# update item in cart

    ## Update name of item in cart
@app.route("/carts/name/<id>", methods=["PUT"])
def update_item_name(id):
    try:
        dbResponse = db.carts.update_one(
            {"_id":ObjectId(id)},
            {"$set":{"name":request.form["name"]}}
        )
        
        if (dbResponse.modified_count > 0):
            return Response(
                response=json.dumps({"message":"Item name updated"}),
                status=200,
                mimetype="application/json"
            )
        else:
            return Response(
                response=json.dumps({"message":"Nothing to Update"}),
                status=200,
                mimetype="application/json"
            )
    except Exception as ex:
        print("**********")
        print(ex)
        print("**********")
        return Response(
            response=json.dumps({"message":"Error updating items in cart"}),
            status=500,
            mimetype="application/json"
        )


    ## Update price of item in cart
@app.route("/carts/price/<id>", methods=["PUT"])
def update_item_price(id):
    try:
        dbResponse = db.carts.update_one(
            {"_id":ObjectId(id)},
            {"$set":{"price":request.form["price"]}}
        )
        if (dbResponse.modified_count > 0):
            return Response(
                response=json.dumps({"message":"Item price updated"}),
                status=200,
                mimetype="application/json"
            )
        else:
            return Response(
                response=json.dumps({"message":"Nothing to Update"}),
                status=200,
                mimetype="application/json"
            )
    except Exception as ex:
        print("**********")
        print(ex)
        print("**********")
        return Response(
            response=json.dumps({"message":"Error updating items in cart"}),
            status=500,
            mimetype="application/json"
        )

    ## Update quantity of item in cart
@app.route("/carts/quantity/<id>", methods=["PUT"])
def update_item_quantity(id):
    try:
        dbResponse = db.carts.update_one(
            {"_id":ObjectId(id)},
            {"$set":{"quantity":request.form["quantity"]}}
        )
        if (dbResponse.modified_count > 0):
            return Response(
                response=json.dumps({"message":"Item quantity updated"}),
                status=200,
                mimetype="application/json"
            )
        else:
            return Response(
                response=json.dumps({"message":"Nothing to Update"}),
                status=200,
                mimetype="application/json"
            )
    except Exception as ex:
        print("**********")
        print(ex)
        print("**********")
        return Response(
            response=json.dumps({"message":"Error updating items in cart"}),
            status=500,
            mimetype="application/json"
        )


#####################################
# Delete  item from cart
@app.route("/carts/<id>", methods=["DELETE"])
def delete_item(id):
    try:
        dbResponse = db.carts.delete_one(
            {"_id":ObjectId(id)}
        )
        if (dbResponse.deleted_count > 0):
            return Response(
                response=json.dumps(
                    {"message":"item Deleted",
                    "id":f"{id}"}),
                status=200,
                mimetype="application/json"
            )
        else:
            return Response(
                response=json.dumps(
                    {"message":"item doesn't exist",
                    "id":f"{id}"}),
                status=200,
                mimetype="application/json"
            )
    except Exception as ex:
        print("**********")
        print(ex)
        print("**********")
        return Response(
            response=json.dumps({"message":"Error deleting items in cart"}),
            status=500,
            mimetype="application/json"
        )


#####################################
# Delete cart
@app.route("/carts", methods=["DELETE"])
def delete_cart():
    try:
        dbResponse = db.carts.delete_many({})
        if (dbResponse.deleted_count > 0):
            return Response(
                response=json.dumps(
                    {"message":"items Deleted",
                    "count":f"{dbResponse.deleted_count}"}),
                status=200,
                mimetype="application/json"
            )
        else:
            return Response(
                response=json.dumps(
                    {"message":"Cart is empty"}),
                status=200,
                mimetype="application/json"
            )
    except Exception as ex:
        print("**********")
        print(ex)
        print("**********")
        return Response(
            response=json.dumps({"message":"Error deleting items in cart"}),
            status=500,
            mimetype="application/json"
        )
   

#####################################
if (__name__ == "__main__"):
    app.run(port=5000, debug=True)


        

        
