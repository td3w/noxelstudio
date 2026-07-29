# Updating the exact python file to match your requested product catalog and bullet points.

flask_code = """from flask import Flask, render_template

app = Flask(__name__)

# Product catalog for Noxel Studio
PRODUCTS = [
    {
        "id": "01",
        "name": "Starter Pack",
        "subtitle": "Essential clean backgrounds to refresh your daily setup.",
        "price": "2.99",
        "included": [
            "2x Desktop Wallpapers (16:9 / Ultrawide ready)",
            "2x Mobile Wallpapers (Optimized for iPhone & Android)",
            "Instant digital download (.zip archive)",
            "Lifetime access to future updates",
            "Added Perk: Standard HD Quality Files (Crisp resolution for daily use)"
        ],
        "stripe_link": "https://buy.stripe.com/your_link_1"
    },
    {
        "id": "02",
        "name": "Pro Creator Pack",
        "subtitle": "Optimized ultrawide setups for professional creators.",
        "price": "3.99",
        "included": [
            "4x Desktop Wallpapers (16:9 / Ultrawide ready)",
            "4x Mobile Wallpapers (Optimized for iPhone & Android)",
            "Instant digital download (.zip archive)",
            "Lifetime access to future updates",
            "Added Perk: Dual-Monitor Matching Sets (Coordinated wallpapers designed to span across two screens seamlessly)"
        ],
        "stripe_link": "https://buy.stripe.com/your_link_2"
    },
    {
        "id": "03",
        "name": "Studio Collection",
        "subtitle": "Complete aesthetic designer archive for immersive setups.",
        "price": "5.99",
        "included": [
            "7x Desktop Wallpapers (16:9 / Ultrawide ready)",
            "7x Mobile Wallpapers (Optimized for iPhone & Android)",
            "Instant digital download (.zip archive)",
            "Lifetime access to future updates",
            "Added Perks:",
            "Dual-Monitor Matching Sets",
            "Exclusive Minimalist Light & Dark Mode Variants (Perfect for automatic OS theme switching)"
        ],
        "stripe_link": "https://buy.stripe.com/your_link_3"
    },
    {
        "id": "04",
        "name": "Ultimate Mega Bundle",
        "subtitle": "All current & future releases in one master package.",
        "price": "7.99",
        "included": [
            "16x Desktop Wallpapers (16:9 / Ultrawide ready)",
            "16x Mobile Wallpapers (Optimized for iPhone & Android)",
            "Instant digital download (.zip archive)",
            "Lifetime access to future updates",
            "Added Perks:",
            "Dual-Monitor & Triple-Monitor Matching Sets",
            "Exclusive Light & Dark Mode Variants",
            "Bonus iPad & Tablet Specific Aspect Ratios (Optimized crop for tablets)",
            "VIP Discord Community Access (Early sneak peeks at upcoming wallpaper drops)"
        ],
        "stripe_link": "https://buy.stripe.com/your_link_4"
    }
]

@app.route('/')
def index():
    return render_template('index.html', products=PRODUCTS)

if __name__ == '__main__':
    app.run(debug=True)
"""

with open("app.py", "w") as f:
    f.write(flask_code)

print("Successfully updated app.py with your exact pricing and bullet points.")
