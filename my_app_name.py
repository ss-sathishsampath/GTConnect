"""
Created on Mon Mar 25 15:03:04 2019
Project Name: GTConnect
CS 6675 Advanced Internet Computing, College of Computing, Georgia Institute of Technology
@Professor & Project Guide: Dr. Ling Liu(lingliu@cc.gatech.edu)
@authors: Sathish Sampath, Jenita Lydia Jebasingh(jenita.lydia17@gmail.com), Sai Tadikonda(saitadikonda001@gmail.com), Sreyas Sriram(sreyas28@gmail.com)
"""
import os,csv,json
from flask import Flask, render_template, jsonify,request, session, redirect, url_for, _app_ctx_stack
from flask_compress import Compress
import copy
import json
import re
import datetime
import pickle
import hashlib


from datetime import timedelta
from spatial import check_ads

app = Flask(__name__)
Compress(app)
user_locations = []

user_data = {}
user_ads = {}
tags = {}


ads = {}
with open('ads.p', 'rb') as fp:
    ads = pickle.load(fp)

@app.route('/userlocation', methods=['GET', 'POST'])
def userlocation():
    lat = float(request.args.get('lat'))
    long = float(request.args.get('long'))
    user = request.args.get('user')
    

    if user not in user_ads:
        user_ads[user] = []
    result, ads_selected = check_ads(lat,long, ads, user, user_ads)
    
    
    
    for each in ads_selected:
        user_ads[user].append(each)
    

    
    return jsonify({'ad': result})


@app.route('/correct_ads', methods=['GET', 'POST'])
def correct_ads():
    for each in ads:
        print(ads)
        ads[each]['text'] = ads[each]['text'].replace("\n"," ")
        ads[each]['text'] = ads[each]['text'].replace("\r"," ")
        
    
    with open('ads.p', 'wb') as fp:
        pickle.dump(ads, fp, protocol=pickle.HIGHEST_PROTOCOL)
    
    return redirect(url_for('advertisements'))



@app.route('/advertise', methods=['GET', 'POST'])
def advertise():
    
    return render_template('advertise.html')

@app.route('/emergency', methods=['GET', 'POST'])
def emergency():
    
    return render_template('emergency.html')

@app.route('/events', methods=['GET', 'POST'])
def event():
    
    return render_template('event.html')


@app.route('/clear_ads', methods=['GET', 'POST'])
def clear_ads():
    ads.clear()
    
    with open('ads.p', 'wb') as fp:
        pickle.dump(ads, fp, protocol=pickle.HIGHEST_PROTOCOL)
    return redirect(url_for('all_ads'))


@app.route('/add_advertise', methods=['GET', 'POST'])
def add_advertise():
    lat = float(request.form['lat'])
    long = float(request.form['long'])
    s = str(request.form['sec_key'])
    
    hashed_key = int(hashlib.sha256(s.encode('utf-8')).hexdigest(), 16) % 10**8
    
    if hashed_key == 54859151:
        ad_text = request.form['ad_text']
        
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        adtype = int(request.form['type'])
        
        if ((adtype == 1) or (adtype == 3)):
            name = request.form['name']
        else:
            name = 'Emergency'
             
        numb = 0
        if len(ads) > 0:
            numb = max(ads)
        
        ads[numb+1] = {'name': name,'type': adtype, 'lat':lat, 'long': long, 'text': ad_text , 'start_date': datetime.datetime.strptime(start_date , '%Y-%m-%d') , 'end_date':  datetime.datetime.strptime(end_date , '%Y-%m-%d')}
    
        with open('ads.p', 'wb') as fp:
            pickle.dump(ads, fp, protocol=pickle.HIGHEST_PROTOCOL)
    
    return redirect(url_for('advertisements'))

@app.route('/messages', methods=['GET', 'POST'])
def messages():
    print(request.form)
    if 'msg' in request.form:
        msg = request.form['msg']
        user = request.form['user']
        if user not in user_data:
            user_data[user] = []
        user_data[user].append(msg)
    else:
        msg = ""
    
    
    return jsonify({'text': msg})

@app.route('/all_ads',methods=['GET', 'POST'])
def all_ads():
    return jsonify(ads)


@app.route('/view_user_ad',methods=['GET', 'POST'])
def view_user_ad():
    return jsonify(user_ads)

@app.route('/clear_user_ad',methods=['GET', 'POST'])
def clear_user_ad():
    user_ads.clear()
    return redirect(url_for('view_user_ad'))

@app.route('/advertisements',methods=['GET', 'POST'])
def advertisements():
    adv = {}
    today = datetime.datetime.now()
    for each in ads:
#        print(ads[each]['end_date'])
        ad_end = datetime.datetime(ads[each]['end_date'].year, ads[each]['end_date'].month, ads[each]['end_date'].day)
        end = ad_end + timedelta(1)
        if((today > ads[each]['start_date']) and (today < end)):
            adv[each] = ads[each]
            
            
    return render_template('advertisements.html', ads= adv)

@app.route('/all_msg',methods=['GET', 'POST'])
def all_msg():
    return jsonify(user_data)


    
if __name__ == "__main__":
	app.run(debug=True,threaded=True) #,port=5000