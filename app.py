from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    product = {
        "name": "Studio Wallpapers Vol. 1",
        "subtitle": "8 high-resolution wallpapers engineered for desktop monitors and mobile screens.",
        "price": 2.99,
        "currency": "EUR",
        "items_count": 8,
        "resolution": "4K Ultra-HD (Uncompressed PNGs)",
        "support_email": "studiowallpapers.support@proton.me",
        "included": [
            "4x Desktop Wallpapers (16:9 / Ultrawide ready)",
            "4x Mobile Wallpapers (Optimized for iPhone & Android)",
            "Instant digital download (.zip archive)",
            "Lifetime access to future updates"
        ]
    }
    return render_template('index.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
