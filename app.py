from flask import Flask, render_template

app = Flask(__name__)

# Product catalog for Noxel Studio
PRODUCTS = [
    {
        "id": "01",
        "name": "Starter Pack",
        "subtitle": "Essential clean backgrounds to refresh your daily setup.",
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
        "subtitle": "Optimized ultrawide setups for professional creators.",
        "price": "4.99",
        "included": [
            "5x Ultrawide Wallpapers (21:9 / 32:9)",
            "4x Mobile Lockscreen & Home Wallpapers",
            "Instant digital download (.zip archive)",
            "Lifetime access to future updates",
            "4K Ultra HD Crisp Files"
        ],
        "stripe_link": "https://buy.stripe.com/your_link_2"
    },
    {
        "id": "03",
        "name": "Studio Edition",
        "subtitle": "Complete aesthetic designer archive for immersive setups.",
        "price": "5.99",
        "included": [
            "10x Curated Studio Wallpapers",
            "Dynamic Dual-Monitor Matching Sets",
            "Instant digital download (.zip archive)",
            "Lifetime access to future updates",
            "Uncompressed Master Files"
        ],
        "stripe_link": "https://buy.stripe.com/your_link_3"
    },
    {
        "id": "04",
        "name": "Ultimate Mega Bundle",
        "subtitle": "All current & future releases in one master package.",
        "price": "7.99",
        "included": [
            "Full Noxel Studio Wallpaper Vault",
            "Priority Access to All Future Drops",
            "Instant digital download (.zip archive)",
            "Lifetime access to future updates"
        ],
        "stripe_link": "https://buy.stripe.com/your_link_4"
    }
]

@app.route('/')
def index():
    return render_template('index.html', products=PRODUCTS)

if __name__ == '__main__':
    app.run(debug=True)
