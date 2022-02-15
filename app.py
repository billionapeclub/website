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
    def collections1():
        results = [
            (
                entry["_id"],
                entry["name_apes"],
                entry["image_link"],
                entry["web_link"],
            )
            for entry in billionape.find({})
        ]
        return render_template("/gallery/gallery-1.html", entries=results)

    @app.route('/gallery-2', methods=["POST", "GET"])
    def collections2():
        results = [
            (
                entry["_id"],
                entry["name_apes"],
                entry["image_link"],
                entry["web_link"],
            )
            for entry in billionape.find({})
        ]
        return render_template("/gallery/gallery-2.html", entries=results)

    @app.route('/gallery-3', methods=["POST", "GET"])
    def collections2():
        results = [
            (
                entry["_id"],
                entry["name_apes"],
                entry["image_link"],
                entry["web_link"],
            )
            for entry in billionape.find({})
        ]
        return render_template("/gallery/gallery-3.html", entries=results)

    @app.route('/gallery-4', methods=["POST", "GET"])
    def collections2():
        results = [
            (
                entry["_id"],
                entry["name_apes"],
                entry["image_link"],
                entry["web_link"],
            )
            for entry in billionape.find({})
        ]
        return render_template("/gallery/gallery-4.html", entries=results)

    @app.route('/gallery-5', methods=["POST", "GET"])
    def collections2():
        results = [
            (
                entry["_id"],
                entry["name_apes"],
                entry["image_link"],
                entry["web_link"],
            )
            for entry in billionape.find({})
        ]
        return render_template("/gallery/gallery-5.html", entries=results)

    @app.route('/gallery-6', methods=["POST", "GET"])
    def collections2():
        results = [
            (
                entry["_id"],
                entry["name_apes"],
                entry["image_link"],
                entry["web_link"],
            )
            for entry in billionape.find({})
        ]
        return render_template("/gallery/gallery-6.html", entries=results)

    @app.route('/gallery-7', methods=["POST", "GET"])
    def collections2():
        results = [
            (
                entry["_id"],
                entry["name_apes"],
                entry["image_link"],
                entry["web_link"],
            )
            for entry in billionape.find({})
        ]
        return render_template("/gallery/gallery-7.html", entries=results)

    @app.route('/gallery-8', methods=["POST", "GET"])
    def collections2():
        results = [
            (
                entry["_id"],
                entry["name_apes"],
                entry["image_link"],
                entry["web_link"],
            )
            for entry in billionape.find({})
        ]
        return render_template("/gallery/gallery-8.html", entries=results)

    @app.route('/gallery-9', methods=["POST", "GET"])
    def collections2():
        results = [
            (
                entry["_id"],
                entry["name_apes"],
                entry["image_link"],
                entry["web_link"],
            )
            for entry in billionape.find({})
        ]
        return render_template("/gallery/gallery-9.html", entries=results)

    @app.route('/gallery-10', methods=["POST", "GET"])
    def collections2():
        results = [
            (
                entry["_id"],
                entry["name_apes"],
                entry["image_link"],
                entry["web_link"],
            )
            for entry in billionape.find({})
        ]
        return render_template("/gallery/gallery-10.html", entries=results)
    

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
