import os
from pymongo import MongoClient
from dotenv import load_dotenv
from flask import Flask, render_template, url_for, request
from entries import *
from amc_entries import *

load_dotenv()

client = MongoClient(os.environ.get("MONGODB_URI"))
db = client.billionape


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template('index.html')


    @app.route('/gallery-1')
    def collections():
        return render_template('/gallery/gallery-1.html', entries=entries1)

    @app.route('/gallery-2')
    def collections2():
        return render_template('/gallery/gallery-2.html', entries=entries2)

    @app.route('/gallery-3')
    def collections3():
        return render_template('/gallery/gallery-3.html', entries=entries3)

    @app.route('/gallery-4')
    def collections4():
        return render_template('/gallery/gallery-4.html', entries=entries4)

    @app.route('/gallery-5')
    def collections5():
        return render_template('/gallery/gallery-5.html', entries=entries5)

    @app.route('/gallery-6')
    def collections6():
        return render_template('/gallery/gallery-6.html', entries=entries6)

    @app.route('/gallery-7')
    def collections7():
        return render_template('/gallery/gallery-7.html', entries=entries7)

    @app.route('/gallery-8')
    def collections8():
        return render_template('/gallery/gallery-8.html', entries=entries8)

    @app.route('/gallery-9')
    def collections9():
        return render_template('/gallery/gallery-9.html', entries=entries9)

    @app.route('/gallery-10')
    def collections10():
        return render_template('/gallery/gallery-10.html', entries=entries10)

    @app.route('/gallery-11')
    def collections11():
        return render_template('/gallery/gallery-11.html', entries=entries11)

    @app.route('/gallery-12')
    def collections12():
        return render_template('/gallery/gallery-12.html', entries=entries12)

    @app.route('/gallery-13')
    def collections13():
        return render_template('/gallery/gallery-13.html', entries=entries13)

    @app.route('/gallery-14')
    def collections14():
        return render_template('/gallery/gallery-14.html', entries=entries14)

    @app.route('/gallery-15')
    def collections15():
        return render_template('/gallery/gallery-15.html', entries=entries15)

    @app.route('/gallery-16')
    def collections16():
        return render_template('/gallery/gallery-16.html', entries=entries16)

    @app.route('/gallery-17')
    def collections17():
        return render_template('/gallery/gallery-17.html', entries=entries17)

    @app.route('/gallery-18')
    def collections18():
        return render_template('/gallery/gallery-18.html', entries=entries18)




    @app.route('/amc-1')
    def amccollection1():
        return render_template('/amc/amc-1.html', entries=apeentries1)

    @app.route('/amc-2')
    def amccollection2():
        return render_template('/amc/amc-2.html', entries=apeentries2)

    @app.route('/amc-3')
    def amccollection3():
        return render_template('/amc/amc-3.html', entries=apeentries3)

    @app.route('/amc-4')
    def amccollection4():
        return render_template('/amc/amc-4.html', entries=apeentries4)

    @app.route('/amc-5')
    def amccollection5():
        return render_template('/amc/amc-5.html', entries=apeentries5)

    @app.route('/amc-6')
    def amccollection6():
        return render_template('/amc/amc-6.html', entries=apeentries6)

    @app.route('/amc-7')
    def amccollection7():
        return render_template('/amc/amc-7.html', entries=apeentries7)

    @app.route('/amc-8')
    def amccollection8():
        return render_template('/amc/amc-8.html', entries=apeentries8)

    @app.route('/amc-9')
    def amccollection9():
        return render_template('/amc/amc-9.html', entries=apeentries9)

    @app.route('/amc-10')
    def amccollection10():
        return render_template('/amc/amc-10.html', entries=apeentries10)

    @app.route('/amc-11')
    def amccollection11():
        return render_template('/amc/amc-11.html', entries=apeentries11)

    @app.route('/amc-12')
    def amccollection12():
        return render_template('/amc/amc-12.html', entries=apeentries12)

    @app.route('/amc-13')
    def amccollection13():
        return render_template('/amc/amc-13.html', entries=apeentries13)

    @app.route('/amc-14')
    def amccollection14():
        return render_template('/amc/amc-14.html', entries=apeentries14)

    @app.route('/amc-15')
    def amccollection15():
        return render_template('/amc/amc-15.html', entries=apeentries15)

    @app.route('/amc-16')
    def amccollection16():
        return render_template('/amc/amc-16.html', entries=apeentries16)

    @app.route('/amc-17')
    def amccollection17():
        return render_template('/amc/amc-17.html', entries=apeentries17)

    @app.route('/amc-18')
    def amccollection18():
        return render_template('/amc/amc-18.html', entries=apeentries18)

    @app.route('/amc-19')
    def amccollection19():
        return render_template('/amc/amc-19.html', entries=apeentries19)

    @app.route('/amc-20')
    def amccollection20():
        return render_template('/amc/amc-20.html', entries=apeentries20)

    @app.route('/amc-21')
    def amccollection21():
        return render_template('/amc/amc-21.html', entries=apeentries21)

    @app.route('/amc-22')
    def amccollection22():
        return render_template('/amc/amc-22.html', entries=apeentries22)

    @app.route('/amc-23')
    def amccollection23():
        return render_template('/amc/amc-23.html', entries=apeentries23)


    

    if __name__ == '__main__':
        app.run(debug=True)

    return app
