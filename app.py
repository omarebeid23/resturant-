from flask import Flask, render_template

app = Flask(__name__)

# Sample restaurant data
restaurant_info = {
    "name": "Restaurant Name",
    "description": "Enjoy delicious food in a cozy atmosphere",
    "menu": [
        {"item": "Dish 1", "price": "$10"},
        {"item": "Dish 2", "price": "$12"},
        {"item": "Dish 3", "price": "$15"},
    ],
    "about": "Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    "contact": {
        "email": "info@restaurantname.com",
        "phone": "+1 (123) 456-7890",
    },
}

@app.route('/')
def homepage():
    return render_template('index.html', restaurant=restaurant_info)

if __name__ == '__main__':
    app.run(debug=True)
