from flask import Flask, jsonify
import repo

application = Flask(__name__)


@application.route('/jobs', methods=['GET'])
def get_jobs():
    items = repo.get_items()
    return jsonify(items)
