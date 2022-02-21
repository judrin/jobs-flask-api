from flask import Flask, jsonify
import repo

application = Flask(__name__)


@application.route('/', methods=['GET'])
def home():
    return 'Hello! :)'


@application.route('/jobs', methods=['GET'])
def get_jobs():
    items = repo.get_items()
    return jsonify(items)


if __name__ == "__main__":
    application.run()
