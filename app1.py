from flask import Flask, render_template,redirect, request, jsonify, session,flash,g
from requests import get
from pymongo import MongoClient
from bcrypt import checkpw
from datetime import datetime
import redis
import os
import secrets
Mongo_db=os.getenv('VAR_MONGO_DB')
current_db=os.getenv('VAR_CURRENT_DB')
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('VAR_SECRET_KEY')
app.static_folder = 'static'
local_api_url = os.getenv('VAR_LOCAL_API_URL')
app.config['SESSION_COOKIE_SECURE'] = True
@app.errorhandler(404)
def not_found(error):
    # 404 error page
    return render_template('404.html'), 404
@app.route('/login', methods=['POST','GET'])
def login():
    # implement login page
    if request.method == 'POST':
        # Get form data from the request
        username = request.form.get('username')
        password = request.form.get('password')
        client=MongoClient(host='localhost',port= 27017)
        db = client[Mongo_db]
        collection = db['user']
        collected_data=collection.find_one({'user_name':username})
        if not collected_data:
            return render_template('login.html', error='Invalid username or password') 
        if checkpw(password.encode('utf-8'),collected_data['password'].encode('utf-8')):
            for key,data in collected_data.items():
                session[key]=data
            if session['status'] == 'inactive':
                flash('Your account is inactive',category='error')
                return render_template('login.html')
            db_collected=collected_data['db_name']
            client = redis.Redis(host='localhost', port=6379, db=0)
            client.set(current_db,db_collected)
            flash('Welcome {}'.format(session['user_name']),category='success')
            return redirect('/home')
        # Return an error message for invalid credentials
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')
@app.route('/register', methods=['GET'])
def register():
    # Redirect to the register page
    return render_template('register.html')
@app.route('/set_up', methods=['GET'])
def set_up():
    # load the set-up page construct db category and branch
    if 'user_name' not in session:
        # User is not logged in, redirect to the login page
        return redirect('/login')
    elif session['access_control'] != 'LEVEL-1':
        flash('You do not have access to this page',category='error')
        return redirect('/home')
    send_category=get('{}/category'.format(local_api_url)).json()
    send_branch=get('{}/branch'.format(local_api_url)).json()
    return render_template('set-up.html',o=send_category,p=send_branch)
@app.route('/user_db', methods=['GET'])
def user_db():
    # [no longer used to deliver  front-end]Get the user database name from the session(Discouraged)
    return jsonify({'user_db': session['db_name']})
@app.route('/home')
def main():
    # Main Dashboard (with user loaded)
    if 'user_name' not in session:
        # User is not logged in, redirect to the login page
        return redirect('/login')
    send_inventory=get('{}/inventory'.format(local_api_url)).json()
    datetime_1=str(datetime.now())
    send_category=get('{}/category'.format(local_api_url)).json()
    send_branch=get('{}/branch'.format(local_api_url)).json()
    send_remak=get('{}/remarks'.format(local_api_url)).json()
    username=session['user_name']
    return render_template('home.html',p=send_inventory,n=send_category,l=send_branch,username=username,t=send_remak,date=datetime_1) 
@app.route('/sales')
def sales():
    # load the sales page
    if 'user_name' not in session:
        # User is not logged in, redirect to the login page
        return redirect('/login')
    send_sales=get('{}/sales'.format(local_api_url)).json()
    return render_template('sales.html',x=send_sales)
@app.route('/pie')
def pie():
    # load the pie page and data to load in charts
    if 'user_name' not in session:
        # User is not logged in, redirect to the login page
        return redirect('/login')
    if session['access_control'] != 'LEVEL-1':
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
    # no longer need to pass the session data to the front end (Discouraged)
    if 'user_name' not in session:
        # User is not logged in, redirect to the login page
        return redirect('/login')
    return render_template('noaccess.html')
@app.route('/inventory')
def inventory():
    # load the inventory page
    if 'user_name' not in session:
        # User is not logged in, redirect to the login page
        return redirect('/login')
    send_inventory=get('{}/inventory'.format(local_api_url)).json()
    return render_template('inventory.html',x=send_inventory)
@app.route('/out_going')
def out_going():
    # load the out_going page
    if 'user_name' not in session:
        # User is not logged in, redirect to the login page
        return redirect('/login')
    send_out_going=get('{}/out_going'.format(local_api_url)).json()
    return render_template('out_going.html',x=send_out_going)
@app.route('/')
def index():
    # Main page
    if 'user_name' in session:
        return redirect('/home')
    return render_template('index.html')
@app.route('/activate/<user_name>', methods=['GET'])
def activate(user_name):
    # Get the username from the URL and activate user account
    user_name=request.view_args['user_name']
    client=MongoClient(host='localhost',port= 27017)
    db = client[Mongo_db]
    collection = db['user']
    collection.find_one_and_update({'user_name': user_name},{'$set': {'status': 'active'}})
    return render_template('activate.html',p=user_name)
@app.route('/logout')
def login_init():
    # remove the username from the session if it is there
    session.pop('user_name', None)
    return redirect('/')
@app.route('/session', methods=['GET'])
def session_data():
    # no longer need to pass the session data to the front end
    return jsonify({'user': session.get('user_name')})
@app.route('/profile')
def profile():
    # load the profile page
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
        "date":session['created_at'],
        "status":session['status']
    }
    return render_template('profile.html',user=user_data)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001,debug=True)