from flask import Flask, request, jsonify,Blueprint
from models import storage
from api.v1.blueprints import api
from functools import wraps
import os
import threading
app = Flask(__name__)
app.secret_key = os.getenv('API_SECRET_KEY')
app.register_blueprint(api, url_prefix='/api/v1')
@app.errorhandler(404)
def not_found(error):
    # 404 error page
    return jsonify({'error': 'Not found'}), 404
@app.teardown_appcontext
def shutdown_session(exception=None):
    # Close the current SQLAlchemy session uppon teardown
    storage.close()
@app.route('/api/v1/hello', methods=['GET'])
def hello():
    # Return a welcome message [Test endpoint]
    return jsonify({'message': 'comming soon!'})
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
