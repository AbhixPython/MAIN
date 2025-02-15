from flask import Flask, render_template_string
import requests
import re
import time
import os

app = Flask(__name__)
app.debug = True

html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WELCOME TO THE [ SERVERX ] </title>
    <style>
        body {
            font-family: sans-serif;
            background-color: #111; /* Dark background as in the image */
            color: #fff; /* Light text color for contrast */
            margin: 0;
            padding: 0;
        }

        .container {
            max-width: 600px; /* Adjust as needed */
            margin: 20px auto;
            padding: 20px;
        }

        .service-box {
            background-color: #222; /* Slightly lighter background for boxes */
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 8px;
            text-align: center; /* Center the content */
            overflow: hidden; /* Ensure image stays within box */
        }

        .service-box img {
            max-width: 100%; /* Make image responsive */
            height: auto;
            display: block; /* Prevent image from affecting text alignment */
            margin-bottom: 10px;
        }

        .service-title {
            font-weight: bold;
            margin-bottom: 10px;
        }

        .service-description {
            color: #ccc; /* Slightly lighter text for description */
        }

        .orange-button {
            background-color: #f26a25; /* Orange button color */
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            text-decoration: none;
            display: inline-block; /* Make it behave like a link */
            margin-top: 10px;
        }

        /* Responsive adjustments as needed */
        @media (max-width: 400px) {
            .container {
                padding: 10px;
            }

            .service-box {
                padding: 10px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>SERVERX SERVICES</h1>

        <div class="service-box">
            <img src="https://i.ibb.co/d9bVjnC/20250214-192622.jpg" alt="">
            <div class="service-title">CONVO TOOL</div>
            <div class="service-description"></div>
            <a href="#" class="orange-button">Visit</a>
        </div>

        <div class="service-box">
            <img src="https://i.ibb.co/LzDWK38f/20250214-193025.jpg" alt="">
            <div class="service-title">SINGLE CHEAKER</div>
            <div class="service-description"></div>
            <a href="https://tokencheck.darkester.online/" class="orange-button">Visit</a>
        </div>

        <div class="service-box">
            <img src="https://i.ibb.co/4ggT0MTQ/20250214-193711.jpg" alt="">
            <div class="service-title">TOKEN GENERATOR</div>
            <div class="service-description"></div>
            <a href="https://generator.darkester.online/" class="orange-button">Visit</a>
        </div>

        <div class="service-box">
            <img src="https://i.ibb.co/jvsKNcGg/20250214-194349.jpg" alt="">
            <div class="service-title">PAGE TOKEN + TID EXTRACTOR </div>
            <div class="service-description"></div>
            <a href="https://pagetoken.darkester.online/" class="orange-button">Visit</a>
        </div>

        <div class="service-box">
            <img src="https://i.ibb.co/5hvSP0wW/20250214-195001.jpg" alt="">
            <div class="service-title">FILTER TOKEN</div>
            <div class="service-description"></div>
            <a href="https://filter.darkester.online/" class="orange-button">Visit</a>
        </div>

        <div class="service-box">
            <img src="https://i.ibb.co/7tvHDSLY/20250214-195836.jpg" alt="">
            <div class="service-title">COOKIE TO JSON</div>
            <div class="service-description"></div>
            <a href="https://jsoncookie.darkester.online/" class="orange-button">Visit</a>
        </div>

        <div class="service-box">
            <img src="https://i.ibb.co/G30GM3vW/20250214-205835.jpg" alt="">
            <div class="service-title">SERVERXHUB</div>
            <div class="service-description"></div>
            <a href="https://desihub.darkester.online/" class="orange-button">Visit</a>
        </div>
    </div>
</body>
</html>'''

@app.route('/')
def home():
    return render_template_string(html_content)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
