from flask import Flask, request, jsonify,Blueprint
from models import storage
from api.v1.blueprints import api
from functools import wraps
import threading
app = Flask(__name__)
app.secret_key = 'a881f5413500986cbd88e99456623f51e6ccde187d2e399a3f4fdcfa72008b74'
@app.before_first_request
@app.before_first_request
def before_first_request():
    thread = threading.Thread(target=init_db)
    thread.start()
    thread.join()  # Wait for initialization to complete

    if db_name is not None:
        app.register_blueprint(api, url_prefix='/api/v1')
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404
@app.teardown_appcontext
def shutdown_session(exception=None):
    storage.close()
@app.route('/api/v1/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'comming soon!'})
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
