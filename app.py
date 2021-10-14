from flask import Flask, render_template,redirect
from flask_pymongo import pymongo
import scrape_mars

app= Flask(__name__)

mongo=Pymongo(app, url='mongodb://localhost:27017/img_list')

@app.route('/')
def index():
    img_url=mongo.db.collection.find_one()
    return render_template('index.html',img_url=img_url)

@app.route('/scrape')
def scrape():
    marsdata=scrape_mars.scrape()
    mongo.db.collection.update({},marsdata,upsert=True)
    return redirect('/', code=302)

if__name__=='__main__':
    app.run(debug=True)