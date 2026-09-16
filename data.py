PRODUCTS = [
    {"id": 1, "name": "Wireless Mouse", "category": "Electronics", "price": 599, "stock": 12, "rating": 4.2,
     "image": "mouse.png", "desc": "A smooth wireless mouse with 2.4GHz connectivity."},
    {"id": 2, "name": "Mechanical Keyboard", "category": "Electronics", "price": 2499, "stock": 5, "rating": 4.6,
     "image": "keyboard.png", "desc": "RGB backlit mechanical keyboard, blue switches."},
    {"id": 3, "name": "Notebook Set", "category": "Stationery", "price": 149, "stock": 40, "rating": 4.0,
     "image": "notebook.png", "desc": "Pack of 3 ruled notebooks, 100 pages each."},
    {"id": 4, "name": "Gel Pens (10 pack)", "category": "Stationery", "price": 99, "stock": 60, "rating": 3.8,
     "image": "pens.png", "desc": "Smooth writing gel pens in assorted colors."},
    {"id": 5, "name": "Coffee Mug", "category": "Home", "price": 249, "stock": 25, "rating": 4.4,
     "image": "mug.png", "desc": "Ceramic mug, holds 350ml, microwave safe."},
    {"id": 6, "name": "Desk Lamp", "category": "Home", "price": 899, "stock": 8, "rating": 4.1,
     "image": "lamp.png", "desc": "Adjustable LED desk lamp with 3 brightness levels.",
     "on_sale": True, "original_price": 1199},
    {"id": 7, "name": "Backpack", "category": "Bags", "price": 1499, "stock": 15, "rating": 4.5,
     "image": "backpack.png", "desc": "Water-resistant 25L backpack with laptop sleeve.",
     "on_sale": True, "original_price": 1999},
    {"id": 8, "name": "Water Bottle", "category": "Home", "price": 349, "stock": 30, "rating": 4.3,
     "image": "bottle.png", "desc": "Insulated steel bottle, keeps drinks cold for 12 hours."},
    {"id": 9, "name": "Bluetooth Earphones", "category": "Electronics", "price": 1799, "stock": 10, "rating": 4.0,
     "image": "earphones.png", "desc": "In-ear bluetooth earphones with 20 hour battery."},
    {"id": 10, "name": "Sticky Notes Pack", "category": "Stationery", "price": 79, "stock": 50, "rating": 3.9,
     "image": "sticky.png", "desc": "5 pads of colorful sticky notes."},
    {"id": 11, "name": "Phone Stand", "category": "Electronics", "price": 199, "stock": 22, "rating": 4.2,
     "image": "standphone.png", "desc": "Adjustable aluminium phone stand for desk use."},
    {"id": 12, "name": "Yoga Mat", "category": "Fitness", "price": 699, "stock": 18, "rating": 4.4,
     "image": "yogamat.png", "desc": "Non-slip 6mm yoga mat with carry strap."},
]

for _p in PRODUCTS:
    _p.setdefault("on_sale", False)
    _p.setdefault("original_price", _p["price"])

CATEGORIES = ["Electronics", "Stationery", "Home", "Bags", "Fitness"]

REVIEWS = {
    1: [{"rating": 5, "text": "Great mouse, very responsive."}, {"rating": 4, "text": "Good but a bit small."}],
    2: [{"rating": 5, "text": "Best keyboard I've used."}, {"rating": 5, "text": "Love the clicky sound."},
        {"rating": 4, "text": "A bit loud for shared rooms."}],
    3: [{"rating": 4, "text": "Good quality paper."}],
    5: [{"rating": 5, "text": "Perfect size for coffee."}, {"rating": 3, "text": "Handle is a bit thin."}],
    7: [{"rating": 5, "text": "Fits a 15 inch laptop easily."}, {"rating": 4, "text": "Zippers feel sturdy."}],
    9: [{"rating": 3, "text": "Battery life is okay, not great."}, {"rating": 4, "text": "Good sound for the price."}],
}

COUPONS = {
    "STUDENT10": 0.10,
    "WELCOME5": 0.05,
}
