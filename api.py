from flask import Flask, abort, request

from db import DbClient

app = Flask(__name__)
db = DbClient('/db')

@app.route('/api/put', methods=['PUT'])
def api_put():
    data = request.get_json()
    if data is None:
        abort(400)
    if data.get('key') is None or data.get('value') is None:
        abort(400)
    print(data)
    db.put(data.get('key'),data.get('value'))
    return 'success'


@app.route('/api/get/<key>', methods=['GET'])
def api_get(key):
    if key is None:
        abort(400)
    print(key)
    value = db.get(key)
    if value is None:
        return 'value not found'
    else:
        return value.decode()


@app.route('/api/queryAll', methods=['GET'])
def api_query_all():
    res = db.query_all()
    print(res)
    return res


@app.route('/api/delete/<key>', methods=['DELETE'])
def api_delete(key):
    if key is None:
        abort(404)
    db.delete(key)
    return 'success'


@app.route('/')
def hello_world():
    return 'hello world'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2020, debug=True)

