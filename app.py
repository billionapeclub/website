import os
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
from flask import Flask, render_template, url_for, request
from flask_paginate import Pagination, get_page_args

load_dotenv()

client = MongoClient(os.environ.get("MONGODB_URI"))
db = client.billionape
billionape = db.billionape
rarities = db.rarities
pages = db.pages

results = [
            (
                entry["_id"],
                entry["name_apes"],
                entry["image_link"],
                entry["web_link"],
            )
            for entry in billionape.find({})
        ]
bac_images = range(1875)

amc_results = [
            (
                entry["_id"],
                entry["rarities"],
                entry["name"],
                entry["chain_link"],
                entry["rank"],
                entry["rarity_score"],
                entry["image_link"],
                entry["web_link"],
                entry['mint_link'],
                entry['num_layers'],
            )
            for entry in rarities.find({})
        ]
amc_images = range(len(amc_results))

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template('index.html')

    
    def get_bac_images(page, offset=0, per_page=10):
        offset = ((page - 1) * 52)
        return bac_images[offset: offset + per_page]

    @app.route('/gallery')
    def collections():
        page, per_page, offset = get_page_args(page_parameter='page', 
                                               per_page_parameter='per_page'
                                               )
        per_page = 52
        total = len(bac_images)
        pagination_users = get_bac_images(page=page,
                                      offset=offset, 
                                      per_page=per_page
                                      )


        pagination = Pagination(page=page, 
                                per_page=per_page, 
                                total=total, 
                                css_framework='bootstrap5'
                                )
        
        numbers = range(len(results))
        return render_template("/gallery/gallery.html", 
                                entries=results, 
                                numbers=numbers, 
                                users=pagination_users,
                                page=page,
                                per_page=per_page,
                                pagination=pagination,
                                )

    def get_amc_images(page, offset=0, per_page=10):
        offset = ((page - 1) * 52)
        return amc_images[offset: offset + per_page]

    @app.route('/amc')
    def amccollection():
        page, per_page, offset = get_page_args(page_parameter='page', 
                                               per_page_parameter='per_page'
                                               )
        per_page = 52
        total = len(amc_images)
        pagination_users = get_amc_images(page=page,
                                      offset=offset, 
                                      per_page=per_page
                                      )


        pagination = Pagination(page=page, 
                                per_page=per_page, 
                                total=total, 
                                css_framework='bootstrap5'
                                )
        
        numbers = range(len(amc_results))
        return render_template("/amc/amc.html", 
                                entries=amc_results, 
                                numbers=numbers, 
                                users=pagination_users,
                                page=page,
                                per_page=per_page,
                                pagination=pagination,
                                )

    def get_amc_apes(page, offset=0, per_page=10):
        offset = ((page - 1) * 1)
        return amc_images[offset: offset + per_page]

    @app.route('/amc/apes')
    def amc_apes():
        page, per_page, offset = get_page_args(page_parameter='page', 
                                               per_page_parameter='per_page'
                                               )
        per_page = 1
        total = len(amc_images)
        pagination_users = get_amc_apes(page=page,
                                      offset=offset, 
                                      per_page=per_page
                                      )


        pagination = Pagination(page=page, 
                                per_page=per_page, 
                                total=total, 
                                css_framework='bootstrap5'
                                )
        
        numbers = range(len(amc_results))
        return render_template("/amc/apes/ape-1.html", 
                                entries=amc_results, 
                                numbers=numbers, 
                                users=pagination_users,
                                page=page,
                                per_page=per_page,
                                pagination=pagination,
                                )

    if __name__ == '__main__':
        app.run(debug=True)

    return app
