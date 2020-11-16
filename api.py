from flask import Flask, abort, request

from db import DbClient

app = Flask(__name__)


@app.route('/api/put', methods=['PUT'])
def api_put():
    values = request.get_json()
    if values is None:
        abort(400)
    print(values)
    return 'success'


@app.route('/api/get/<key>', methods=['GET'])
def api_get(key):
    if key is None:
        abort(400)
    print(key)

    return 'success'


@app.route('/api/queryAll', methods=['GET'])
def api_query_all():
    return 'hello world'


@app.route('/api/delete/<key>', methods=['DELETE'])
def api_delete(key):
    if key is None:
        abort(404)
    print(key)
    return 'success'


@app.route('/')
def hello_world():
    return 'hello world'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2020, debug=False)
    db = DbClient('/db')
