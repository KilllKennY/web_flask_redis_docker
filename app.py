from flask import Flask, request
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/test/<string:key>', methods=['GET'])
def det_value(key):
    value = redis.get(key)
    return value if value is not None else f'Key: {key} not found'

@app.route('/test/', methods=['POST', 'PUT'])
def create_value():
    key = request.json['key']
    value = request.json['value']
    redis.set(key, value)
    return f'Data created: {key}: {value}'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
