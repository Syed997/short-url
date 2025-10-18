from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/home')
def home():
    return 'welcome flask smart url app'

@app.route('/api/url', methods=['POST'])
def received_url():
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "not data found"}), 400
    
    actual_url = data.get('url')
    short_url = data.get('short_url')

    return jsonify({
        "message": "url shorted successfully!!",
        "short_url": short_url
    })
    
if __name__ == '__main__':
    app.run(debug=True)

