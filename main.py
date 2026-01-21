import firebase_admin
from firebase_admin import credentials, firestore

#Firebase Information:
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
products = db.collection("products")
##print("Firebase connected successfully!")


##--------Now This starts the Firebase Firestore CRUD Operations--------##

# This Adds a new product to the "Products" collection in Firestore
db.collection("products").add({
    "category": "Drinkware",
    "description": "A durable and insulated water bottle that keeps drinks cold for hours",
    "in_stock": True,
    "name": "Insulated Water Bottle",
    "price" : 15.00,
})
print("Your product has been added to the database!")


# for doc in db.collection("products").stream():
#    print(doc.id, doc.to_dict())

# #This will Read all the Products name that are in the "Product's collection" in Firestore
products = db.collection("products")

docs = products.stream()
for doc in docs:
    data = doc.to_dict()
    print(data.get("name"))

