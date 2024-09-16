from flask import Flask, render_template,redirect, request, jsonify, session,flash
from requests import get
from pymongo import MongoClient
from bcrypt import checkpw
from datetime import datetime
from bson.json_util import dumps
Mongo_db='Ax'
app = Flask(__name__)
app.config['SECRET_KEY'] ='a881f5413500986cbd88e99456623f51e6ccde187d2e399a3f4fdcfa72008b74'
app.static_folder = 'static'
x=None
current_db=None
local_api_url = 'http://localhost:5000/api/v1'
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        # Get form data from the request
        username = request.form.get('username')
        password = request.form.get('password')
        client=MongoClient(host='localhost',port= 27017)
        db = client[Mongo_db]
        collection = db['user']
        collected_data=collection.find_one({'user_name':username})   
        if checkpw(password.encode('utf-8'),collected_data['password'].encode('utf-8')):
            for key,data in collected_data.items():
                session[key]=data
            current_db=collected_data['db_name']
            print(current_db)
            flash('Welcome {}'.format(session['user_name']),category='success')
            return redirect('/home')
        # Return an error message for invalid credentials
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        pass
    return render_template('register.html')
@app.route('/home')
def main():
    if 'user_name' not in session:
        # User is not logged in, redirect to the login page
        return redirect('/login')
    print(session)
    send_inventory=get('{}/inventory'.format(local_api_url)).json()
    datetime_1=str(datetime.now())
    send_category=get('{}/category'.format(local_api_url)).json()
    send_branch=get('{}/branch'.format(local_api_url)).json()
    send_remak=get('{}/remarks'.format(local_api_url)).json()
    username=session['user_name']
    return render_template('home.html',p=send_inventory,n=send_category,l=send_branch,username=username,t=send_remak,date=datetime_1) 
@app.route('/sales')
def sales():
    if 'user_name' not in session:
        # User is not logged in, redirect to the login page
        return redirect('/login')
    send_sales=get('{}/sales'.format(local_api_url)).json()
    return render_template('sales.html',x=send_sales)
@app.route('/pie')
def pie():
    if 'user_name' not in session:
        # User is not logged in, redirect to the login page
        return redirect('/login')
    if session['access_control'] != 'LEVEL-1-1':
        flash('You do not have access to this page',category='error')
        return redirect('/home') 
    send_days=dict(get('{}/pie/days'.format(local_api_url)).json())
    send_total_weeekly_items=get('{}/pie/total_weeekly_items'.format(local_api_url)).json()
    send_category_percentage=dict(get('{}/category/percentage'.format(local_api_url)).json())
    send_best_selling=get('{}/pie/best_selling'.format(local_api_url)).json()
    send_out_going=get('{}/pie/out_going'.format(local_api_url)).json()
    send_payment=get('{}/pie/payment'.format(local_api_url)).json()
    return render_template('pie.html',x=send_category_percentage,total_weekly=send_total_weeekly_items,days=send_days,best=send_best_selling,out_going=send_out_going,pay=send_payment)
@app.route('/noaccess')
def noaccess():
    if 'user_name' not in session:
        # User is not logged in, redirect to the login page
        return redirect('/login')
    return render_template('noaccess.html')
@app.route('/inventory')
def inventory():
    if 'user_name' not in session:
        # User is not logged in, redirect to the login page
        return redirect('/login')
    send_inventory=get('{}/inventory'.format(local_api_url)).json()
    return render_template('inventory.html',x=send_inventory)
@app.route('/out_going')
def out_going():
    if 'user_name' not in session:
        # User is not logged in, redirect to the login page
        return redirect('/login')
    send_out_going=get('{}/out_going'.format(local_api_url)).json()
    return render_template('out_going.html',x=send_out_going)
@app.route('/')
def index():
    if 'user_name' in session:
        return redirect('/home')
    return render_template('index.html')
@app.route('/logout')
def login_init():
    session.pop('user_name', None)
    return redirect('/login')
@app.route('/session', methods=['GET'])
def session_data():
    return jsonify({'user': session.get('user_name')})
@app.route('/profile')
def profile():
    if 'user_name' not in session:
        # User is not logged in, redirect to the login page
        return redirect('/login')
    user_data={
        "username":session['user_name'],
        "email":session['email'],
        "phone":session['contact'],
        "company":session['company'],
        "address":session['address'],
        "role":session['access_control'],
        "date":session['created_at']
    }
    return render_template('profile.html',user=user_data)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001,debug=True)
