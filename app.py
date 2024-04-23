from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/test/<string:key>', methods=['GET'])
def det_tasks(key):
    return redis.get('key')


@app.route('/test/', methods=['POST'])
def create_task(key, value):
    return redis.set(key, value)


@app.route('/test/<string:key>', methods=['PUT'])
def update_task(key, value):
    return redis.set(key, value)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
