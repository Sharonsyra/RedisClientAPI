from flask import Flask, make_response, jsonify

from containers import Configs, Readers, Clients

app = Flask(__name__)

Configs.config.override({
        "host": "localhost",
        "port": "6379",
        "db": 0
})

redis_methods = Readers.redis_methods()

@app.route('/redis/api/v1.0/methods/check/<string:hash_name>/<string:key>', methods=['GET'])
def redis_hash_check(hash_name, key):
    output = redis_methods.hash_check(hash_name, key)
    return make_response(jsonify({'Exists?': output}), 200)

@app.route('/redis/api/v1.0/methods/<string:hash_name>/<string:key>/<string:value>', methods=['POST'])
def redis_set_hash(hash_name, key, value):
    output = redis_methods.set_hash(hash_name, key, value)
    if output:
        return make_response(jsonify({'Created': output}), 201)
    return make_response(jsonify({'Already Exists!': output}), 200)

@app.route('/redis/api/v1.0/methods/<string:hash_name>/<string:key>', methods=['GET'])
def redis_get_hash(hash_name, key):
    output = redis_methods.get_hash(hash_name, key)
    return make_response(jsonify({'Hash: ': str(output)}), 200)

@app.route('/redis/api/v1.0/methods/<string:hash_name>', methods=['GET'])
def redis_get_hash_dict(hash_name):
    bytes_output = redis_methods.get_hash_dist(hash_name)
    if isinstance(bytes_output, str):
        return make_response(jsonify({"Hash Dict: ": bytes_output}), 200)
    output = {str(k):str(v) for k,v in bytes_output.items()}
    return make_response(jsonify({"Hash Dict: ": output}), 200)

@app.route('/redis/api/v1.0/methods/<string:hash_name>/<string:key>', methods=['DELETE'])
def redis_delete_hash(hash_name, key):
    output = redis_methods.delete_hash(hash_name, key)
    if output:
        return make_response(jsonify({"Hash Deleted": output}), 200)
    return make_response(jsonify({"Hash does not exist": output}), 200)

if __name__ == "__main__":
    app.run(debug=True)
