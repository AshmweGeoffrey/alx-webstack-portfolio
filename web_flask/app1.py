from flask import Flask, render_template,redirect, request, jsonify, session
from requests import get
app = Flask(__name__)
app.config['SECRET_KEY'] ='a881f5413500986cbd88e99456623f51e6ccde187d2e399a3f4fdcfa72008b74'
app.static_folder = 'static'
x=None
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
        users=get('{}/post/login'.format(local_api_url)).json()
        # Fetch user data from the database
        # Check if the provided credentials are valid
        if username in users and users[username] == password:
            session['user'] = username
            x=username
            return redirect('/home')
        # Return an error message for invalid credentials
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')
@app.route('/home')
def main():
    if 'user' not in session:
        # User is not logged in, redirect to the login page
        return redirect('/login')
    send_inventory=get('{}/inventory'.format(local_api_url)).json()
    send=get('{}/user/{}'.format(local_api_url,session['user'])).json()
    send_category=get('{}/category'.format(local_api_url)).json()
    send_branch=get('{}/branch'.format(local_api_url)).json()
    send_remak=get('{}/remarks'.format(local_api_url)).json()
    username=session['user']
    return render_template('home.html',x=send,p=send_inventory,n=send_category,l=send_branch,username=username,t=send_remak) 
@app.route('/sales')
def sales():
    if 'user' not in session:
        # User is not logged in, redirect to the login page
        return redirect('/login')
    send_sales=get('{}/sales'.format(local_api_url)).json()
    return render_template('sales.html',x=send_sales)
@app.route('/pie')
def pie():
    if 'user' not in session:
        # User is not logged in, redirect to the login page
        return redirect('/login')
    if session['user'] != 'Ashimwe_Geoffrey':
        return redirect('/noaccess') 
    send_days=dict(get('{}/pie/days'.format(local_api_url)).json())
    send_total_weeekly_items=get('{}/pie/total_weeekly_items'.format(local_api_url)).json()
    send_category_percentage=dict(get('{}/category/percentage'.format(local_api_url)).json())
    send_best_selling=get('{}/pie/best_selling'.format(local_api_url)).json()
    send_out_going=get('{}/pie/out_going'.format(local_api_url)).json()
    send_payment=get('{}/pie/payment'.format(local_api_url)).json()
    return render_template('pie.html',x=send_category_percentage,total_weekly=send_total_weeekly_items,days=send_days,best=send_best_selling,out_going=send_out_going,pay=send_payment)
@app.route('/noaccess')
def noaccess():
    if 'user' not in session:
        # User is not logged in, redirect to the login page
        return redirect('/login')
    return render_template('noaccess.html')
@app.route('/inventory')
def inventory():
    if 'user' not in session:
        # User is not logged in, redirect to the login page
        return redirect('/login')
    send_inventory=get('{}/inventory'.format(local_api_url)).json()
    return render_template('inventory.html',x=send_inventory)
@app.route('/out_going')
def out_going():
    if 'user' not in session:
        # User is not logged in, redirect to the login page
        return redirect('/login')
    send_out_going=get('{}/out_going'.format(local_api_url)).json()
    return render_template('out_going.html',x=send_out_going)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/logout')
def login_init():
    session.pop('user', None)
    return redirect('/login')
@app.route('/session', methods=['GET'])
def session_data():
    return jsonify({'user': session.get('user')})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001,debug=True)
