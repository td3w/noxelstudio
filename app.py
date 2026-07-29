from flask import Flask, render_template

app = Flask(__name__)

# Elite product catalog for Noxel Studio
PRODUCTS = [
    {
        "id": "01",
        "name": "Starter Pack",
        "subtitle": "Essential clean backgrounds for daily setup.",
        "price": "2.99",
        "included": [
            "2x Desktop Wallpapers (16:9 / Ultrawide)",
            "2x Mobile Wallpapers (iPhone & Android)",
            "Instant digital download (.zip archive)",
            "Lifetime access to future updates",
            "Standard HD Quality Files"
        ],
        "stripe_link": "https://buy.stripe.com/your_link_1"
    },
    {
        "id": "02",
        "name": "Pro Creator",
        "subtitle": "Optimized ultrawide setups and sleek aesthetics.",
        "price": "4.99",
        "included": [
            "5x Ultrawide & Dual Monitor Wallpapers",
            "Custom Mobile Lockscreen Crops",
            "Instant digital download (.zip archive)",
            "Lifetime access to future updates",
            "4K Ultra HD Crisp Resolution"
        ],
        "stripe_link": "https://buy.stripe.com/your_link_2"
    },
    {
        "id": "03",
        "name": "Studio Edition",
        "subtitle": "Complete designer archive for advanced visual workflows.",
        "price": "5.99",
        "included": [
            "Full Library of Dynamic Wallpapers",
            "Optimized for High-PPI OLED & Retina Displays",
            "Instant digital download (.zip archive)",
            "Lifetime access to future updates",
            "Master Resolution Archives"
        ],
        "stripe_link": "https://buy.stripe.com/your_link_3"
    },
    {
        "id": "04",
        "name": "Ultimate Mega Bundle",
        "subtitle": "All current & future releases in one master package.",
        "price": "7.99",
        "included": [
            "Complete Noxel Studio Asset Vault",
            "Priority Support & Early Access Passes",
            "Instant digital download (.zip archive)",
            "Lifetime access to future updates",
            "Exclusive Unreleased Drops"
        ],
        "stripe_link": "https://buy.stripe.com/your_link_4"
    }
]

@app.route('/')
def index():
    return render_template('index.html', products=PRODUCTS)

if __name__ == '__main__':
    app.run(debug=True)
