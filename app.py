from flask import Flask, render_template

app = Flask(__name__)

# Data for all 4 wallpaper packs
PRODUCTS = [
    {
        "id": "01",
        "name": "Starter Pack",
        "price": "2.99",
        "subtitle": "Essential clean backgrounds to refresh your daily setup.",
        "support_email": "support@studiowallpapers.com",
        "stripe_link": "YOUR_STRIPE_LINK_1",
        "included": [
            "2x Desktop Wallpapers (16:9 / Ultrawide)",
            "2x Mobile Wallpapers (iPhone & Android)",
            "Instant digital download (.zip archive)",
            "Lifetime access to future updates",
            "Standard HD Quality Files"
        ],
        "previews": ["#1a1a22", "#111d2e", "#221616", "#18241b"]
    },
    {
        "id": "02",
        "name": "Pro Creator Pack",
        "price": "3.99",
        "subtitle": "Expanded collection tailored for dual-monitor workflows.",
        "support_email": "support@studiowallpapers.com",
        "stripe_link": "YOUR_STRIPE_LINK_2",
        "included": [
            "4x Desktop Wallpapers (16:9 / Ultrawide)",
            "4x Mobile Wallpapers (iPhone & Android)",
            "Instant digital download (.zip archive)",
            "Lifetime access to future updates",
            "Dual-Monitor Matching Sets",
            "Standard HD Quality Files"
        ],
        "previews": ["#141419", "#1b2214", "#22141f", "#142220"]
    },
    {
        "id": "03",
        "name": "Studio Collection",
        "price": "5.99",
        "subtitle": "Comprehensive set upgraded to crisp 4K Ultra HD resolution.",
        "support_email": "support@studiowallpapers.com",
        "stripe_link": "YOUR_STRIPE_LINK_3",
        "included": [
            "7x Desktop Wallpapers (16:9 / Ultrawide)",
            "7x Mobile Wallpapers (iPhone & Android)",
            "Instant digital download (.zip archive)",
            "Lifetime access to future updates",
            "Dual-Monitor Matching Sets",
            "Crisp 4K Ultra HD Quality Files"
        ],
        "previews": ["#1e1b2e", "#2e1b1b", "#1b2e25", "#29291b"]
    },
    {
        "id": "04",
        "name": "Ultimate Mega Bundle",
        "price": "7.99",
        "subtitle": "The complete archive with every extra asset and raw file.",
        "support_email": "support@studiowallpapers.com",
        "stripe_link": "YOUR_STRIPE_LINK_4",
        "included": [
            "16x Desktop Wallpapers (16:9 / Ultrawide)",
            "16x Mobile Wallpapers (iPhone & Android)",
            "Instant digital download (.zip archive)",
            "Lifetime access to future updates",
            "Dual-Monitor Matching Sets",
            "Crisp 4K Ultra HD Quality Files",
            "Bonus iPad & Tablet Specific Aspect Ratios",
            "Uncompressed Raw Asset Files",
            "VIP Discord Community Access"
        ],
        "previews": ["#22182b", "#18262b", "#2b2518", "#2b1818"]
    }
]

@app.route('/')
def home():
    return render_template('index.html', products=PRODUCTS)

if __name__ == '__main__':
    app.run(debug=True)
