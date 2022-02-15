import os
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
from flask import Flask, render_template, url_for, request, jsonify

load_dotenv()

client = MongoClient(os.environ.get("MONGODB_URI"))
db = client.billionape
billionape = db.billionape
rarities = db.rarities
pages = db.pages

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/gallery-1', methods=["POST", "GET"])
    def collections():
        results = [
            (
                entry["_id"],
                entry["name_apes"],
                entry["image_link"],
                entry["web_link"],
            )
            for entry in billionape.find({})
        ]
        numbers = range(len(results))
        return render_template("/gallery/gallery-1.html", entries=results, numbers=numbers)

    @app.route('/amc')
    def amccollection1():
        results = [
            (
                entry["_id"],
                entry["rarities"],
                entry["name"],
                entry["chain_link"],
                entry["rank"],
                entry["rarity_score"],
                entry["image_link"],
                entry["web_link"],
            )
            for entry in rarities.find({})
        ]
        numbers = range(len(results))
        return render_template('/amc/amc.html', entries=results, numbers=numbers)

    if __name__ == '__main__':
        app.run(debug=True)

    return app
